#!/usr/bin/env python3
"""Build a clean install ZIP plus a reproducible source ZIP; no mod binaries."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT.parent/'artifacts'
NAME='Fantasia_Campaign_1.1.0_RC1'

def checksum(data):return hashlib.sha256(data).hexdigest()

def archive(path, entries):
    manifest={}
    with zipfile.ZipFile(path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for target,source in sorted(entries.items()):
            data=source.read_bytes();z.writestr(NAME+'/'+target,data);manifest[target]=checksum(data)
        z.writestr(NAME+'/SHA256SUMS.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None
        for target,digest in manifest.items():assert checksum(z.read(NAME+'/'+target))==digest
    return {'name':path.name,'bytes':path.stat().st_size,'sha256':checksum(path.read_bytes()),'files':len(manifest)}

def collect(directory):
    return {str(p.relative_to(ROOT)):p for p in (ROOT/directory).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'}

def main():
    OUT.mkdir(exist_ok=True)
    base={}
    for directory in ['world','kubejs','config']:base.update(collect(directory))
    for file in ['README.md','CHANGELOG_KO.md','VALIDATION_KO.md','VERSION']:base[file]=ROOT/file
    base['install.py']=ROOT/'tools/install_pack.py'
    base['map_preview.png']=ROOT/'artifacts/map_preview.png'
    base['map_preview.svg']=ROOT/'artifacts/map_preview.svg'
    base['README_먼저읽기.txt']=ROOT/'README.md'
    result=[archive(OUT/(NAME+'.zip'),base)]
    source={}
    for directory in ['world','kubejs','config','tools','tests','OPTIONAL_FantasiaCore_source','fantasia_content','docs']:source.update(collect(directory))
    for file in ['README.md','CHANGELOG_KO.md','VALIDATION_KO.md','VERSION']:source[file]=ROOT/file
    source['artifacts/validation.log']=ROOT/'artifacts/validation.log'
    source['artifacts/map_preview.png']=ROOT/'artifacts/map_preview.png'
    source['artifacts/map_preview.svg']=ROOT/'artifacts/map_preview.svg'
    for p in ROOT.iterdir():
        if p.is_file() and p.suffix in ('.txt','.md','.json') and p.name not in source:
            source['docs/original_reference/'+p.name]=p
    result.append(archive(OUT/(NAME+'_source.zip'),source))
    (OUT/'RELEASE_MANIFEST.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
