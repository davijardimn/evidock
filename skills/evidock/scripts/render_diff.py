#!/usr/bin/env python3
"""Render Evidock BEFORE → AFTER SVG using stable rubric v0.6."""
from __future__ import annotations
import argparse,json,subprocess,sys
from html import escape
from pathlib import Path
MAXIMA={"discovery":20,"demonstration":20,"quick_start":20,"documentation":15,"trust":15,"polish":10}; LABELS={"discovery":"Discovery","demonstration":"Demonstration","quick_start":"Quick Start","documentation":"Documentation","trust":"Trust","polish":"Polish"}; ACCENTS={"READY":"#B8FF5A","CAUTION":"#FFCE5C","BLOCKED":"#FF6B6B","UNKNOWN":"#94A3B8"}
def valid(p):
    r=subprocess.run([sys.executable,str(Path(__file__).with_name('validate_audit.py')),'--audit',str(p)],capture_output=True,text=True)
    if r.returncode: raise SystemExit(r.stderr.strip() or r.stdout.strip())
def t(x,y,text,size=18,weight=400,fill='#F4F4F5',anchor='start',letter=0): return f'<text x="{x}" y="{y}" font-family="ui-sans-serif,system-ui,-apple-system,Segoe UI,sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{letter}">{escape(str(text))}</text>'
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--before',required=True); ap.add_argument('--after',required=True); ap.add_argument('--output',required=True); a=ap.parse_args(); valid(a.before); valid(a.after); b=json.loads(Path(a.before).read_text(encoding='utf-8')); n=json.loads(Path(a.after).read_text(encoding='utf-8'))
    if b['rubric_version']!=n['rubric_version']: raise SystemExit('rubric versions differ')
    project=n.get('project') or b.get('project') or 'Untitled project'; bs=int(b['launch_score']); ns=int(n['launch_score']); delta=ns-bs; W,H=1200,675
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Evidock before after Launch Score for {escape(project)}">','<rect width="1200" height="675" rx="34" fill="#09090B"/>','<rect x="1" y="1" width="1198" height="673" rx="33" fill="none" stroke="#27272A" stroke-width="2"/>',t(68,68,'EVIDOCK',18,800,'#F4F4F5',letter=2.5),t(1132,68,'BEFORE / AFTER',14,800,'#71717A',anchor='end',letter=1.6),t(68,120,project,34,750),t(68,224,f'{bs:02d}',82,800,ACCENTS[b['launch_status']]),t(177,224,'>',42,700,'#52525B'),t(242,224,f'{ns:02d}',82,800,ACCENTS[n['launch_status']]),t(355,220,f'{delta:+d}',22,800,'#B8FF5A' if delta>=0 else '#FF6B6B'),t(68,260,b['launch_status'],14,800,ACCENTS[b['launch_status']],letter=1),t(242,260,n['launch_status'],14,800,ACCENTS[n['launch_status']],letter=1)]
    y0=335
    for i,k in enumerate(MAXIMA):
        y=y0+i*43; bv=int(b['categories'][k]['score']); nv=int(n['categories'][k]['score']); ch=nv-bv; out += [t(68,y,LABELS[k],16,650,'#D4D4D8'),t(520,y,f'{bv}/{MAXIMA[k]}',15,700,'#71717A',anchor='end'),t(590,y,'>',15,700,'#52525B',anchor='middle'),t(660,y,f'{nv}/{MAXIMA[k]}',15,750,'#F4F4F5',anchor='end'),t(750,y,f'{ch:+d}',14,800,'#B8FF5A' if ch>0 else ('#FF6B6B' if ch<0 else '#71717A'),anchor='end')]; bw=320; fill=round(bw*nv/MAXIMA[k]); out += [f'<rect x="790" y="{y-11}" width="{bw}" height="8" rx="4" fill="#27272A"/>',f'<rect x="790" y="{y-11}" width="{fill}" height="8" rx="4" fill="{ACCENTS[n["launch_status"]]}"/>']
    out += ['<line x1="68" y1="606" x2="1132" y2="606" stroke="#27272A"/>',t(68,642,'Launch Score measures launch readiness, not code quality.',14,600,'#71717A'),t(1132,642,'evidock · rubric v0.6',14,650,'#71717A',anchor='end'),'</svg>']; p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text('\n'.join(out)+'\n',encoding='utf-8'); print(p)
if __name__=='__main__': main()
