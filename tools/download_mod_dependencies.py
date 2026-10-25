#!/usr/bin/env python3
"""Download the pinned optional magic mods to a separate folder, verifying each SHA512."""
from pathlib import Path
import argparse,hashlib,json,urllib.request

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--destination',type=Path,default=Path('magic-dependencies'));parser.add_argument('--manifest',type=Path)
 args=parser.parse_args();base=Path(__file__).resolve().parent
 manifest=args.manifest or base/'dependencies.json'
 if not manifest.exists():manifest=base.parent/'FantasiaMod/dependencies.json'
 data=json.loads(manifest.read_text());args.destination.mkdir(parents=True,exist_ok=True)
 for mod in data['mods']:
  name=mod['filename'];url=mod['url']
  if Path(name).name!=name or not url.startswith('https://cdn.modrinth.com/'):raise ValueError('Invalid dependency record')
  target=args.destination/name
  if target.exists() and hashlib.sha512(target.read_bytes()).hexdigest()==mod['sha512']:print('OK:',name);continue
  payload=urllib.request.urlopen(url,timeout=60).read()
  if hashlib.sha512(payload).hexdigest()!=mod['sha512']:raise ValueError('Dependency hash mismatch: '+name)
  temporary=target.with_suffix('.jar.downloading');temporary.write_bytes(payload);temporary.replace(target);print('Downloaded:',name)
 print('완료. 게임과 서버를 종료하고 기존 동일 모드 JAR을 백업한 뒤 이 파일들을 mods에 설치하세요.')
if __name__=='__main__':main()
