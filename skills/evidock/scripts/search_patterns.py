#!/usr/bin/env python3
"""Search Evidock's launch-pattern library. Standard library only."""
from __future__ import annotations
import argparse,json
from pathlib import Path
HERE=Path(__file__).resolve().parent.parent; DB=HERE/'assets'/'patterns.json'
def hay(p): return ' '.join([p.get('id',''),p.get('category',''),p.get('severity',''),p.get('title',''),p.get('summary',''),p.get('remediation',''),' '.join(p.get('evidence_signals',[])),' '.join(p.get('tags',[]))]).lower()
def token_matches(token,text):
    if token in text: return True
    aliases={'missing':('absent','no ','not found'),'broken':('dead','fails','does not resolve'),'readme':('front door','front-door')}; return any(a in text for a in aliases.get(token,()))
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--query',default=''); ap.add_argument('--category'); ap.add_argument('--severity'); ap.add_argument('--limit',type=int,default=20); ap.add_argument('--format',choices=['text','json'],default='text'); ap.add_argument('--list-categories',action='store_true'); a=ap.parse_args(); data=json.loads(DB.read_text(encoding='utf-8')); items=data['patterns']
    if a.list_categories: print('\n'.join(sorted({p['category'] for p in items}))); return
    q=a.query.lower().strip(); out=[]
    for p in items:
        if a.category and p['category'].lower()!=a.category.lower(): continue
        if a.severity and p['severity'].lower()!=a.severity.lower(): continue
        h=hay(p)
        if q and not all(token_matches(t,h) for t in q.split()): continue
        out.append(p)
    out=out[:max(0,a.limit)]
    if a.format=='json': print(json.dumps(out,indent=2,ensure_ascii=False)); return
    if not out: print('No patterns matched.'); return
    for p in out: print(f"{p['id']} [{p['severity']}] {p['title']} ({p['category']})"); print(f"  {p['summary']}"); print(f"  Fix: {p['remediation']}")
if __name__=='__main__': main()
