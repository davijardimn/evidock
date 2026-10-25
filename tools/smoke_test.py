#!/usr/bin/env python3
"""End-to-end smoke test of Evidock's agent-facing scripts. Standard library only."""
from __future__ import annotations
import shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent; SKILL=ROOT/'skills'/'evidock'; S=SKILL/'scripts'; failures=[]
def run(name,args,expect=(),cwd=None):
    p=subprocess.run([sys.executable]+[str(x) for x in args],cwd=str(cwd or ROOT),capture_output=True); out=(p.stdout+p.stderr).decode('utf-8','replace'); probs=[]
    if p.returncode: probs.append(f'exit={p.returncode}')
    if 'Traceback (most recent call last)' in out: probs.append('traceback')
    for e in expect:
        if isinstance(e,Path):
            if not e.exists(): probs.append(f'missing {e}')
        elif str(e) not in out: probs.append(f'output lacks {e!r}')
    print(f"[{'ok  ' if not probs else 'FAIL'}] {name}")
    if probs: failures.append(name); print('       '+'; '.join(probs)); print(out[-1800:])
    return out
def main():
    tmp=Path(tempfile.mkdtemp(prefix='evidock-smoke-'))
    try:
        repo=tmp/'fixture'; repo.mkdir(); (repo/'README.md').write_text('# TinyRepo\n\nTiny CLI for demo users.\n\n## Quick start\n\n```bash\npython app.py\n```\n'); (repo/'app.py').write_text("print('hello')\n"); (repo/'LICENSE').write_text('MIT\n')
        evidence=tmp/'evidence.json'; run('inspect_repo',[S/'inspect_repo.py','--root',repo,'--output',evidence],[evidence]); run('inspect_github_parse',[S/'inspect_github.py','--repo','https://github.com/octocat/Hello-World/tree/master','--parse-only'],['octocat','Hello-World']); run('search_patterns',[S/'search_patterns.py','--query','missing readme'],['front-door-void'])
        before=ROOT/'examples'/'before.audit.json'; after=ROOT/'examples'/'after.audit.json'; scored=tmp/'scored.json'; shutil.copy(before,scored); run('score_audit',[S/'score_audit.py','--audit',scored],['Evidock score computed']); run('validate_audit',[S/'validate_audit.py','--audit',before],['VALID Evidock audit']); card=tmp/'card.svg'; report=tmp/'report.html'; diff=tmp/'diff.svg'; badge=tmp/'badge.svg'; badge_md=tmp/'badge.md'; run('render_card',[S/'render_card.py','--audit',before,'--output',card],[card]); run('render_report',[S/'render_report.py','--audit',before,'--output',report],[report]); run('render_diff',[S/'render_diff.py','--before',before,'--after',after,'--output',diff],[diff]); run('render_badge',[S/'render_badge.py','--audit',after,'--output',badge,'--markdown-output',badge_md],[badge,badge_md,'Evidock Launch Score']); run('verify_artifacts',[S/'verify_artifacts.py','--audit',before,'--card',card,'--report',report],['VALID Evidock artifacts']); run('lint_evals',[ROOT/'tools'/'lint_evals.py'],['VALID eval suite']); run('package_skill',[ROOT/'tools'/'package_skill.py'],[ROOT/'dist'/'evidock.zip'])
    finally: shutil.rmtree(tmp,ignore_errors=True)
    caches=[p for p in SKILL.rglob('__pycache__')]; print(f"[{'ok  ' if not caches else 'FAIL'}] no __pycache__ in skill")
    if caches: failures.append('cache pollution')
    if failures: print(f"{len(failures)} failure(s): {', '.join(failures)}"); sys.exit(1)
    print('all checks passed')
if __name__=='__main__': sys.dont_write_bytecode=True; main()
