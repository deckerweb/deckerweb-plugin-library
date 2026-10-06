#!/usr/bin/env python3
"""Compatibility wrapper for BAS integration."""
import argparse,subprocess,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('destination');p.add_argument('--version',required=True);a=p.parse_args()
subprocess.run([sys.executable,str(Path(__file__).with_name('prepare-plugin.py')),a.source,a.destination,'--slug','brand-admin-schemes','--version',a.version],check=True)
