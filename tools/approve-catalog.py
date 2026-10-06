#!/usr/bin/env python3
"""Export the exact reviewed candidate as a public catalog artifact, without publishing."""
import argparse,hashlib,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('candidate',type=Path);p.add_argument('destination',type=Path);p.add_argument('--sha256',required=True);a=p.parse_args()
raw=a.candidate.read_bytes()
if a.destination.exists():p.error('Destination must be new')
if hashlib.sha256(raw).hexdigest()!=a.sha256:p.error('Candidate changed since review')
d=json.loads(raw)
if d.get('schema_version')!=1 or not d.get('catalog_revision')or not isinstance(d.get('plugins'),list):p.error('Invalid candidate')
# Candidate package/metadata validation is performed by refresh-catalog and runtime validation.
a.destination.parent.mkdir(parents=True,exist_ok=True);a.destination.write_bytes(raw);print('Reviewed catalog artifact exported. Nothing published.')
