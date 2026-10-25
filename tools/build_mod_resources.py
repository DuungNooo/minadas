#!/usr/bin/env python3
"""Embed existing campaign data and export whitelisted GUI menus and exam questions."""
from pathlib import Path
import json,re,shutil,subprocess
ROOT=Path(__file__).resolve().parents[1]
RES=ROOT/'FantasiaMod/src/main/resources'
if (RES/'data').exists():shutil.rmtree(RES/'data')
for pack in ('fantasia_all_spells','fantasia_campaign'):
 shutil.copytree(ROOT/'world/datapacks'/pack/'data',RES/'data',dirs_exist_ok=True)
# Merge load/tick tags: copytree alone would discard the research load function.
for tag in ('load','tick'):
 values=[]
 for pack in ('fantasia_all_spells','fantasia_campaign'):
  p=ROOT/'world/datapacks'/pack/'data/minecraft/tags/function'/f'{tag}.json'
  if p.exists():values+=json.loads(p.read_text())['values']
 p=RES/'data/minecraft/tags/function'/f'{tag}.json'
 p.write_text(json.dumps({'values':list(dict.fromkeys(values))}))
(RES/'pack.mcmeta').write_text(json.dumps({'pack':{'pack_format':48,'description':'Fantasia Campaign mod data'}}))
# NPC interaction is exclusively handled by the mod. Ordinary villagers are untouched.
shutil.rmtree(RES/'data/fantasia/advancement/npc')
menus={}
for p in (RES/'data/fantasia/function/npc').glob('*.mcfunction'):
 if p.stem in ('load','spawn','wait'):continue
 text=[]; actions=[]
 for line in p.read_text().splitlines():
  if line.startswith('tellraw @s '):
   value=json.loads(line.removeprefix('tellraw @s '))
   if isinstance(value,dict): text.append(value.get('text',''))
   else:
    for b in value:
     command=b.get('clickEvent',{}).get('value','')
     m=re.fullmatch(r'/trigger fa_action set (\d+)',command)
     if m:actions.append({'label':b['text'].strip(' []'),'id':int(m[1])})
 menus[p.stem]={'title':text[0],'body':'\n\n'.join(text[1:]),'actions':actions}
 # Legacy advancement rewards/functions must never open chat menus in mod mode.
 p.write_text('# NPC UI is provided by Fantasia Campaign.\n')
(RES/'fantasia').mkdir(exist_ok=True)
(RES/'fantasia/menus.json').write_text(json.dumps(menus,ensure_ascii=False,indent=2))
s=(ROOT/'kubejs/server_scripts/fantasia_exam_runtime.js').read_text().split('function pname')[0]
program=s+'\nconsole.log(JSON.stringify({questions:QUESTIONS,schools:SCHOOL_LABELS,weapons:WEAPON_LABELS}))'
r=subprocess.run(['node','-e',program],check=True,capture_output=True,text=True)
(RES/'fantasia/exam.json').write_text(json.dumps(json.loads(r.stdout),ensure_ascii=False,indent=2))
s=(ROOT/'kubejs/server_scripts/fantasia_magic_runtime.js').read_text()
a=s.index('const FANTASIA_SPELL_GATES = ')+len('const FANTASIA_SPELL_GATES = ')
b=s.index('\n}',a)+2
(RES/'fantasia/spells.json').write_text(json.dumps(json.loads(s[a:b]),ensure_ascii=False,indent=2))
s=(ROOT/'kubejs/server_scripts/fantasia_campaign_runtime.js').read_text().split('// Campaign progress')[0]
r=subprocess.run(['node','-e',s+'\nconsole.log(JSON.stringify(FANTASIA_NPCS))'],check=True,capture_output=True,text=True)
(RES/'fantasia/npcs.json').write_text(r.stdout)
# Remove trigger dispatch; server UI calls the same validation function immediately.
p=RES/'data/fantasia/function/tick.mcfunction'
p.write_text('\n'.join(l for l in p.read_text().splitlines() if 'as @a[scores={fa_action=1..}]' not in l)+'\n')
for file in ['join.mcfunction','second.mcfunction','action.mcfunction']:
 p=RES/'data/fantasia/function'/file
 lines=[l for l in p.read_text().splitlines() if 'scoreboard players enable' not in l]
 p.write_text('\n'.join(lines).replace('입학 검사 선택지는 채팅에서 클릭합니다.','아델린과 대화하면 입학 검사 화면이 열립니다.')+'\n')
p=RES/'data/fantasia/function/load.mcfunction'
p.write_text(p.read_text().replace('fa_action trigger','fa_action dummy'))
# No external chat command entrypoints in embedded data.
for p in (RES/'data').rglob('*.mcfunction'):
 s=p.read_text()
 if '/fantasia_' in s or '/trigger ' in s:
  p.write_text('\n'.join(l for l in s.splitlines() if '/fantasia_' not in l and '/trigger ' not in l)+'\n')
# Research ranks are now granted by actual practice in the mod, not story boss rewards.
for p in (RES/'data').rglob('*.mcfunction'):
 lines=[l for l in p.read_text().splitlines() if not re.search(r'advancement grant .* only fantasia_research:(?:fire|ice|lightning|nature|holy|ender|blood|evocation|void)_tier_[123]',l)]
 p.write_text('\n'.join(lines)+'\n')
# TextDisplay in 1.21.1 decodes alignment even when absent; set it explicitly.
for p in (RES/'data').rglob('*.mcfunction'):
 s=p.read_text().replace('billboard:"center",','billboard:"center",alignment:"center",')
 p.write_text(s)
# Recover interrupted first-time builds. Persisted #building alone cannot prove that callbacks/tickets survived.
mapdir=RES/'data/fantasia/function/map'
callbacks=['fantasia:map/'+str(p.relative_to(mapdir)).removesuffix('.mcfunction') for p in mapdir.rglob('*.mcfunction') if p.stem!='restart']
(mapdir/'restart.mcfunction').write_text('\n'.join('schedule clear '+f for f in callbacks)+'\nscoreboard players set #building fa_world 0\nfunction fantasia:map/build\n')
p=RES/'data/fantasia/function/load.mcfunction'
p.write_text(p.read_text().replace('unless score #ready fa_world matches 1 run function fantasia:map/build','unless score #ready fa_world matches 1 run function fantasia:map/restart'))
print('Embedded campaign, research, 12-question exam, NPC menus and 111 spell gates')

from build_expansion import create
create()
