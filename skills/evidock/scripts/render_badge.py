#!/usr/bin/env python3
"""Render a small Evidock Launch Score badge from validated audit.json."""
from __future__ import annotations
import argparse,json,subprocess,sys
from html import escape
from pathlib import Path
ACCENTS={"READY":"#79D45E","CAUTION":"#D9A441","BLOCKED":"#E05D5D","UNKNOWN":"#64748B"}
DEFAULT_TARGET="https://github.com/davijardimn/evidock"
def validate(path:Path)->None:
    script=Path(__file__).with_name("validate_audit.py"); p=subprocess.run([sys.executable,str(script),"--audit",str(path)],capture_output=True,text=True)
    if p.returncode: raise SystemExit(p.stderr.strip() or p.stdout.strip())
def text_width(text:str,char_px:float=7.1,padding:int=20)->int: return max(42,int(round(len(text)*char_px+padding)))
def segment(x:int,width:int,fill:str,text:str,fg:str="#F8FAFC")->str:
    tx=x+width/2; return f'<rect x="{x}" y="0" width="{width}" height="28" fill="{fill}"/><text x="{tx:.1f}" y="18.5" text-anchor="middle" font-family="Verdana,DejaVu Sans,sans-serif" font-size="11" font-weight="600" fill="{fg}">{escape(text)}</text>'
def main()->None:
    ap=argparse.ArgumentParser(description="Render an Evidock badge from a validated audit."); ap.add_argument("--audit",required=True); ap.add_argument("--output",required=True); ap.add_argument("--markdown-output"); ap.add_argument("--asset-path",default=".evidock/badge.svg"); ap.add_argument("--target-url",default=DEFAULT_TARGET); args=ap.parse_args()
    audit=Path(args.audit); validate(audit); d=json.loads(audit.read_text(encoding="utf-8")); score=int(d["launch_score"]); status=d["launch_status"]; provisional=bool(d.get("provisional")); right=f"{score}/100 · {status}"+(" · PROVISIONAL" if provisional else ""); left="Evidock"; lw=text_width(left,padding=24); rw=text_width(right,padding=28); total=lw+rw; accent=ACCENTS[status]; label=f"Evidock Launch Score {score}/100 {status}"+(" provisional" if provisional else "")
    svg="\n".join([f'<svg xmlns="http://www.w3.org/2000/svg" width="{total}" height="28" viewBox="0 0 {total} 28" role="img" aria-label="{escape(label)}">',f'<title>{escape(label)}</title>','<clipPath id="r"><rect width="100%" height="28" rx="6"/></clipPath>','<g clip-path="url(#r)">',segment(0,lw,"#18181B",left),segment(lw,rw,accent,right,"#0A0A0C" if status in {"READY","CAUTION"} else "#FFFFFF"),'</g>',f'<rect x="0.5" y="0.5" width="{total-1}" height="27" rx="5.5" fill="none" stroke="#000" stroke-opacity="0.12"/>','</svg>','']); out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(svg,encoding="utf-8"); markdown=f"[![{label}]({args.asset_path})]({args.target_url})"
    if args.markdown_output:
        md=Path(args.markdown_output); md.parent.mkdir(parents=True,exist_ok=True); md.write_text(markdown+"\n",encoding="utf-8")
    print(out); print(markdown)
if __name__=="__main__": main()
