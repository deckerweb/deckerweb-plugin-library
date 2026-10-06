#!/usr/bin/env python3
"""Refresh only dated GitHub star snapshots in the curated catalog, atomically."""
from pathlib import Path
from datetime import datetime,timezone
import json,re,urllib.request,argparse
p=argparse.ArgumentParser();p.add_argument('--catalog',type=Path,default=Path(__file__).resolve().parents[1]/'lib/catalog.json');a=p.parse_args();data=json.loads(a.catalog.read_text())
for entry in data['plugins']:
 if not entry.get('approved'):continue
 repo=entry['repository']
 if not re.fullmatch(r'deckerweb/[a-zA-Z0-9_.-]+',repo):p.error('Untrusted repository')
 request=urllib.request.Request('https://api.github.com/repos/'+repo,headers={'User-Agent':'deckerweb-release-preparation','Accept':'application/vnd.github+json'})
 with urllib.request.urlopen(request,timeout=15) as response:count=json.load(response)['stargazers_count']
 if not isinstance(count,int) or count<0:p.error('Invalid star count')
 entry['github_stars']=count;entry['stars_checked_at']=datetime.now(timezone.utc).date().isoformat()
 print(repo,count)
temporary=a.catalog.with_suffix('.json.tmp');temporary.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');temporary.replace(a.catalog)
