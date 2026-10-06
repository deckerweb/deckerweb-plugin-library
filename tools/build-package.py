#!/usr/bin/env python3
"""Build separate runtime and authoring-kit ZIPs with checked manifests and no private working records."""
from pathlib import Path
import json,hashlib,zipfile,argparse
p=argparse.ArgumentParser();p.add_argument('destination',type=Path);a=p.parse_args();kit=Path(__file__).resolve().parents[1];lib=kit/'lib';m=json.loads((lib/'compatibility.json').read_text());version=m['version'];runtime=[f for f in lib.rglob('*')if f.is_file()and f.name not in ['compatibility.json','host.json','messages.json']and f.suffix not in ['.po','.pot']];m['files']=sorted(str(f.relative_to(lib))for f in runtime);m['hashes']={name:hashlib.sha256((lib/name).read_bytes()).hexdigest()for name in m['files']};(lib/'compatibility.json').write_text(json.dumps(m,indent=2)+'\n')
a.destination.mkdir(parents=True,exist_ok=True)
for kind in ['runtime','kit']:
 out=a.destination/('deckerweb-plugin-library-'+('runtime-'if kind=='runtime'else'')+version+'.zip')
 if out.exists():p.error('Destination exists: '+str(out))
 with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED)as z:
  files=runtime+[lib/'compatibility.json',kit/'LICENSE']if kind=='runtime'else[f for f in kit.rglob('*')if f.is_file()and'__pycache__'not in f.parts]
  for f in sorted(files):
   if kind=='runtime':name='deckerweb-plugin-library/'+(str(f.relative_to(lib))if f.is_relative_to(lib)else'LICENSE')
   else:name='deckerweb-plugin-library/'+str(f.relative_to(kit))
   if any(part in ['.git','node_modules']for part in f.parts) or f.name == 'pending-plugins.json':continue
   if any(term in f.name.lower()for term in ['sub-spec','audit','spezifikation']):p.error('Internal document in public package')
   z.write(f,name)
 print(out.resolve())
