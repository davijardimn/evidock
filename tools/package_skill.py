#!/usr/bin/env python3
"""Package skills/evidock as dist/evidock.zip for Claude.ai/Desktop skill upload."""
import os,zipfile
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); SKILL=os.path.join(ROOT,'skills','evidock'); DIST=os.path.join(ROOT,'dist'); SKIP={'__pycache__','.DS_Store'}
def main():
    os.makedirs(DIST,exist_ok=True); out=os.path.join(DIST,'evidock.zip')
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
        for base,dirs,files in os.walk(SKILL):
            dirs[:]=[d for d in dirs if d not in SKIP]
            for fn in files:
                if fn in SKIP or fn.endswith('.pyc'): continue
                full=os.path.join(base,fn); z.write(full,os.path.join('evidock',os.path.relpath(full,SKILL)))
    print(f'{out}  {os.path.getsize(out)/1e6:.2f} MB')
if __name__=='__main__': main()
