#!/usr/bin/env python3
import json,sys
from pathlib import Path
P=Path(__file__).resolve().parent.parent/'evals'/'cases.json'; d=json.loads(P.read_text()); errors=[]; seen=set()
for i,c in enumerate(d.get('cases',[])):
    cid=c.get('id')
    if not cid or cid in seen: errors.append(f'case {i}: missing/duplicate id {cid!r}')
    seen.add(cid)
    for k in ('prompt','expect_mode','must_include','must_not'):
        if k not in c: errors.append(f'{cid}: missing {k}')
    if not isinstance(c.get('must_include'),list) or not isinstance(c.get('must_not'),list): errors.append(f'{cid}: must lists invalid')
if len(seen)<10: errors.append('expected at least 10 eval cases')
if errors: print('\n'.join('ERROR: '+x for x in errors)); sys.exit(2)
print(f'VALID eval suite: {len(seen)} cases')
