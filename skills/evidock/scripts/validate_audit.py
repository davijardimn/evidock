#!/usr/bin/env python3
"""Validate Evidock audit JSON using stable rubric/schema v0.6. Standard library only."""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
MAXIMA={"discovery":20,"demonstration":20,"quick_start":20,"documentation":15,"trust":15,"polish":10}
CRITERIA={"discovery.purpose":("discovery",5),"discovery.user":("discovery",4),"discovery.value":("discovery",5),"discovery.differentiation":("discovery",4),"discovery.identity":("discovery",2),"demonstration.proof":("demonstration",5),"demonstration.core":("demonstration",5),"demonstration.reachability":("demonstration",5),"demonstration.credibility":("demonstration",5),"quick_start.prerequisites":("quick_start",5),"quick_start.install":("quick_start",5),"quick_start.first_use":("quick_start",5),"quick_start.short_path":("quick_start",5),"documentation.core_usage":("documentation",5),"documentation.behavior":("documentation",5),"documentation.navigation":("documentation",5),"trust.license":("trust",3),"trust.verification":("trust",3),"trust.process":("trust",3),"trust.claims":("trust",3),"trust.support":("trust",3),"polish.no_noise":("polish",2),"polish.primary_files_intentional":("polish",2),"polish.front_door_refs":("polish",2),"polish.naming":("polish",2),"polish.first_impression":("polish",2)}
STATUSES={"PASS","FAIL","N_A","UNKNOWN"}; LAUNCH={"READY","CAUTION","BLOCKED","UNKNOWN"}; CLAIM_STATUSES={"VERIFIED","INFERRED","UNKNOWN","CONTRADICTED"}; PROOF_RESULTS={"PASS","FAIL","INCONCLUSIVE","SKIPPED"}; BLOCKER_SEVERITIES={"CRITICAL","HIGH","MEDIUM","LOW"}
def validate(d):
    errors=[]
    if str(d.get('schema_version'))!='0.6': errors.append('schema_version must be 0.6')
    if str(d.get('rubric_version'))!='0.6': errors.append('rubric_version must be 0.6')
    if d.get('launch_status') not in LAUNCH: errors.append('invalid launch_status')
    if not isinstance(d.get('provisional'),bool): errors.append('provisional must be boolean')
    cats=d.get('categories') or {}
    for k,m in MAXIMA.items():
        c=cats.get(k)
        if not isinstance(c,dict): errors.append(f'missing category {k}'); continue
        try: s=int(c.get('score')); mx=int(c.get('max'))
        except Exception: errors.append(f'invalid category numeric values: {k}'); continue
        if mx!=m: errors.append(f'{k}.max must be {m}')
        if not 0<=s<=m: errors.append(f'{k}.score out of range')
    items=d.get('criteria'); items=[] if not isinstance(items,list) else items
    if not isinstance(d.get('criteria'),list): errors.append('criteria must be a list')
    seen={}; category_sums={k:0 for k in MAXIMA}
    for i,c in enumerate(items):
        if not isinstance(c,dict): errors.append(f'criteria[{i}] not object'); continue
        cid=c.get('id')
        if cid not in CRITERIA: errors.append(f'unknown criterion id: {cid}'); continue
        if cid in seen: errors.append(f'duplicate criterion id: {cid}')
        seen[cid]=1; cat,maxp=CRITERIA[cid]
        if c.get('category')!=cat: errors.append(f'{cid}: category must be {cat}')
        if c.get('status') not in STATUSES: errors.append(f'{cid}: invalid status')
        try: pts=int(c.get('points')); mp=int(c.get('max_points'))
        except Exception: errors.append(f'{cid}: points/max_points must be integers'); continue
        if mp!=maxp: errors.append(f'{cid}: max_points must be {maxp}')
        if c.get('status')=='PASS':
            if pts!=maxp: errors.append(f'{cid}: PASS must award full {maxp}')
        elif pts!=0: errors.append(f'{cid}: non-PASS must award 0')
        if not str(c.get('evidence') or '').strip(): errors.append(f'{cid}: evidence is required')
        category_sums[cat]+=pts
    missing=sorted(set(CRITERIA)-set(seen))
    if missing: errors.append('missing criteria: '+', '.join(missing))
    for cat,s in category_sums.items():
        if cat in cats and int(cats[cat].get('score',-999))!=s: errors.append(f'{cat}: category score mismatch')
    total=sum(category_sums.values())
    try: launch_score=int(d.get('launch_score'))
    except Exception: launch_score=-1; errors.append('launch_score must be integer')
    if launch_score!=total: errors.append(f'launch_score {launch_score} != criterion sum {total}')
    blockers=d.get('blockers') or []
    if not isinstance(blockers,list): errors.append('blockers must be a list'); blockers=[]
    for i,b in enumerate(blockers):
        if not isinstance(b,dict): errors.append(f'blockers[{i}] not object'); continue
        if b.get('severity') not in BLOCKER_SEVERITIES: errors.append(f'blockers[{i}]: invalid severity')
        if not str(b.get('title') or '').strip(): errors.append(f'blockers[{i}]: title is required')
        if not str(b.get('evidence') or '').strip(): errors.append(f'blockers[{i}]: evidence is required')
    claims=d.get('claims') or []; claim_ids=set()
    if not isinstance(claims,list): errors.append('claims must be a list'); claims=[]
    for i,c in enumerate(claims):
        if not isinstance(c,dict): errors.append(f'claims[{i}] not object'); continue
        cid=str(c.get('id') or '').strip()
        if not cid: errors.append(f'claims[{i}]: id is required')
        elif cid in claim_ids: errors.append(f'duplicate claim id: {cid}')
        else: claim_ids.add(cid)
        if c.get('status') not in CLAIM_STATUSES: errors.append(f'claims[{i}]: invalid status')
        if not str(c.get('claim') or '').strip(): errors.append(f'claims[{i}]: claim text is required')
    proofs=d.get('proof_runs') or []; proof_ids=set()
    if not isinstance(proofs,list): errors.append('proof_runs must be a list'); proofs=[]
    for i,p in enumerate(proofs):
        if not isinstance(p,dict): errors.append(f'proof_runs[{i}] not object'); continue
        pid=str(p.get('id') or '').strip()
        if not pid: errors.append(f'proof_runs[{i}]: id is required')
        elif pid in proof_ids: errors.append(f'duplicate proof id: {pid}')
        else: proof_ids.add(pid)
        if p.get('result') not in PROOF_RESULTS: errors.append(f'proof_runs[{i}]: invalid result')
        if not str(p.get('scope') or '').strip(): errors.append(f'proof_runs[{i}]: scope is required')
        if not str(p.get('action') or '').strip(): errors.append(f'proof_runs[{i}]: action is required')
        claim_id=p.get('claim_id')
        if claim_id is not None and str(claim_id).strip() and str(claim_id) not in claim_ids: errors.append(f'proof_runs[{i}]: unknown claim_id {claim_id}')
    if d.get('provisional') and not str(d.get('provisional_reason') or '').strip(): errors.append('provisional_reason is required when provisional is true')
    return errors
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--audit',required=True); a=ap.parse_args(); p=Path(a.audit); d=json.loads(p.read_text(encoding='utf-8')); errors=validate(d)
    if errors:
        for e in errors: print('ERROR:',e,file=sys.stderr)
        raise SystemExit(2)
    print(f'VALID Evidock audit v0.6: {p} · Launch Score {d["launch_score"]}/100 · {d["launch_status"]}')
if __name__=='__main__': main()
