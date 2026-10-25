#!/usr/bin/env python3
"""Package the compiled standalone mod without third-party binaries or saved worlds."""
from pathlib import Path
import hashlib,json,zipfile,shutil
ROOT=Path(__file__).resolve().parents[1]
MOD=ROOT/'FantasiaMod';OUT=ROOT/'releases';NAME='Fantasia_Campaign_Mod_1.2.0_RC2'
JAR=MOD/'build/libs/fantasia-campaign-1.2.0-rc.2.jar'
def digest(data):return hashlib.sha256(data).hexdigest()
def archive(target,files):
 manifest={}
 with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for name,p in sorted(files.items()):
   data=p.read_bytes();z.writestr(NAME+'/'+name,data);manifest[name]=digest(data)
  z.writestr(NAME+'/SHA256SUMS.json',json.dumps(manifest,indent=2)+'\n')
 with zipfile.ZipFile(target) as z:
  assert z.testzip() is None
  for name,hash in manifest.items():assert digest(z.read(NAME+'/'+name))==hash
 return {'name':target.name,'bytes':target.stat().st_size,'sha256':digest(target.read_bytes()),'files':len(manifest)}
def main():
 with zipfile.ZipFile(JAR) as z:
  assert z.testzip() is None
  assert not any('/verification/' in name for name in z.namelist())
  assert 'data/minecraft/worldgen/world_preset/flat.json' not in z.namelist()
  assert 'data/fantasia_campaign/structure/test_empty.nbt' not in z.namelist()
  assert 'META-INF/neoforge.mods.toml' in z.namelist()
 OUT.mkdir(exist_ok=True);shutil.copy2(JAR,OUT/JAR.name)
 files={'mods/'+JAR.name:JAR,'install.py':ROOT/'tools/install_mod.py','download_dependencies.py':ROOT/'tools/download_mod_dependencies.py','dependencies.json':MOD/'dependencies.json','README_먼저읽기.txt':MOD/'README_KO.md','README.md':MOD/'README_KO.md','VALIDATION_MOD_KO.md':MOD/'VALIDATION_MOD_KO.md','CHANGELOG_KO.md':ROOT/'CHANGELOG_KO.md'}
 result=[archive(OUT/(NAME+'.zip'),files)]
 source={}
 for directory in ['FantasiaMod','tools','tests','kubejs','world/datapacks','config','fantasia_content']:
  for p in (ROOT/directory).rglob('*'):
   relative=p.relative_to(ROOT)
   if not p.is_file() or any(part in {'.gradle','build','run','run-verification','__pycache__','.git'} for part in relative.parts) or p.suffix in {'.pyc','.log'}:continue
   source[str(relative)]=p
 for file in ['README.md','CHANGELOG_KO.md','VERSION','.gitignore']:source[file]=ROOT/file
 result.append(archive(OUT/(NAME+'_source.zip'),source))
 result.insert(0,{'name':JAR.name,'bytes':JAR.stat().st_size,'sha256':digest(JAR.read_bytes())})
 (OUT/'MOD_RELEASE_MANIFEST.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
