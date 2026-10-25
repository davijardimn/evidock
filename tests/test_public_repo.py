import json,subprocess,sys,unittest,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent; SKILL=ROOT/'skills'/'evidock'
class PublicRepoTests(unittest.TestCase):
    def test_manifests_and_skill_versions_match(self):
        p=json.loads((ROOT/'.claude-plugin/plugin.json').read_text(encoding='utf-8')); m=json.loads((ROOT/'.claude-plugin/marketplace.json').read_text(encoding='utf-8')); skill=(SKILL/'SKILL.md').read_text(encoding='utf-8'); self.assertEqual(p['name'],'evidock'); self.assertEqual(p['version'],'0.9.0'); self.assertEqual(m['name'],'evidock'); self.assertEqual(m['metadata']['version'],'0.9.0'); self.assertEqual(m['plugins'][0]['name'],'evidock'); self.assertEqual(m['plugins'][0]['version'],'0.9.0'); self.assertIn('version: "0.9.0"',skill)
    def test_pattern_library_shape(self):
        d=json.loads((SKILL/'assets/patterns.json').read_text(encoding='utf-8')); self.assertEqual(d['count'],len(d['patterns'])); self.assertGreaterEqual(d['count'],30)
        for p in d['patterns']:
            for key in ('id','category','severity','title','summary','evidence_signals','remediation'): self.assertIn(key,p)
    def test_evals_have_breadth(self): d=json.loads((ROOT/'evals/cases.json').read_text(encoding='utf-8')); self.assertGreaterEqual(len(d['cases']),16)
    def test_surface_is_packaged(self):
        for rel in ['references/github-url.md','references/fix-mode.md','references/badge.md','scripts/inspect_github.py','scripts/render_badge.py']:
            self.assertTrue((SKILL/rel).exists(),rel)
    def test_package_has_skill_root(self):
        subprocess.check_call([sys.executable,str(ROOT/'tools/package_skill.py')],cwd=ROOT); z=ROOT/'dist/evidock.zip'
        with zipfile.ZipFile(z) as f: names=set(f.namelist())
        self.assertIn('evidock/SKILL.md',names); self.assertIn('evidock/assets/patterns.json',names); self.assertIn('evidock/scripts/inspect_github.py',names); self.assertIn('evidock/scripts/render_badge.py',names); self.assertIn('evidock/references/fix-mode.md',names); self.assertNotIn('evidock/README.md',names)
if __name__=='__main__': unittest.main()
