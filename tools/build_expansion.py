#!/usr/bin/env python3
"""Authored expedition chapters, connected rooms and world interaction objectives.
Time budgets in planning documents are targets, never fabricated playtest results.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
RES=ROOT/'FantasiaMod/src/main/resources'
# Chapter format: id, title, NPC, minimum stage, palette, six authored investigation beats.
CHAPTERS=[
('blackout','서장 · 꺼지지 않는 빛','adeline',0,'stone_bricks',[
('꺼진 동쪽 회랑','정전은 사고가 아니었다. 등불 아래에서 검은 결정을 발견했다.'),
('남겨진 훈련장','수업용 골렘의 제어 문양이 낯선 손길로 바뀌어 있다.'),
('지하의 세 공명기','기록에는 새벽, 정오, 저녁 순서로 공명을 맞추라고 쓰여 있다.'),
('문 너머의 조교','조교는 실종된 교수가 마지막으로 지하에 내려갔다고 증언했다.'),
('봉인실의 침입자','검은 로브의 침입자는 아카데미의 교직원 인장을 갖고 있었다.'),
('첫 번째 균열','노아는 결정 속 파동이 네 지역의 마력핵과 같다는 사실을 확인했다.')]),
('mine_depths','불타는 광산 · 마지막 교대','irina',1,'deepslate_tiles',[
('사라진 교대표','아침 교대원 전원이 돌아오지 않았다. 광산 통로에 최근 발자국이 있다.'),
('잿빛 운반로','빈 광차 뒤에서 화염에 잠식된 경비가 나타났다.'),
('압력 조절실','증기는 낮은 압력부터 흘려보내야 한다. 청색, 황색, 적색 밸브를 찾자.'),
('갇힌 광부들','광부는 검은 인장을 단 자들이 마력 샘플을 가져갔다고 말했다.'),
('불씨를 먹는 수호자','수호자는 열을 흡수할수록 강해진다. 경고된 바닥에서 벗어나자.'),
('교수의 표본함','표본함에는 독성 검사가 아니라 살아 있는 마력에 관한 기록이 있었다.')]),
('canal_rescue','얼어붙은 수로 · 흐르지 않는 시간','riana',1,'prismarine_bricks',[
('수문 관리인의 일지','수로는 자연스럽게 언 것이 아니다. 마력이 한 지점으로 빨려 들어갔다.'),
('동결된 경비실','오염된 수로 경비들이 연구원 구조를 막는다.'),
('역류 장치','한꺼번에 열면 하류가 잠긴다. 낮은 수위에서 높은 수위 순서로 복구하자.'),
('물속의 신호','연구원은 얼음 속에서도 신호를 보내고 있었다. 안전 구역까지 이동을 지키자.'),
('얼어붙은 펌프실','펌프실의 수호자는 움직임을 늦춘다. 파란 경고 원에서 빠져나오자.'),
('누가 수문을 닫았는가','명령서의 서명은 지워졌지만 연맹 기록번호가 남아 있었다.')]),
('forest_heart','침식된 숲 · 뿌리가 기억하는 이름','rowen',1,'mossy_stone_bricks',[
('독성 잎의 표본','독은 나무에서 시작되지 않았다. 오래된 금속 관이 뿌리를 관통한다.'),
('흉터 난 정원','정화 장치를 지키던 동물들이 마력에 잠식되었다.'),
('순환의 세 돌','씨앗, 잎, 꽃. 숲이 자라는 순서로 정화석을 공명시키자.'),
('숲지기의 길','로웬의 동료를 안전한 숲길로 안내하고 뒤쫓는 마물들을 막자.'),
('검은 뿌리','오염원을 끊기 전에 수호자의 속박을 풀어야 한다.'),
('숨겨진 배관','배관은 아카데미 방향으로 이어진다. 숲은 봉인뿐 아니라 채취 시설이었다.')]),
('storm_signal','낙뢰 평원 · 하늘에 남긴 암호','theo',1,'cut_copper',[
('끊어진 중계선','낙뢰 기록 속에 규칙적인 신호가 반복된다.'),
('움직이는 전장','중계소를 빼앗은 적들은 끊임없이 위치를 바꾼다.'),
('세 개의 피뢰침','가장 짧은 침에서 가장 긴 침으로 전류를 보내야 한다.'),
('연구자의 귀환','신호를 해독한 연구자를 호위해 중계소를 벗어나자.'),
('폭풍의 전령','전령이 번개를 예고하면 붉은 표식 밖으로 이동하자.'),
('마지막 발신자','신호의 마지막 문장은 하나였다. 교수는 아직 살아 있다.')]),
('buried_lab','봉인의 진실 · 지워진 연구소','noah',3,'polished_deepslate',[
('폐쇄된 승강기','오래된 설계도에 없는 아래층이 발견되었다.'),
('자동 경비대','연구소는 침입자가 아니라 기록을 파괴하려는 자를 막도록 설정되어 있었다.'),
('연맹의 암호','창립, 번영, 봉인. 연대순으로 세 기록 장치를 맞추자.'),
('기억의 증인','도망친 기록 관리인이 원본 자료의 위치를 알고 있다.'),
('추출 장치','장치가 살아 있는 마력을 흡수한다. 가동을 멈추기 위해 수호자를 제압하자.'),
('연맹의 대가','아카데미의 번영은 마왕의 힘을 조금씩 빼앗아 얻은 것이었다.')]),
('cult_hideout','봉인의 진실 · 교수의 선택','rachel',3,'polished_blackstone_bricks',[
('밀수꾼의 통로','교단은 폐기된 연구 장비를 통해 지하로 들어왔다.'),
('인장 없는 경비','납치범들은 교수의 연구를 완성하기 위해 그를 살려 두었다.'),
('감옥의 잠금장치','달이 지고 별이 사라진 뒤 해가 뜬다. 감옥의 문양을 맞추자.'),
('베른하르트 구출','교수는 자신이 남긴 연구가 악용됐다는 사실을 알고 있었다.'),
('교단의 집행자','집행자는 출구를 막고 증인을 없애려 한다.'),
('다른 봉인법','마력을 빼앗지 않는 봉인이 가능하다. 그러나 세 전선의 공명석이 필요하다.')]),
('capital_refuge','침공 · 돌아갈 집','edric',2,'stone_bricks',[
('버려진 광장','첫 공격은 성문이 아니라 사람들이 모인 시장을 노렸다.'),
('치료소 앞의 전투','부상자가 대피할 때까지 치료소의 통로를 확보하자.'),
('성문 복구','받침대, 경첩, 잠금쇠 순으로 성문 장치를 고쳐야 한다.'),
('마지막 피난민','아직 떠나지 못한 피난민을 안전 지점까지 호위하자.'),
('공성 지휘관','지휘관은 구조 경로를 읽고 매복해 있었다.'),
('지키는 이유','성벽은 다시 세울 수 있지만 돌아오지 못한 사람은 되찾을 수 없다.')]),
('north_watch','북부 전선 · 서로의 온기','elena',4,'packed_ice',[
('멈춘 관측소','구조 신호는 들리지만 관측소 안에는 아무도 보이지 않는다.'),
('얼음 속의 균열','공허의 틈에서 나타난 적들을 막아 관측소를 확보하자.'),
('등대의 빛','새벽빛, 한낮의 빛, 황혼빛을 차례로 밝혀 길을 열자.'),
('고립된 정찰대','흩어진 정찰대원을 등대까지 호위하자.'),
('백야의 장군','장군의 냉기를 피하며 움직여야 한다. 제자리에 머물면 얼어붙는다.'),
('북부 공명석','공명석은 혼자 버티는 힘이 아니라 서로 이어지는 힘에 반응했다.')]),
('east_garden','동부 전선 · 다시 자라는 것','claude',4,'mossy_stone_bricks',[
('독 안개의 끝','버려진 약초원에 아직 생명의 흔적이 남아 있다.'),
('정찰대의 흔적','정찰대가 남긴 길을 따라 독성 마물들을 제압하자.'),
('정화수 순환','뿌리에서 줄기로, 줄기에서 잎으로 물을 보내야 한다.'),
('약초사의 길','약초사를 호위해 치료제 재료를 안전한 곳으로 옮기자.'),
('시든 정원의 장군','장군은 주변 생명을 자신의 방패로 삼고 있다.'),
('동부 공명석','한 번 상처 입은 곳에서도 새싹은 자란다. 클라우드는 돌아갈 길을 택했다.')]),
('south_forge','남부 전선 · 불꽃의 값','bernard',4,'nether_bricks',[
('비어 있는 병기고','교단은 무기보다 사람의 마력을 연료로 삼았다.'),
('붉은 제련로','제련로 주변의 병사들을 제압하고 가동을 멈출 방법을 찾자.'),
('열 교환 장치','냉각, 순환, 차단. 열을 먼저 빼내고 공급을 끊어야 한다.'),
('실험체가 된 포로','포로는 적군이었지만 실험의 희생자이기도 했다. 탈출을 돕자.'),
('피의 장군','장군은 붉은 영역에서 힘을 회복한다. 경고 지점에서 벗어나 싸우자.'),
('남부 공명석','교수는 자신의 잘못을 지우는 대신 남은 생애로 책임지겠다고 약속했다.')]),
('castle_memory','최종막 · 왕이 되기 전','headmaster',5,'polished_blackstone_bricks',[
('칠흑 회랑','마왕성의 벽에는 정복이 아니라 잃어버린 사람들의 이름이 새겨져 있다.'),
('뒤틀린 연구실','연맹의 실험과 닮은 장치들이 왕성을 채우고 있다.'),
('과거의 세 문','탄생, 상실, 왕관. 벨카리온이 걸어온 순서로 기억의 문을 열자.'),
('기록을 지키는 자','마지막 기록관을 호위해 과거 마법사들의 원본을 확보하자.'),
('장군의 잔재','세 전선에서 물리친 의지가 하나의 잔재로 되살아났다.'),
('왕좌 앞의 기록','누구도 처음부터 괴물은 아니었다. 하지만 고통이 타인의 고통을 정당화하지는 않는다.')]),
]
# Keep room contents authored and visibly distinct; do not use repeated kills as time gates.
def create():
 chapters=[];functions=RES/'data/fantasia/function/expansion';functions.mkdir(parents=True,exist_ok=True)
 chunks=[]
 for n,(id,title,npc,stage,palette,beats) in enumerate(CHAPTERS):
  cx=1024+(n%4)*256;cz=1024+(n//4)*256
  steps=[];commands=[f'kill @e[tag=fa_exp_station,x={cx-16},y=60,z={cz-16},dx=128,dy=32,dz=80]',f'kill @e[tag=fa_exp_label,x={cx-16},y=60,z={cz-16},dx=128,dy=32,dz=80]']
  # Six 31x31 rooms, connected by 17-block corridors; each room is independently traversable.
  for i,(name,lore) in enumerate(beats):
   x=cx+(i%3)*48;z=cz+(i//3)*48;typ=['investigate','battle','sequence','escort','boss','evidence'][i]
   floor='polished_andesite' if palette=='packed_ice' else palette
   commands += [f'fill {x-16} 62 {z-16} {x+16} 63 {z+16} minecraft:deepslate_tiles',f'fill {x-16} 64 {z-16} {x+16} 64 {z+16} minecraft:{floor}']
   for ax,az,bx,bz in [(x-16,z-16,x+16,z-16),(x-16,z+16,x+16,z+16),(x-16,z-16,x-16,z+16),(x+16,z-16,x+16,z+16)]:
    commands.append(f'fill {ax} 65 {az} {bx} 69 {bz} minecraft:{palette}')
   for dx,dz in [(-12,-12),(-12,12),(12,-12),(12,12)]:
    commands += [f'fill {x+dx} 65 {z+dz} {x+dx} 70 {z+dz} minecraft:chiseled_stone_bricks',f'setblock {x+dx} 71 {z+dz} minecraft:sea_lantern']
   for dx in [-7,0,7]:
    commands += [f'setblock {x+dx} 64 {z} minecraft:sea_lantern']
   if i%3<2:
    commands += [f'fill {x+16} 65 {z-2} {x+16} 68 {z+2} minecraft:air',f'fill {x+17} 64 {z-3} {x+32} 64 {z+3} minecraft:stone_bricks',f'fill {x+32} 65 {z-2} {x+32} 68 {z+2} minecraft:air']
   if i<3:
    commands += [f'fill {x-2} 65 {z+16} {x+2} 68 {z+16} minecraft:air',f'fill {x-3} 64 {z+17} {x+3} 64 {z+32} minecraft:stone_bricks',f'fill {x-2} 65 {z+32} {x+2} 68 {z+32} minecraft:air']
   # Props around the clear center differ by objective.
   if typ in ('investigate','evidence'):
    for dx in [-10,10]:commands += [f'fill {x+dx} 65 {z-7} {x+dx} 67 {z+7} minecraft:bookshelf']
    commands += [f'setblock {x} 65 {z-7} minecraft:lectern']
   elif typ=='sequence':
    for j,block in enumerate(['lapis_block','gold_block','redstone_block']):commands.append(f'fill {x+(j-1)*7} 65 {z-7} {x+(j-1)*7} 67 {z-7} minecraft:{block}')
   elif typ=='boss':
    commands += [f'fill {x-4} 64 {z-4} {x+4} 64 {z+4} minecraft:crying_obsidian']
   else:
    for dx,dz in [(-9,-5),(9,5)]:commands.append(f'fill {x+dx} 65 {z+dz} {x+dx+2} 66 {z+dz+2} minecraft:stone_bricks')
   steps.append({'title':name,'text':lore,'kind':typ,'x':x,'z':z,'sequence':[0,1,2] if n%2==0 else [2,0,1]})
  # Carve both ends after every room wall exists (later rooms otherwise reseal corridors).
  for i in range(6):
   x=cx+(i%3)*48;z=cz+(i//3)*48
   if i%3<2:
    for dx in (16,32):commands.append(f'fill {x+dx} 65 {z-2} {x+dx} 68 {z+2} minecraft:air')
   if i<3:
    for dz in (16,32):commands.append(f'fill {x-2} 65 {z+dz} {x+2} 68 {z+dz} minecraft:air')
  # Every chamber's main marker is a directly interacted entity handled by Java, never chat commands.
  for i,step in enumerate(steps):
   x,z=step['x'],step['z']
   commands.append(f'summon minecraft:interaction {x} 65 {z} '+f'{{Tags:["fa_exp_station","fa_exp_{id}_{i}"],width:2.0f,height:2.5f,response:1b}}')
   label=json.dumps(json.dumps({'text':step['title'],'color':'aqua'},ensure_ascii=False),ensure_ascii=False)
   commands.append(f'summon minecraft:text_display {x} 68 {z} {{Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:{label}}}')
  # Hold only this area's chunks, yield to load, then batch world writes.
  area=functions/id;area.mkdir(exist_ok=True)
  chunk_positions=[(x,z) for x in range((cx-16)//16,(cx+112)//16+1) for z in range((cz-16)//16,(cz+64)//16+1)]
  start=[f'execute in fantasia:campaign run forceload add {cx-16} {cz-16} {cx+112} {cz+64}',f'schedule function fantasia:expansion/{id}/wait 10t replace']
  (area/'start.mcfunction').write_text('\n'.join(start)+'\n')
  wait=['scoreboard players set #exp_chunks fa_world 0']+[f'execute in fantasia:campaign if loaded {x*16} 65 {z*16} run scoreboard players add #exp_chunks fa_world 1' for x,z in chunk_positions]
  wait += [f'execute unless score #exp_chunks fa_world matches {len(chunk_positions)} run schedule function fantasia:expansion/{id}/wait 10t replace',f'execute if score #exp_chunks fa_world matches {len(chunk_positions)} run function fantasia:expansion/{id}/batch_0']
  (area/'wait.mcfunction').write_text('\n'.join(wait)+'\n')
  for batch,offset in enumerate(range(0,len(commands),40)):
   lines=['execute in fantasia:campaign run '+c for c in commands[offset:offset+40]]
   if offset+40<len(commands):lines.append(f'schedule function fantasia:expansion/{id}/batch_{batch+1} 1t replace')
   else:
    lines += [f'execute in fantasia:campaign run forceload remove {cx-16} {cz-16} {cx+112} {cz+64}']
    lines += [f'function fantasia:expansion/{CHAPTERS[n+1][0]}/start'] if n+1<len(CHAPTERS) else ['scoreboard players set #exp_ready fa_world 1','tellraw @a {"text":"추가 원정 지역 준비 완료. NPC의 원정 메뉴를 확인하세요.","color":"green"}']
   (area/f'batch_{batch}.mcfunction').write_text('\n'.join(lines)+'\n')
  chapters.append({'id':id,'title':title,'npc':npc,'stage':stage,'steps':steps})
 (RES/'fantasia/expeditions.json').write_text(json.dumps({'chapters':chapters},ensure_ascii=False,indent=2))
 (functions/'start.mcfunction').write_text('execute if score #exp_ready fa_world matches 1.. run return 0\nscoreboard players set #exp_ready fa_world 2\nfunction fantasia:expansion/blackout/start\n')
 tick=RES/'data/fantasia/function/tick.mcfunction'
 tick.write_text('\n'.join(l for l in tick.read_text().splitlines() if 'function fantasia:expansion/start' not in l)+'\n'+'execute if score #ready fa_world matches 1 unless score #exp_ready fa_world matches 1.. run function fantasia:expansion/start\n')
 callbacks=['fantasia:expansion/'+str(p.relative_to(functions)).removesuffix('.mcfunction') for p in functions.rglob('*.mcfunction') if p.stem!='restart']
 (functions/'restart.mcfunction').write_text('\n'.join('schedule clear '+f for f in callbacks)+'\nscoreboard players set #exp_ready fa_world 0\n')
 load=RES/'data/fantasia/function/load.mcfunction'
 load.write_text(load.read_text()+'execute unless score #exp_ready fa_world matches 1 run function fantasia:expansion/restart\n')
 print(f'Built {len(chapters)} connected expedition maps / {sum(len(c["steps"]) for c in chapters)} authored objectives')
if __name__=='__main__':create()
