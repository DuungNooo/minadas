#!/usr/bin/env python3
from pathlib import Path
import importlib.util,tempfile,json,re,shutil
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('validator',ROOT/'tests/validate_commands.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
with tempfile.TemporaryDirectory(prefix='fantasia_mod_check_') as t:
 root=Path(t);(root/'world/datapacks').mkdir(parents=True)
 shutil.copytree(ROOT/'FantasiaMod/src/main/resources',root/'world/datapacks/mod')
 m.ROOT=root;m.FIXTURES=ROOT/'tests/fixtures';m.validate()
res=ROOT/'FantasiaMod/src/main/resources'
chapters=json.loads((res/'fantasia/expeditions.json').read_text())['chapters']
assert len({c['id'] for c in chapters})==len(chapters)
menus=json.loads((res/'fantasia/menus.json').read_text())
for c in chapters:
 assert c['npc'] in menus
 assert len(c['steps'])==6
 # Sparse real-command simulation verifies corridor endpoints remain clear after all walls are built.
 points={}
 for s in c['steps']:
  for dx,dz in [(0,9),(0,0),(10,10),(-16,0),(16,0),(0,-16),(0,16)]:
   for y in [64,65,66]:points[s['x']+dx,y,s['z']+dz]='minecraft:air'
 files=sorted((res/f'data/fantasia/function/expansion/{c["id"]}').glob('batch_*.mcfunction'),key=lambda p:int(p.stem.split('_')[-1]))
 for f in files:
  for line in f.read_text().splitlines():
   found=re.search(r'run fill (-?\d+) (-?\d+) (-?\d+) (-?\d+) (-?\d+) (-?\d+) (\S+)',line)
   if found:
    a,b,d,e,g,h=map(int,found.groups()[:6]);block=found[7]
    for pos in points:
     x,y,z=pos
     if a<=x<=e and b<=y<=g and d<=z<=h:points[pos]=block
 for i,s in enumerate(c['steps']):
  check=[(0,9),(0,0),(10,10)]
  if i%3<2:check.append((16,0))
  if i%3>0:check.append((-16,0))
  if i<3:check.append((0,16))
  else:check.append((0,-16))
  for dx,dz in check:
   assert points[s['x']+dx,64,s['z']+dz]!='minecraft:air',(c['id'],i,dx,dz,'missing floor')
   for y in [65,66]:assert points[s['x']+dx,y,s['z']+dz]=='minecraft:air',(c['id'],i,dx,dz,'blocked path')
for p in (res/'data').rglob('*.mcfunction'):
 assert '/trigger ' not in p.read_text(),p
print(f'PASS: {len(chapters)} expedition maps, {sum(len(c["steps"]) for c in chapters)} objectives, traversable exits, no chat trigger buttons')
