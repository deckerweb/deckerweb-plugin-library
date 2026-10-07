#!/usr/bin/env python3
"""Prepare a new direct-distribution integration draft for a supported host; never overwrite a source."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import argparse,re,shutil,tempfile,json
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('source',type=Path);p.add_argument('destination',type=Path)
p.add_argument('--slug',required=True,choices=['brand-admin-schemes','daily-scripture']);p.add_argument('--version',required=True)
a=p.parse_args()
if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[a-zA-Z0-9.-]+)?',a.version):p.error('Invalid version')
if a.destination.exists() or a.destination.resolve()==a.source.resolve():p.error('Destination must be new')
kit=Path(__file__).resolve().parents[1];manifest=json.loads((kit/'lib/compatibility.json').read_text())
def replace_block(text,start,end,body):
 if start in text or end in text:
  if text.count(start)!=1 or text.count(end)!=1 or text.index(start)>text.index(end):p.error('Ambiguous integration block')
  return text[:text.index(start)]+body+text[text.index(end)+len(end):]
 return text.rstrip()+'\n\n'+body+'\n'
def version(v):return tuple(map(int,v.split('.')))
with tempfile.TemporaryDirectory() as temp:
 root=Path(temp)
 with ZipFile(a.source) as z:
  if len(z.infolist())>5000 or sum(i.file_size for i in z.infolist())>150*1024*1024:p.error('Unexpected archive size')
  seen=set()
  for i in z.infolist():
   q=Path(i.filename)
   if q.is_absolute() or '..' in q.parts or '\\' in i.filename or (i.external_attr>>16)&0o170000==0o120000:p.error('Unsafe archive')
   if not q.parts or q.parts[0]=='__MACOSX' or q.name=='.DS_Store':continue
   if q.parts[0]!=a.slug or i.filename in seen:p.error('Unexpected root or duplicate archive path')
   seen.add(i.filename);z.extract(i,root)
 plugin=root/a.slug;main=plugin/(a.slug+'.php');text=main.read_text()
 # Reorder only the known host header; preserve body, version markers and other code.
 blocks=list(re.finditer(r'/\*.*?\*/',text,re.S));header=next((b for b in blocks if re.search(r'(?m)^\s*\*?\s*Plugin Name:',b.group())),None)
 if not header:p.error('Missing host header')
 fields={};extras=[]
 for line in header.group().splitlines()[1:-1]:
  cleaned=re.sub(r'^\s*\*?\s?', '',line).strip();match=re.match(r'([A-Za-z ]+):\s*(.*)',cleaned)
  if match:fields[match[1].strip()]=match[2].strip()
  elif cleaned:extras.append(cleaned)
 if 'Copyright'in fields:extras.append('Copyright: '+fields.pop('Copyright'))
 copyrights=[x for x in extras if x.startswith('Copyright')];spdx=[x for x in extras if x.startswith('SPDX-License-Identifier')];other=[x for x in extras if x not in copyrights+spdx]
 extras=(copyrights or ['Copyright © 2026 David Decker – DECKERWEB.'])+(spdx or ['SPDX-License-Identifier: GPL-2.0-or-later'])+other
 order=['Plugin Name','Plugin URI','Description','Version','Requires at least','Requires PHP','Author','Author URI','License','License URI','Text Domain','Domain Path','Update URI','GitHub Plugin URI']
 new='/**\n'+'\n'.join(' * '+key+': '+fields[key]for key in order if key in fields)+'\n *\n'+'\n'.join(' * '+line for line in extras)+'\n */'
 unknown=[key for key in fields if key not in order]
 if unknown:p.error('Unreviewed extra host header fields: '+', '.join(unknown))
 text=text[:header.start()]+new+text[header.end():]

 if re.search(r'\?>\s*$',text):p.error('Closing PHP tag requires manual integration')
 for header,required in [('Requires PHP',manifest['requires_php']),('Requires at least',manifest['requires_wp'])]:
  m=re.search(r'(?m)^\s*\*?\s*'+re.escape(header)+r':\s*(\d+(?:\.\d+){1,2})\s*$',text)
  if not m or version(m[1])<version(required):p.error(header+' conflicts with Library '+required+'; agree on host requirements before building')
 old=re.search(r'(?m)^(\s*\*?\s*Version:\s*)(\S+)',text)
 if not old:p.error('Plugin header not found')
 text=re.sub(r'(?m)^(\s*\*?\s*Version:\s*)\S+',lambda m:m[1]+a.version,text,count=1)
 pattern=r"(const VERSION = ')[^']+('; )" if False else (r"(const VERSION = ')[^']+('; )" if False else r"(const VERSION = ')[^']+(';)")
 if a.slug=='daily-scripture':pattern=r"(define\( 'DAILY_SCRIPTURE_VERSION', ')[^']+(' \);)"
 text,n=re.subn(pattern,lambda m:m[1]+a.version+m[2],text,count=1)
 if n!=1:p.error('Supported runtime version marker not found')
 start='// BEGIN deckerweb Library integration';end='// END deckerweb Library integration'
 legacy='// Shared embedded catalog; elect one runtime after all active plugins have loaded.'
 if legacy in text:
  legacy_pattern=re.escape(legacy)+r"\nrequire_once __DIR__ \. '/includes/deckerweb-plugin-library/bootstrap\.php';\ndeckerweb_library_register(?:_v2)?\( __FILE__, \[\], __DIR__ \. '/includes/deckerweb-plugin-library' \);"
  text,n=re.subn(legacy_pattern,'',text,count=1)
  if n!=1:p.error('Legacy registration needs manual review')
 if 'deckerweb_library_register' in text and start not in text:p.error('Unknown integration requires manual review')
 body=start+"\nrequire_once __DIR__ . '/includes/deckerweb-plugin-library/bootstrap.php';\ndeckerweb_library_register_v2( __FILE__, [], __DIR__ . '/includes/deckerweb-plugin-library' );\n"+end
 text=replace_block(text,start,end,body);main.write_text(text)
 for f in ('readme.txt','readme-de.txt'):
  q=plugin/f
  if q.exists():q.write_text(re.sub(r'(?m)^Stable tag:.*$','Stable tag: '+a.version,q.read_text()))
 target=plugin/'includes/deckerweb-plugin-library'
 if target.exists():shutil.rmtree(target)
 shutil.copytree(kit/'lib',target)
 for resource in list(target.rglob('*')):
  if resource.is_file() and (resource.name=='messages.json' or resource.suffix in ['.po','.pot']):resource.unlink()
 (target/'host.json').write_text(json.dumps({'host':a.slug+'/'+a.slug+'.php','text_domain':a.slug,'protocol':2},indent=2)+'\n')
 uninstall=plugin/'uninstall.php';u=uninstall.read_text() if uninstall.exists() else "<?php\nif ( ! defined( 'WP_UNINSTALL_PLUGIN' ) ) { exit; }\n"
 if re.search(r'\?>\s*$',u):p.error('Host uninstall closing tag needs manual review')
 us='// BEGIN deckerweb Library cleanup';ue='// END deckerweb Library cleanup'
 ub=us+"\nrequire_once __DIR__ . '/includes/deckerweb-plugin-library/lifecycle.php';\ndeckerweb_library_uninstall_v3( __DIR__ . '/"+a.slug+".php' );\n"+ue
 if us not in u:
  legacy_cleanup=re.compile(r"require_once __DIR__ \. '/includes/deckerweb-plugin-library/lifecycle\.php';\ndeckerweb_library_uninstall_v[23]\( __DIR__ \. '/"+re.escape(a.slug)+r"\.php' \);")
  u=legacy_cleanup.sub('',u,count=1)
 reviewed_control=u.replace("if ( ! defined( 'WP_UNINSTALL_PLUGIN' ) ) { exit; }",'').replace("defined( 'WP_UNINSTALL_PLUGIN' ) || exit;",'')
 reviewed_control=re.sub(r"if\s*\(\s*!\s*defined\s*\(\s*'WP_UNINSTALL_PLUGIN'\s*\)\s*\)\s*\{\s*exit;\s*\}",'',reviewed_control,count=1)
 if a.slug=='daily-scripture':
  # This reviewed autoloader's return exits only its closure, not uninstall.php.
  autoload=re.compile(r"spl_autoload_register\(\s*static function \( \$class_name \) \{.*?\n[ \t]*\}[ \t]*\n[ \t]*\);",re.S)
  reviewed_control=autoload.sub('',reviewed_control)
 if us not in u and ('return;' in reviewed_control or 'exit;' in reviewed_control):p.error('Conditional host uninstall needs manual cleanup integration')
 uninstall.write_text(replace_block(u,us,ue,ub))
 a.destination.parent.mkdir(parents=True,exist_ok=True)
 with ZipFile(a.destination,'x',ZIP_DEFLATED) as z:
  for q in sorted(plugin.rglob('*')):
   if q.is_file():
    parts=q.relative_to(plugin).parts
    if any(x in ['.git','node_modules','tests','tools','__pycache__'] for x in parts):continue
    z.write(q,q.relative_to(root))
print(a.destination.resolve())
