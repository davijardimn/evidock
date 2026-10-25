#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os,re,subprocess
from pathlib import Path
from datetime import datetime,timezone
SKIP={'.git','node_modules','.next','dist','build','target','vendor','.venv','venv','__pycache__','.evidock','.pytest_cache','.mypy_cache','.ruff_cache'}
NOISE={'.venv','venv','node_modules','__pycache__','.pytest_cache','.mypy_cache','.ruff_cache','.DS_Store','Thumbs.db','.idea','.vscode'}
MANIFESTS=['package.json','pyproject.toml','requirements.txt','Cargo.toml','go.mod','pom.xml','build.gradle','build.gradle.kts','pubspec.yaml','composer.json','Gemfile']; LOCKS=['package-lock.json','pnpm-lock.yaml','yarn.lock','bun.lockb','uv.lock','poetry.lock','Cargo.lock','go.sum','pubspec.lock','composer.lock','Gemfile.lock']; ASSET_EXT={'.png','.jpg','.jpeg','.gif','.webp','.svg','.mp4','.webm'}; MD_LINK=re.compile(r'!?(?:\[[^\]]*\])\(([^)]+)\)'); HEAD_RE=re.compile(r'^(#{1,6})\s+(.+?)\s*#*\s*$',re.M)
def rel(p,r): return str(p.relative_to(r)).replace(os.sep,'/')
def walk(r):
    for b,d,f in os.walk(r):
        d[:]=[x for x in d if x not in SKIP]
        for n in f: yield Path(b)/n
def git(r,*a):
    try:
        x=subprocess.run(['git','-C',str(r),*a],capture_output=True,text=True,timeout=3); return x.stdout.strip() if x.returncode==0 else None
    except Exception: return None
def slug(s):
    s=re.sub(r'[`*_~]','',s).strip().lower(); s=re.sub(r'[^\w\- ]','',s,flags=re.UNICODE); return re.sub(r'[\s\-]+','-',s).strip('-')
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--output',default='.evidock/evidence.json'); a=ap.parse_args(); root=Path(a.root).resolve(); files=list(walk(root)); paths={rel(p,root):p for p in files}; readmes=sorted([x for x in paths if Path(x).name.lower().startswith('readme')]); licenses=sorted([x for x in paths if Path(x).name.lower() in {'license','license.md','license.txt','copying'}]); ci=sorted([x for x in paths if x.startswith('.github/workflows/')]); support=sorted([x for x in paths if Path(x).name.lower() in {'contributing.md','security.md','support.md','code_of_conduct.md','changelog.md'}]); assets=sorted([x for x in paths if Path(x).suffix.lower() in ASSET_EXT])[:300]; tests=sorted([x for x in paths if 'test' in x.lower() or 'spec' in x.lower()]); manifests=[x for x in MANIFESTS if x in paths]; locks=[x for x in LOCKS if x in paths]; root_noise=sorted([p.name+('/' if p.is_dir() else '') for p in root.iterdir() if p.name in NOISE]); empty=sorted([x for x,p in paths.items() if p.stat().st_size==0])[:300]; ri=[]; broken=[]
    for item in readmes[:5]:
        p=root/item; text=p.read_text(encoding='utf-8',errors='replace'); heads=[{'level':len(m.group(1)),'text':m.group(2).strip(),'anchor':slug(m.group(2))} for m in HEAD_RE.finditer(text)]; anchors={h['anchor'] for h in heads}; refs=[]
        for raw in MD_LINK.findall(text):
            t=raw.strip().split()[0].strip('<>')
            if not t or t.startswith(('http://','https://','mailto:','data:')): continue
            if t.startswith('#'): ok=t[1:] in anchors; rec={'from':item,'target':t,'kind':'anchor','exists':ok}
            else:
                fp,_,an=t.partition('#'); c=(p.parent/fp.split('?',1)[0]).resolve()
                try: c.relative_to(root); outside=False
                except ValueError: outside=True
                ok=(not outside and c.exists()); rec={'from':item,'target':t,'kind':'local','exists':ok,'outside_root':outside}
            refs.append(rec)
            if not rec['exists']: broken.append(rec)
        ri.append({'path':item,'size':p.stat().st_size,'opening_excerpt':'\n'.join(text.splitlines()[:80])[:7000],'headings':heads[:50],'local_references':refs[:300]})
    ev={'schema_version':'0.6','generated_at':datetime.now(timezone.utc).isoformat(),'root':str(root),'repository':{'file_count':len(files),'manifests':manifests,'lockfiles':locks,'readmes':readmes,'licenses':licenses,'ci':ci,'support_files':support,'test_files_count':len(tests),'test_files_sample':tests[:40],'assets':assets,'root_noise':root_noise,'empty_files':empty,'readme':ri,'broken_front_door_references':broken},'git':{'branch':git(root,'branch','--show-current'),'head':git(root,'rev-parse','--short','HEAD'),'remote':git(root,'remote','get-url','origin'),'last_commit':git(root,'log','-1','--format=%cI')},'notes':['Static evidence only. Runtime success is not implied. Generated/environment contents are skipped, but their presence at root is reported.']}; out=(root/a.output).resolve() if not Path(a.output).is_absolute() else Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(ev,indent=2,ensure_ascii=False)+'\n',encoding='utf-8'); print(f'Evidock evidence written to {out}')
if __name__=='__main__': main()
