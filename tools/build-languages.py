#!/usr/bin/env python3
"""Compile component messages for loading into the host plugin's existing text domain."""
from pathlib import Path
import json,struct
kit=Path(__file__).resolve().parents[1];lib=kit/'lib';data=json.loads((lib/'messages.json').read_text());version=json.loads((lib/'compatibility.json').read_text())['version'];out=lib/'languages';out.mkdir(exist_ok=True)
def compile_mo(messages):
 """Return GNU gettext MO bytes from a source-to-translation mapping.

 Sorted entries and valid table offsets support the minimum WordPress POMO reader;
 no text domain is embedded because the host supplies it at load time.
 """
 keys=sorted(messages);ids=b'';strings=b'';ki=[];vi=[]
 for k in keys:
  a=k.encode();b=messages[k].encode();ki.append((len(a),len(ids)));vi.append((len(b),len(strings)));ids+=a+b'\0';strings+=b+b'\0'
 n=len(keys);base=28+16*n;second=base+len(ids)
 return struct.pack('<7I',0x950412de,0,n,28,28+8*n,0,base)+b''.join(struct.pack('<2I',l,base+o)for l,o in ki)+b''.join(struct.pack('<2I',l,second+o)for l,o in vi)+ids+strings
for locale in ['de_DE','de_DE_formal']:
 d={k:v[locale]for k,v in data.items()};assert all(d.values()),'Missing translation';d['']='Project-Id-Version: deckerweb Library '+version+'\nLanguage: '+locale+'\nContent-Type: text/plain; charset=UTF-8\nPlural-Forms: nplurals=2; plural=(n != 1);\n';(out/(locale+'.mo')).write_bytes(compile_mo(d));(out/(locale+'.po')).write_text('\n\n'.join('msgid '+json.dumps(k,ensure_ascii=False)+'\nmsgstr '+json.dumps(v,ensure_ascii=False)for k,v in sorted(d.items()))+'\n')
(out/'messages.pot').write_text('\n\n'.join('msgid '+json.dumps(k,ensure_ascii=False)+'\nmsgstr ""'for k in sorted(data))+'\n')
print(len(data),'messages compiled for host domains')
