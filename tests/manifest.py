"""Fail if any runtime file differs from the compatibility manifest."""
from pathlib import Path
import hashlib
import json
root = Path(__file__).resolve().parents[1] / 'lib'
manifest = json.loads((root / 'compatibility.json').read_text())
for name in manifest['files']:
    path = Path(name)
    assert not path.is_absolute() and '..' not in path.parts, name
    assert hashlib.sha256((root / path).read_bytes()).hexdigest() == manifest['hashes'][name], name
print(f"PASS {len(manifest['files'])} runtime hashes")
