#!/usr/bin/env python3
"""Install the standalone Fantasia mod; preserve worlds and back up conflicting legacy files."""
from pathlib import Path
import argparse,datetime,shutil,zipfile,tomllib

def mod_id(path):
 try:
  with zipfile.ZipFile(path) as z:
   for metadata in ('META-INF/neoforge.mods.toml','META-INF/mods.toml'):
    if metadata in z.namelist():return {m.get('modId') for m in tomllib.loads(z.read(metadata).decode()).get('mods',[])}
 except (OSError,zipfile.BadZipFile,ValueError):pass
 return set()

def install(instance,jar,dry_run=False):
 instance=instance.resolve();jar=jar.resolve()
 if not instance.is_dir():raise ValueError('마인크래프트 인스턴스 폴더가 존재하지 않습니다.')
 if not jar.is_file() or 'fantasia_campaign' not in mod_id(jar):raise ValueError('유효한 Fantasia Campaign JAR이 필요합니다.')
 candidates=[]
 for name in ('fantasia_exam_runtime.js','fantasia_campaign_runtime.js','fantasia_magic_runtime.js'):
  p=instance/'kubejs/server_scripts'/name
  if p.exists():candidates.append(p)
 mods=instance/'mods'
 if mods.exists():
  for p in mods.glob('*.jar'):
   if mod_id(p)&{'fantasia_campaign','fantasia_core'}:candidates.append(p)
 # Only remove our two legacy datapacks. No level.dat, player data or region is touched.
 worlds=[]
 if (instance/'saves').is_dir():worlds.extend(p for p in (instance/'saves').iterdir() if p.is_dir())
 worlds.extend(p for p in instance.iterdir() if p.is_dir() and (p/'level.dat').exists())
 for world in worlds:
  for name in ('fantasia_campaign','fantasia_all_spells'):
   for p in (world/'datapacks'/name,world/'datapacks'/(name+'.zip')):
    if p.exists():candidates.append(p)
 for p in candidates:
  if p.is_symlink() or not p.resolve().is_relative_to(instance):raise ValueError('외부 링크는 자동 변경하지 않습니다: '+str(p))
 target=mods/jar.name
 if not target.parent.resolve().is_relative_to(instance):raise ValueError("mods 폴더가 인스턴스 외부를 가리킵니다.")
 if target.exists() and target not in candidates:candidates.append(target)
 payload=jar.read_bytes()
 backup=instance/'fantasia-backups'/datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
 print('설치:',target)
 for p in candidates:print('백업 후 비활성화:',p.relative_to(instance))
 if dry_run:return
 moved=[];installed=False
 try:
  for p in candidates:
   dest=backup/p.relative_to(instance);dest.parent.mkdir(parents=True,exist_ok=True);shutil.move(p,dest);moved.append((p,dest))
  mods.mkdir(exist_ok=True)
  # Copy through a temporary name so interruption cannot leave a truncated active JAR.
  temporary=mods/(jar.name+'.installing');temporary.write_bytes(payload);temporary.replace(target);installed=True
 except Exception:
  if installed:target.unlink(missing_ok=True)
  (mods/(jar.name+".installing")).unlink(missing_ok=True)
  for original,saved in reversed(moved):original.parent.mkdir(parents=True,exist_ok=True);shutil.move(saved,original)
  raise
 print('완료. 월드와 진행 기록은 유지됩니다. 백업:',backup if moved else '(기존 파일 없음)')
 print('싱글플레이는 게임을, 멀티플레이는 서버와 모든 클라이언트를 완전히 재시작하세요.')

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--instance',required=True,type=Path)
 parser.add_argument('--jar',type=Path)
 parser.add_argument('--dry-run',action='store_true')
 args=parser.parse_args();base=Path(__file__).resolve().parent
 jar=args.jar
 if jar is None:
  jars=list((base/'mods').glob('fantasia-campaign-*.jar'))
  if len(jars)!=1:parser.error('--jar로 설치할 JAR을 지정하세요.')
  jar=jars[0]
 install(args.instance,jar,args.dry_run)
if __name__=='__main__':main()
