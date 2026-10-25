#!/usr/bin/env python3
'''Render a standalone RepoReel v0.6 HTML report from validated audit.json.'''
from __future__ import annotations
import argparse,json,subprocess,sys
from html import escape
from pathlib import Path

LABELS={'discovery':'Discovery','demonstration':'Demonstration','quick_start':'Quick Start','documentation':'Documentation','trust':'Trust','polish':'Polish'}
COLOR={'READY':'#b8ff5a','CAUTION':'#ffce5c','BLOCKED':'#ff6b6b','UNKNOWN':'#94a3b8'}
RESULT_COLOR={'PASS':'#b8ff5a','FAIL':'#ff6b6b','INCONCLUSIVE':'#ffce5c','SKIPPED':'#94a3b8'}

def _items(values):
    return ''.join(f'<li>{escape(str(v))}</li>' for v in (values or [])) or '<li>None recorded.</li>'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--audit',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    vr=subprocess.run([sys.executable,str(Path(__file__).with_name('validate_audit.py')),'--audit',a.audit],capture_output=True,text=True)
    if vr.returncode: raise SystemExit(vr.stderr.strip() or vr.stdout.strip())
    d=json.loads(Path(a.audit).read_text(encoding='utf-8')); accent=COLOR[d['launch_status']]
    cats=''.join(f'<div class="row"><span>{escape(LABELS[k])}</span><div class="bar"><i style="width:{100*v["score"]/v["max"]:.0f}%"></i></div><b>{v["score"]}/{v["max"]}</b></div>' for k,v in d['categories'].items())
    crit=''.join(f'<tr><td><code>{escape(c["id"])}</code></td><td><span class="pill">{escape(c["status"])}</span></td><td>{c["points"]}/{c["max_points"]}</td><td>{escape(c["evidence"])}</td></tr>' for c in d['criteria'])
    blockers=''.join(f'<li><b>{escape(x.get("severity",""))}</b> · {escape(x.get("title",""))}<small>{escape(x.get("evidence", ""))}</small></li>' for x in (d.get('blockers') or [])) or '<li>None recorded.</li>'
    claim_chunks=[]
    for x in d.get('claims') or []:
        claim_chunks.append(f'<article class="claim"><h3><span class="pill">{escape(x.get("status",""))}</span> {escape(x.get("claim",""))}</h3><div class="twocol"><div><h4>Evidence</h4><ul>{_items(x.get("evidence"))}</ul></div><div><h4>Conflicts</h4><ul>{_items(x.get("conflicts"))}</ul></div></div></article>')
    claims=''.join(claim_chunks) or '<p>No consequential claims recorded.</p>'
    proof_chunks=[]
    for p in d.get('proof_runs') or []:
        result=p.get('result',''); rcolor=RESULT_COLOR.get(result,'#94a3b8')
        proof_chunks.append(f'<article class="proof"><div class="proofhead"><h3>{escape(p.get("id","Proof"))}</h3><span class="result" style="--r:{rcolor}">{escape(result)}</span></div><dl><dt>Claim</dt><dd><code>{escape(str(p.get("claim_id") or "unlinked"))}</code></dd><dt>Scope</dt><dd>{escape(p.get("scope", ""))}</dd><dt>Action</dt><dd>{escape(p.get("action", ""))}</dd></dl><div class="twocol"><div><h4>Observations</h4><ul>{_items(p.get("observations"))}</ul></div><div><h4>Limitations</h4><ul>{_items(p.get("limitations"))}</ul></div></div></article>')
    proofs=''.join(proof_chunks) or '<p>No runtime proof was run.</p>'
    scope=d.get('scope') or {}; provisional=' <span class="provisional">PROVISIONAL</span>' if d.get('provisional') else ''
    provisional_reason=f'<p class="muted"><b>Why provisional:</b> {escape(str(d["provisional_reason"]))}</p>' if d.get('provisional') and d.get('provisional_reason') else ''
    html=f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>RepoReel · {escape(d.get('project','Project'))}</title><style>:root{{--a:{accent}}}*{{box-sizing:border-box}}body{{margin:0;background:#09090b;color:#f4f4f5;font:15px/1.55 ui-sans-serif,system-ui,-apple-system,Segoe UI,sans-serif}}main{{max-width:1050px;margin:auto;padding:54px 28px 80px}}header,section{{border:1px solid #27272a;border-radius:22px;padding:26px;background:#0d0d10}}header{{border-radius:28px;padding:34px;background:#0f0f12}}section{{margin-top:28px}}.brand{{letter-spacing:.18em;font-weight:800;color:#a1a1aa}}h1{{font-size:38px;margin:12px 0 6px}}.score{{font-size:72px;font-weight:850;color:var(--a)}}.status{{color:var(--a);border:1px solid var(--a);border-radius:999px;padding:6px 12px;font-weight:800}}.provisional{{margin-left:8px;color:#a1a1aa;border:1px solid #3f3f46;border-radius:999px;padding:6px 12px;font-size:12px;font-weight:800}}h2{{font-size:14px;letter-spacing:.12em;color:#a1a1aa}}.row{{display:grid;grid-template-columns:150px 1fr 58px;gap:14px;align-items:center;margin:14px 0}}.bar{{height:9px;background:#27272a;border-radius:99px;overflow:hidden}}.bar i{{display:block;height:100%;background:var(--a)}}table{{width:100%;border-collapse:collapse}}th,td{{border-bottom:1px solid #27272a;padding:10px;text-align:left;vertical-align:top}}.pill{{font-size:12px;border:1px solid #3f3f46;border-radius:999px;padding:3px 7px}}small,.muted{{display:block;color:#a1a1aa}}.twocol{{display:grid;grid-template-columns:1fr 1fr;gap:24px}}.proofhead{{display:flex;justify-content:space-between}}.result{{color:var(--r);border:1px solid var(--r);border-radius:999px;padding:4px 9px;font-size:12px;font-weight:800}}footer{{color:#71717a;margin-top:30px}}</style></head><body><main><header><div class="brand">REPOREEL</div><h1>{escape(d.get('project','Untitled project'))}</h1><div><span class="score">{int(d['launch_score']):02d}</span> / 100 &nbsp; <span class="status">{escape(d['launch_status'])}</span>{provisional}</div><p>Launch Score measures repository launch readiness — not code quality.</p>{provisional_reason}</header><section><h2>SCOPE</h2><p>{escape(scope.get('summary',''))}</p><p><code>{escape(scope.get('kind',''))}</code> · <code>{escape(scope.get('completeness',''))}</code> · {escape(scope.get('execution',''))}</p></section><section><h2>THE REEL BREAKER</h2><h3>{escape(d.get('reel_breaker','No Reel Breaker recorded.'))}</h3></section><section><h2>SCORECARD</h2>{cats}</section><section><h2>LAUNCH BLOCKERS</h2><ul>{blockers}</ul></section><section><h2>CLAIM VERIFICATION</h2>{claims}</section><section><h2>PROOF MODE</h2>{proofs}</section><section><h2>CRITERIA</h2><table><tr><th>Criterion</th><th>Status</th><th>Points</th><th>Evidence</th></tr>{crit}</table></section><footer>Market the evidence. Never manufacture it. · RepoReel rubric v0.6</footer></main></body></html>'''
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(html,encoding='utf-8'); print(p)
if __name__=='__main__': main()
