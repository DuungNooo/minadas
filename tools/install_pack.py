#!/usr/bin/env python3
"""Install Fantasia into an existing, stopped NeoForge instance, with backups.

Python 3.10+, standard library only. Never overwrite an existing world.
Run --dry-run to inspect the exact plan without writing anything.
"""
from pathlib import Path
import argparse
from datetime import datetime, timezone
import json
import re
import shutil
import zipfile

def source_root():
    here=Path(__file__).resolve().parent
    return here if (here/'world').is_dir() else here.parent

def plan(instance, mode='singleplayer', world_name='Fantasia_Campaign_RC1', source=None):
    source=Path(source or source_root()).resolve();instance=Path(instance).expanduser().resolve()
    if not instance.is_dir():raise ValueError('게임/서버 폴더가 존재하지 않습니다: '+str(instance))
    if not re.fullmatch(r'[A-Za-z0-9_.-]+',world_name) or world_name in ('.','..'):
        raise ValueError('월드 이름은 영문, 숫자, _, -, . 만 사용할 수 있습니다.')
    if instance==source or source.is_relative_to(instance):raise ValueError('배포 파일 폴더가 아닌 실제 게임/서버 폴더를 지정하세요.')
    target_world=instance/('saves/'+world_name if mode=='singleplayer' else world_name)
    if target_world.exists():raise FileExistsError('기존 월드는 덮어쓰지 않습니다. 다른 --world-name을 지정하세요: '+str(target_world))
    operations=[(source/'world',target_world)]
    operations += [(p,instance/'kubejs/server_scripts'/p.name) for p in sorted((source/'kubejs/server_scripts').glob('fantasia_*.js'))]
    operations.append((source/'config/ftbquests/quests',instance/'config/ftbquests/quests'))
    for src,dst in operations:
        if not src.exists():raise FileNotFoundError(src)
        if not dst.resolve().is_relative_to(instance):raise ValueError('대상 경로가 게임 폴더 밖을 가리킵니다: '+str(dst))
    legacy=[]
    for jar in sorted((instance/'mods').glob('*.jar')):
        try:
            with zipfile.ZipFile(jar) as archive:
                for name in ['META-INF/neoforge.mods.toml','META-INF/mods.toml']:
                    if name in archive.namelist():
                        text=archive.read(name).decode('utf-8')
                        if re.search(r'^\s*modId\s*=\s*[\"\']fantasia_core[\"\']',text,re.M):
                            if not jar.resolve().is_relative_to(instance):raise ValueError('기존 Core JAR가 게임 폴더 밖을 가리킵니다: '+str(jar))
                            legacy.append(jar);break
        except (zipfile.BadZipFile,UnicodeError):
            if jar.name.startswith('fantasia_core'):raise ValueError('기존 FantasiaCore JAR를 읽을 수 없습니다: '+str(jar))
    return instance,target_world,operations,legacy

def install(instance, mode='singleplayer', world_name='Fantasia_Campaign_RC1', source=None, dry_run=False):
    instance,target_world,operations,legacy=plan(instance,mode,world_name,source)
    report={'world':str(target_world),'copies':[str(dst) for _,dst in operations],'disable_legacy_core':[str(p) for p in legacy],'mode':mode}
    if dry_run:return report
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    backup=instance/'fantasia_backups'/stamp
    backup.mkdir(parents=True,exist_ok=False)
    saved=[];created=[]
    try:
        for path in legacy:
            dst=backup/path.relative_to(instance);dst.parent.mkdir(parents=True,exist_ok=True)
            shutil.move(str(path),str(dst));saved.append((dst,path))
        for src,dst in operations:
            if dst.exists():
                old=backup/dst.relative_to(instance);old.parent.mkdir(parents=True,exist_ok=True)
                shutil.move(str(dst),str(old));saved.append((old,dst))
            dst.parent.mkdir(parents=True,exist_ok=True);created.append(dst)
            if src.is_dir():shutil.copytree(src,dst)
            else:shutil.copy2(src,dst)
        report['backup']=str(backup)
        (backup/'INSTALL_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    except Exception:
        for path in reversed(created):
            if path.is_dir():shutil.rmtree(path)
            elif path.exists():path.unlink()
        for old,dst in reversed(saved):
            if old.exists():dst.parent.mkdir(parents=True,exist_ok=True);shutil.move(str(old),str(dst))
        raise
    return report

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--instance',required=True,help='게임 프로필 폴더 또는 서버 폴더. 반드시 게임/서버를 종료한 뒤 사용하세요.')
    parser.add_argument('--mode',choices=['singleplayer','server'],default='singleplayer')
    parser.add_argument('--world-name',default='Fantasia_Campaign_RC1')
    parser.add_argument('--dry-run',action='store_true')
    args=parser.parse_args()
    print(json.dumps(install(args.instance,args.mode,args.world_name,dry_run=args.dry_run),ensure_ascii=False,indent=2))
    if args.mode=='server':print('server.properties의 level-name을 '+args.world_name+' 으로 설정한 뒤 시작하세요. 기존 값은 자동 변경하지 않았습니다.')

if __name__=='__main__':main()
