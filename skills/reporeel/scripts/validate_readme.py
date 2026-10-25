#!/usr/bin/env python3
"""Lightweight Front Door checks for RepoReel. Standard library only."""
import argparse,json,re
from pathlib import Path
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--json',action='store_true'); a=ap.parse_args(); root=Path(a.root); candidates=[root/'README.md',root/'README',root/'readme.md']; p=next((x for x in candidates if x.exists()),None)
    if not p: result={'found':False,'checks':{},'warnings':['README not found']}
    else:
        t=p.read_text(encoding='utf-8',errors='replace'); lines=t.splitlines(); opening='\n'.join(lines[:80]); low=t.lower(); op=opening.lower(); checks={'has_title':bool(re.search(r'^#\s+\S+',t,re.M)),'opening_has_value_copy':len(re.findall(r'\b(for|para|turn|transform|audit|build|create|help|helps|use|users?|developer|repository|repo)\b',op,re.I))>=2,'has_quick_start_or_install':bool(re.search(r'quick\s*start|getting started|install|instala|como usar|usage',low)),'has_code_example':'```' in t,'has_visual_or_output_proof':bool(re.search(r'!\[[^\]]*\]\([^\)]+\)|<img\b|\.gif\b|\.mp4\b|example output|sample output',t,re.I)),'has_license_section':bool(re.search(r'^#{1,4}\s+.*licen[cs]e|^#{1,4}\s+licen[çc]a',t,re.I|re.M)),'opening_has_next_step':bool(re.search(r'install|quick\s*start|try|demo|usage|use repo|upload|claude',op,re.I))}; result={'found':True,'path':str(p),'line_count':len(lines),'checks':checks,'warnings':[]}
    print(json.dumps(result,indent=2,ensure_ascii=False) if a.json else '\n'.join(f'{k}: {v}' for k,v in result.get('checks',{}).items()))
if __name__=='__main__': main()
