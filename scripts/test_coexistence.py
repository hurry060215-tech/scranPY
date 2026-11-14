"""Exercise wheel reinstall/uninstall without altering an upstream installation."""
import argparse
import hashlib
import importlib.metadata as metadata
import json
from pathlib import Path
import subprocess
import sys
import tempfile

parser=argparse.ArgumentParser()
parser.add_argument('--wheel',type=Path,required=True)
parser.add_argument('--distribution',required=True)
parser.add_argument('--module',required=True)
parser.add_argument('--upstream-distribution',required=True)
parser.add_argument('--upstream-module',required=True)
parser.add_argument('--report',type=Path)
args=parser.parse_args()
wheel=args.wheel.resolve()
upstream=metadata.distribution(args.upstream_distribution)
original={Path(upstream.locate_file(f)).resolve() for f in upstream.files
          if str(f).endswith(('.py','METADATA','LICENSE'))}
assert original, 'No upstream files found'
def hashes():
    return {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(original)}
expected=hashes()
candidate=metadata.distribution(args.distribution)
assert not original.intersection({Path(candidate.locate_file(f)).resolve() for f in candidate.files})
with tempfile.TemporaryDirectory(prefix='coexistence-') as temp:
    def pip(*options):
        subprocess.run([sys.executable,'-m','pip','--disable-pip-version-check',*options],cwd=temp,check=True)
    def check_imports(candidate_present):
        code=f'''import importlib, importlib.util, pathlib, sys
old=importlib.import_module({args.upstream_module!r})
assert pathlib.Path(old.__file__).resolve().is_relative_to(pathlib.Path(sys.prefix).resolve())
assert bool(importlib.util.find_spec({args.module!r})) is {candidate_present!r}
'''
        if candidate_present:
            code+=f'''new=importlib.import_module({args.module!r})
assert pathlib.Path(new.__file__).resolve().is_relative_to(pathlib.Path(sys.prefix).resolve())
assert pathlib.Path(old.__file__).resolve().parent != pathlib.Path(new.__file__).resolve().parent
print(old.__file__)
print(new.__file__)
'''
        subprocess.run([sys.executable,'-I','-c',code],cwd=temp,check=True)
    check_imports(True)
    pip('install','--no-deps','--force-reinstall',str(wheel))
    assert hashes()==expected
    check_imports(True)
    try:
        pip('uninstall','-y',args.distribution)
        assert hashes()==expected
        check_imports(False)
    finally:
        pip('install','--no-deps',str(wheel))
    assert hashes()==expected
    check_imports(True)
result={'distribution':args.distribution,'upstream':args.upstream_distribution,
        'result':'passed','original_files_unchanged':len(expected),
        'phases':['side-by-side imports','wheel reinstall','candidate uninstall','candidate restore']}
if args.report:
    args.report.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
