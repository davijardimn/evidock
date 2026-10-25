#!/usr/bin/env python3
"""Recompute RepoReel category and launch scores from criterion states. Standard library only."""
from __future__ import annotations
import argparse, json
from pathlib import Path
MAXIMA={'discovery':20,'demonstration':20,'quick_start':20,'documentation':15,'trust':15,'polish':10}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--audit',required=True); ap.add_argument('--output'); a=ap.parse_args(); p=Path(a.audit); d=json.loads(p.read_text(encoding='utf-8')); sums={k:0 for k in MAXIMA}
    for c in d.get('criteria',[]):
        maxp=int(c.get('max_points',0)); pts=maxp if c.get('status')=='PASS' else 0; c['points']=pts; cat=c.get('category');
        if cat in sums: sums[cat]+=pts
    d['categories']={k:{'score':sums[k],'max':MAXIMA[k]} for k in MAXIMA}; d['launch_score']=sum(sums.values()); out=Path(a.output) if a.output else p; out.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8'); print(f"RepoReel score computed: {d['launch_score']}/100 -> {out}")
if __name__=='__main__': main()
