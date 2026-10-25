import json,subprocess,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent; S=ROOT/'skills/evidock/scripts'
class SkillToolsTests(unittest.TestCase):
    def test_search_patterns(self):
        p=subprocess.run([sys.executable,str(S/'search_patterns.py'),'--query','missing readme'],capture_output=True,text=True,check=True); self.assertIn('front-door-void',p.stdout)
    def test_score_nonpass_zero(self):
        src=json.loads((ROOT/'examples/before.audit.json').read_text()); [c.__setitem__('points',999) for c in src['criteria']]
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'a.json'; p.write_text(json.dumps(src)); subprocess.check_call([sys.executable,str(S/'score_audit.py'),'--audit',str(p)]); d=json.loads(p.read_text());
            for c in d['criteria']: self.assertEqual(c['points'],c['max_points'] if c['status']=='PASS' else 0)
if __name__=='__main__': unittest.main()
