import json,re,subprocess,sys,tempfile,unittest,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent; SKILL=ROOT/'skills'/'evidock'; S=SKILL/'scripts'; EX=ROOT/'examples'
class CoreContractTests(unittest.TestCase):
    def runv(self,p): return subprocess.run([sys.executable,str(S/'validate_audit.py'),'--audit',str(p)],capture_output=True,text=True)
    def test_skill_frontmatter(self):
        text=(SKILL/'SKILL.md').read_text(encoding='utf-8'); self.assertTrue(text.startswith('---\n')); fm=text.split('---',2)[1]; name=re.search(r'^name:\s*(.+)$',fm,re.M).group(1).strip(); desc=re.search(r'^description:\s*(.+)$',fm,re.M).group(1).strip(); self.assertEqual(name,'evidock'); self.assertRegex(name,r'^[a-z0-9-]+$'); self.assertLessEqual(len(desc),1024)
    def test_referenced_core_files_exist(self):
        for rel in ['references/front-door.md','references/proof-mode.md','references/audit-rubric.md','references/audit-schema.md','references/pattern-library.md','scripts/inspect_repo.py','scripts/search_patterns.py','scripts/score_audit.py','scripts/validate_audit.py','scripts/render_card.py','scripts/render_report.py','scripts/verify_artifacts.py','assets/patterns.json']: self.assertTrue((SKILL/rel).exists(),rel)
    def test_examples_validate(self): self.assertEqual(self.runv(EX/'before.audit.json').returncode,0); self.assertEqual(self.runv(EX/'after.audit.json').returncode,0)
    def test_na_cannot_get_points(self):
        d=json.loads((EX/'before.audit.json').read_text()); c=next(x for x in d['criteria'] if x['id']=='trust.claims'); c['status']='N_A'; c['points']=3; d['categories']['trust']['score']+=3; d['launch_score']+=3
        with tempfile.TemporaryDirectory() as td: p=Path(td)/'bad.json'; p.write_text(json.dumps(d)); self.assertNotEqual(self.runv(p).returncode,0)
    def test_missing_criterion_rejected(self):
        d=json.loads((EX/'before.audit.json').read_text()); d['criteria']=d['criteria'][:-1]
        with tempfile.TemporaryDirectory() as td: p=Path(td)/'bad.json'; p.write_text(json.dumps(d)); self.assertNotEqual(self.runv(p).returncode,0)
    def test_unknown_proof_claim_rejected(self):
        d=json.loads((EX/'self.audit.json').read_text()); d['proof_runs'][0]['claim_id']='claim-does-not-exist'
        with tempfile.TemporaryDirectory() as td: p=Path(td)/'bad.json'; p.write_text(json.dumps(d)); self.assertNotEqual(self.runv(p).returncode,0)
    def test_provisional_requires_reason(self):
        d=json.loads((EX/'before.audit.json').read_text()); d['provisional']=True; d['provisional_reason']=None
        with tempfile.TemporaryDirectory() as td: p=Path(td)/'bad.json'; p.write_text(json.dumps(d)); self.assertNotEqual(self.runv(p).returncode,0)
    def test_inspector_reports_noise_empty_broken_ref(self):
        with tempfile.TemporaryDirectory() as td:
            r=Path(td); (r/'.venv').mkdir(); (r/'README.md').write_text('# Demo\n\n![x](missing.png)\n[Local](docs.md)\n'); (r/'requirements.txt').write_text(''); out=r/'evidence.json'; p=subprocess.run([sys.executable,str(S/'inspect_repo.py'),'--root',str(r),'--output',str(out)],capture_output=True,text=True); self.assertEqual(p.returncode,0,p.stderr); d=json.loads(out.read_text()); self.assertIn('.venv/',d['repository']['root_noise']); self.assertIn('requirements.txt',d['repository']['empty_files']); self.assertGreaterEqual(len(d['repository']['broken_front_door_references']),2)
    def test_renderers(self):
        with tempfile.TemporaryDirectory() as td:
            td=Path(td); card=td/'card.svg'; diff=td/'diff.svg'; report=td/'report.html'
            for cmd in [[S/'render_card.py','--audit',EX/'before.audit.json','--output',card],[S/'render_diff.py','--before',EX/'before.audit.json','--after',EX/'after.audit.json','--output',diff],[S/'render_report.py','--audit',EX/'before.audit.json','--output',report]]:
                p=subprocess.run([sys.executable,*map(str,cmd)],capture_output=True,text=True); self.assertEqual(p.returncode,0,p.stderr)
            ET.parse(card); ET.parse(diff); html=report.read_text(); self.assertIn('THE SHIP BLOCKER',html); self.assertIn('Launch Score',html)
    def test_self_report_contains_proof_runs_and_integrity(self):
        with tempfile.TemporaryDirectory() as td:
            td=Path(td); card=td/'card.svg'; report=td/'report.html'; a=EX/'self.audit.json'; subprocess.check_call([sys.executable,str(S/'render_card.py'),'--audit',str(a),'--output',str(card)]); subprocess.check_call([sys.executable,str(S/'render_report.py'),'--audit',str(a),'--output',str(report)]); s=report.read_text(); self.assertIn('PROOF MODE',s); self.assertIn('proof-self-tests',s); v=subprocess.run([sys.executable,str(S/'verify_artifacts.py'),'--audit',str(a),'--card',str(card),'--report',str(report)],capture_output=True,text=True); self.assertEqual(v.returncode,0,v.stderr)
if __name__=='__main__': unittest.main()
