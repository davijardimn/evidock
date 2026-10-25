#!/usr/bin/env python3
"""Render a RepoReel v0.6 Launch Score SVG. Standard library only."""
from __future__ import annotations
import argparse,json,textwrap,subprocess,sys
from html import escape
from pathlib import Path
MAXIMA={"discovery":20,"demonstration":20,"quick_start":20,"documentation":15,"trust":15,"polish":10}
LABELS={"discovery":"Discovery","demonstration":"Demonstration","quick_start":"Quick Start","documentation":"Documentation","trust":"Trust","polish":"Polish"}
ACCENTS={"READY":"#B8FF5A","CAUTION":"#FFCE5C","BLOCKED":"#FF6B6B","UNKNOWN":"#94A3B8"}
def validate(path):
    script=Path(__file__).with_name('validate_audit.py'); r=subprocess.run([sys.executable,str(script),'--audit',str(path)],capture_output=True,text=True)
    if r.returncode: raise SystemExit(r.stderr.strip() or r.stdout.strip())
def t(x,y,text,size=18,weight=400,fill="#F4F4F5",anchor="start",letter=0): return f'<text x="{x}" y="{y}" font-family="ui-sans-serif,system-ui,-apple-system,Segoe UI,sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{letter}">{escape(str(text))}</text>'
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--audit',required=True); ap.add_argument('--output',required=True); a=ap.parse_args(); validate(a.audit)
    d=json.loads(Path(a.audit).read_text(encoding='utf-8')); status=d['launch_status']; accent=ACCENTS[status]; score=int(d['launch_score']); project=d.get('project') or 'Untitled project'; provisional=bool(d.get('provisional')); breaker=(d.get('reel_breaker') or 'No Reel Breaker recorded.').strip(); blockers=d.get('blockers') or []; claims=d.get('claims') or []; proofs=d.get('proof_runs') or []
    W,H=1200,675; x0=68; out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="RepoReel Launch Score for {escape(project)}">','<rect width="1200" height="675" rx="34" fill="#09090B"/>','<rect x="1" y="1" width="1198" height="673" rx="33" fill="none" stroke="#27272A" stroke-width="2"/>',t(x0,70,'REPOREEL',18,800,'#F4F4F5',letter=2.5),t(1130,70,'LAUNCH READINESS',14,700,'#71717A',anchor='end',letter=1.6),t(x0,126,project,34,750),t(x0,188,f'{score:02d}',82,800,accent),t(166,188,'/ 100',24,650,'#71717A'),f'<rect x="{x0}" y="214" width="156" height="36" rx="18" fill="{accent}" fill-opacity="0.12" stroke="{accent}" stroke-opacity="0.55"/>',t(x0+78,238,status,15,800,accent,anchor='middle',letter=1.2)]
    if provisional: out += [f'<rect x="238" y="214" width="140" height="36" rx="18" fill="#18181B" stroke="#3F3F46"/>',t(308,238,'PROVISIONAL',13,750,'#A1A1AA',anchor='middle',letter=1)]
    bx=470; by=133; bw=610; row=57
    for i,k in enumerate(MAXIMA):
        y=by+i*row; s=int(d['categories'][k]['score']); m=MAXIMA[k]; fillw=round(bw*s/m); out += [t(bx,y,LABELS[k],16,650,'#D4D4D8'),t(bx+bw,y,f'{s}/{m}',15,700,'#A1A1AA',anchor='end'),f'<rect x="{bx}" y="{y+15}" width="{bw}" height="9" rx="4.5" fill="#27272A"/>',f'<rect x="{bx}" y="{y+15}" width="{fillw}" height="9" rx="4.5" fill="{accent}"/>']
    out += ['<line x1="68" y1="390" x2="1132" y2="390" stroke="#27272A"/>',t(x0,432,'THE REEL BREAKER',13,800,'#71717A',letter=1.8)]
    lines=[]
    for part in breaker.splitlines() or [breaker]: lines += textwrap.wrap(part,width=80) or ['']
    for i,line in enumerate(lines[:3]): out.append(t(x0,472+i*31,line,23,650,'#F4F4F5'))
    verified=sum(1 for c in claims if c.get('status')=='VERIFIED'); contradicted=sum(1 for c in claims if c.get('status')=='CONTRADICTED')
    bc=len(blockers); pc=len(proofs); out += [t(x0,589,f'{bc} blocker' + ('' if bc==1 else 's'),13,700,'#A1A1AA'),t(180,589,f'{verified} verified claim' + ('' if verified==1 else 's'),13,700,'#A1A1AA'),t(330,589,f'{contradicted} contradicted',13,700,'#A1A1AA'),t(470,589,f'{pc} proof run' + ('' if pc==1 else 's'),13,700,'#A1A1AA'),t(x0,635,'Market the evidence. Never manufacture it.',14,600,'#71717A'),t(1132,635,'reporeel · rubric v0.6',14,650,'#71717A',anchor='end'),'</svg>']
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text('\n'.join(out)+'\n',encoding='utf-8'); print(p)
if __name__=='__main__': main()
