#!/usr/bin/env python3
"""Prepare a reviewed catalog candidate from approved public releases; never publish it."""
import argparse,copy,datetime,hashlib,json,os,re,urllib.request,zipfile,stat
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--output',required=True,type=Path);p.add_argument('--revision',required=True);p.add_argument('--reuse-from',type=Path);a=p.parse_args()
if a.output.exists():p.error('Output must be a new directory')
if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{0,63}',a.revision):p.error('Invalid revision')
kit=Path(__file__).resolve().parents[1];base=json.loads((kit/'lib/catalog.json').read_text());a.output.mkdir(parents=True);records=[];changes=[]
class SafeRedirect(urllib.request.HTTPRedirectHandler):
 """Reject API credential redirects and limit public ZIP redirects to GitHub asset hosts."""
 def redirect_request(self,req,fp,code,msg,headers,newurl):
  """Validate the response redirect before returning a new urllib request.

  Arguments follow HTTPRedirectHandler: req is the original request, fp the response,
  code/msg the HTTP status, headers the response headers and newurl the target.
  Raises ValueError for unexpected hosts or any authenticated API redirect.
  """
  target=urllib.parse.urlparse(newurl)
  if req.host=='api.github.com' or target.scheme!='https' or target.hostname not in ['github.com','release-assets.githubusercontent.com','objects.githubusercontent.com']:raise ValueError('Unexpected redirect')
  return super().redirect_request(req,fp,code,msg,headers,newurl)
def get(url,limit,api=False):
 """Return bounded response bytes from url; limit is the maximum byte count.

 api selects JSON metadata and optional operator-only authentication. Credentials
 never enter public asset requests or saved artifacts. Network errors abort preparation.
 """
 headers={'User-Agent':'deckerweb-catalog-preparation','Accept':'application/vnd.github+json'if api else'application/octet-stream'}
 token=os.environ.get('DECKERWEB_CATALOG_GITHUB_TOKEN')if api else None
 if token:headers['Authorization']='Bearer '+token
 req=urllib.request.Request(url,headers=headers)
 with urllib.request.build_opener(SafeRedirect()).open(req,timeout=30)as r:
  data=r.read(limit+1)
 if len(data)>limit:raise ValueError('Response exceeds allowed size')
 return data
try:
 for old in base['plugins']:
  if not old.get('approved'):continue
  repo=old['repository'];assert re.fullmatch(r'deckerweb/[A-Za-z0-9_.-]+',repo)
  repo_info=json.loads(get('https://api.github.com/repos/'+repo,1048576,True));assert repo_info.get('private')is False,'Private repositories cannot enter the public feed'
  release=json.loads(get('https://api.github.com/repos/'+repo+'/releases/latest',1048576,True));assert not release['draft']and not release['prerelease']
  version=release['tag_name'].removeprefix('v');assert re.fullmatch(r'\d+\.\d+\.\d+(?:-[A-Za-z0-9.-]+)?',version)
  names=[old['slug']+'-'+version+'.zip',old['slug']+'.zip'];asset=next((x for name in names for x in release['assets']if x['name']==name),None);assert asset,'No unambiguous plugin release ZIP'
  url=asset['browser_download_url'];assert re.fullmatch(r'https://github.com/'+re.escape(repo)+r'/releases/download/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\.zip',url)
  cached=a.reuse_from/(old['slug']+'.zip')if a.reuse_from else None
  binary=cached.read_bytes()if cached and cached.is_file()and asset.get('digest')=='sha256:'+hashlib.sha256(cached.read_bytes()).hexdigest()else get(url,20*1024*1024)
  digest=hashlib.sha256(binary).hexdigest()
  if asset.get('digest'):assert asset['digest']=='sha256:'+digest
  path=a.output/(old['slug']+'.zip');path.write_bytes(binary)
  with zipfile.ZipFile(path)as z:
   seen=set();total=0;assert len(z.infolist())<=3000
   for i in z.infolist():
    n=i.filename;assert '\\'not in n and not n.startswith('/')and '..'not in n.split('/')and stat.S_IFMT(i.external_attr>>16)!=stat.S_IFLNK
    assert n not in seen;seen.add(n);total+=i.file_size;assert total<=80*1024*1024
    if not n.startswith('__MACOSX/')and Path(n).name!='.DS_Store':assert n.split('/')[0]==old['slug']
   info=z.getinfo(old['plugin_file']);assert info.file_size<=2*1024*1024
   with z.open(info)as f:main=f.read(8192).decode('utf-8-sig')
  def header(key):
   """Return one trimmed header from the bounded main-file text, including the legacy WP alias."""
   m=re.search(r'(?mi)^\s*\*?\s*'+re.escape(key)+r':\s*(.+)$',main)
   if not m and key=='Requires at least':m=re.search(r'(?mi)^\s*\*?\s*Requires WP:\s*(.+)$',main)
   return m[1].strip()if m else''
  assert header('Version')==version and header('Plugin Name')==old['name']
  identity=header('Update URI')or header('Plugin URI');assert identity.rstrip('/')=='https://github.com/'+repo
  for key in ['Requires at least','Requires PHP']:assert re.fullmatch(r'\d+\.\d+(?:\.\d+)?',header(key))
  entry=copy.deepcopy(old);entry.update(github_stars=repo_info['stargazers_count'],stars_checked_at=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d'),version=version,download_url=url,sha256=digest,requires_wp=header('Requires at least'),requires_php=header('Requires PHP'),published_at=release['published_at']);base['plugins'][base['plugins'].index(old)]=entry
  records.append({'slug':old['slug'],'release_id':release['id'],'tag':release['tag_name'],'published_at':release['published_at'],'asset':asset['name'],'download_url':url,'sha256':digest,'description_header':header('Description')})
  if old['version']!=version:changes.append({'slug':old['slug'],'before':old['version'],'after':version,'review':['Review localized descriptions, dependencies, network policy and artwork before approval.']})
 base.update(catalog_revision=a.revision,generated_at=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),requires_library='0.1.0')
 (a.output/'candidate.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n');(a.output/'sources.json').write_text(json.dumps({'plugins':records},indent=2)+'\n');(a.output/'review.json').write_text(json.dumps({'status':'review_required','changes':changes,'candidate_sha256':hashlib.sha256((a.output/'candidate.json').read_bytes()).hexdigest()},indent=2)+'\n')
 print('Candidate prepared; review metadata and approve explicitly. Nothing published.')
except Exception as error:
 print('Stopped while reviewing '+old['slug']+'.')
 print('Preparation stopped. Check approved repository access, release ZIP identity and limits; no catalog approved or published.');raise SystemExit(1)
