#!/usr/bin/env python3
"""Verify RepoReel output artifacts without requiring a GUI or rasterizer."""
from __future__ import annotations
import argparse,json,subprocess,sys,xml.etree.ElementTree as ET
from pathlib import Path
def fail(msg): print('ERROR:',msg,file=sys.stderr); raise SystemExit(2)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--audit',required=True); ap.add_argument('--card'); ap.add_argument('--report'); ap.add_argument('--diff'); a=ap.parse_args(); audit=Path(a.audit); validator=Path(__file__).with_name('validate_audit.py'); r=subprocess.run([sys.executable,str(validator),'--audit',str(audit)],capture_output=True,text=True)
    if r.returncode: fail(r.stderr.strip() or r.stdout.strip())
    d=json.loads(audit.read_text(encoding='utf-8')); checked=['audit.json']
    if a.card:
        p=Path(a.card)
        if not p.is_file() or p.stat().st_size<200: fail('card.svg missing or unexpectedly small')
        try: root=ET.parse(p).getroot()
        except Exception as e: fail(f'card.svg is not valid XML: {e}')
        if not root.tag.endswith('svg'): fail('card file root is not <svg>')
        text=p.read_text(encoding='utf-8')
        if str(d['launch_score']).zfill(2) not in text or d['launch_status'] not in text: fail('card.svg does not contain the audit score/status')
        checked.append('card.svg')
    if a.diff:
        p=Path(a.diff)
        if not p.is_file() or p.stat().st_size<200: fail('diff.svg missing or unexpectedly small')
        try: root=ET.parse(p).getroot()
        except Exception as e: fail(f'diff.svg is not valid XML: {e}')
        if not root.tag.endswith('svg'): fail('diff file root is not <svg>')
        checked.append('diff.svg')
    if a.report:
        p=Path(a.report)
        if not p.is_file() or p.stat().st_size<500: fail('report.html missing or unexpectedly small')
        text=p.read_text(encoding='utf-8')
        for marker in ['REPOREEL','THE REEL BREAKER','SCORECARD','CLAIM VERIFICATION','PROOF MODE','CRITERIA']:
            if marker not in text: fail(f'report.html missing section: {marker}')
        if f'>{int(d["launch_score"]):02d}<' not in text or d['launch_status'] not in text: fail('report.html does not contain the audit score/status')
        for proof in d.get('proof_runs') or []:
            if proof.get('id') and proof['id'] not in text: fail(f'report.html missing proof run {proof["id"]}')
        checked.append('report.html')
    print('VALID RepoReel artifacts: '+', '.join(checked)); print('Note: structural validation does not claim human visual inspection.')
if __name__=='__main__': main()
