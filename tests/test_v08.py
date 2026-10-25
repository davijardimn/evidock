import importlib.util,json,subprocess,sys,tempfile,unittest,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent; SKILL=ROOT/'skills'/'reporeel'; S=SKILL/'scripts'; EX=ROOT/'examples'
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module
GH=load('reporeel_inspect_github',S/'inspect_github.py')
class V08Tests(unittest.TestCase):
    def test_github_url_parser(self):
        self.assertEqual(GH.parse_repo('davijardimn/reporeel'),('davijardimn','reporeel'))
        self.assertEqual(GH.parse_repo('https://github.com/davijardimn/reporeel'),('davijardimn','reporeel'))
        self.assertEqual(GH.parse_repo('https://github.com/davijardimn/reporeel/tree/main'),('davijardimn','reporeel'))
        self.assertEqual(GH.parse_repo('https://github.com/davijardimn/reporeel.git'),('davijardimn','reporeel'))
    def test_github_url_parser_rejects_other_hosts_and_http(self):
        for value in ['https://evil.example/a/b','http://github.com/a/b','https://github.com/only-owner','a/b/c','']:
            with self.subTest(value=value):
                with self.assertRaises(ValueError): GH.parse_repo(value)
    def test_github_file_selection_is_bounded_and_front_door_first(self):
        tree=[{'type':'blob','path':'src/main.py'},{'type':'blob','path':'requirements.txt'},{'type':'blob','path':'LICENSE'},{'type':'blob','path':'README.md'}]
        self.assertEqual(GH._selected_paths(tree,3),['README.md','LICENSE','requirements.txt'])
    def test_parse_only_never_needs_network(self):
        p=subprocess.run([sys.executable,str(S/'inspect_github.py'),'--repo','https://github.com/davijardimn/reporeel/tree/main','--parse-only'],capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stderr); d=json.loads(p.stdout); self.assertEqual(d['owner'],'davijardimn'); self.assertEqual(d['repository'],'reporeel')
    def test_badge_renders_from_validated_audit_and_markdown(self):
        with tempfile.TemporaryDirectory() as td:
            td=Path(td); badge=td/'badge.svg'; md=td/'badge.md'
            p=subprocess.run([sys.executable,str(S/'render_badge.py'),'--audit',str(EX/'after.audit.json'),'--output',str(badge),'--markdown-output',str(md)],capture_output=True,text=True)
            self.assertEqual(p.returncode,0,p.stderr); ET.parse(badge); svg=badge.read_text(encoding='utf-8'); snippet=md.read_text(encoding='utf-8'); self.assertIn('87/100 · READY',svg); self.assertIn('.reporeel/badge.svg',snippet); self.assertIn('github.com/davijardimn/reporeel',snippet)
    def test_provisional_badge_cannot_hide_provisional_state(self):
        d=json.loads((EX/'after.audit.json').read_text(encoding='utf-8')); d['provisional']=True; d['provisional_reason']='Synthetic incomplete scope for badge test.'
        with tempfile.TemporaryDirectory() as td:
            td=Path(td); audit=td/'audit.json'; badge=td/'badge.svg'; audit.write_text(json.dumps(d),encoding='utf-8')
            p=subprocess.run([sys.executable,str(S/'render_badge.py'),'--audit',str(audit),'--output',str(badge)],capture_output=True,text=True)
            self.assertEqual(p.returncode,0,p.stderr); self.assertIn('PROVISIONAL',badge.read_text(encoding='utf-8'))
if __name__=='__main__': unittest.main()
