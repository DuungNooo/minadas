#!/usr/bin/env python3
"""Generate the playable Minecraft 1.21.1 campaign datapack (no third-party dependencies)."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'world/datapacks/fantasia_campaign'
FN=PACK/'data/fantasia/function'
def write(rel,data):
 p=PACK/rel; p.parent.mkdir(parents=True,exist_ok=True);p.write_text(data,encoding='utf-8')
def fun(name,lines):
 if isinstance(lines,str): lines=lines.splitlines()
 write(f'data/fantasia/function/{name}.mcfunction','\n'.join(lines)+'\n')
def js(x):return json.dumps(x,ensure_ascii=False,separators=(',',':'))
def msg(text,color='gold'):return 'tellraw @s '+js({'text':text,'color':color})
def button(label,action):return {'text':'[ '+label+' ] ','color':'aqua','bold':True,'clickEvent':{'action':'run_command','value':f'/trigger fa_action set {action}'}}
def buttons(items):return 'tellraw @s '+js([button(*x) for x in items])
def reward(event):return f'advancement grant @s only fantasia_research:campaign/{event}'
def grant(event):return f'advancement grant @s only fantasia_research:{event}'
areas={
 'hub':(0,0),'mine':(160,0),'canal':(0,160),'forest':(-160,0),'storm':(0,-160),
 'archive':(160,160),'capital':(-160,160),'north':(-160,-160),'east':(160,-160),'south':(320,0),'castle':(320,160)}
npcs={
 'adeline':('아델린 · 안내',0,0,'hub'), 'kyle':('카일 · 훈련과 보급',6,0,'hub'),
 'seraphine':('세라핀 · 치료',-6,0,'hub'), 'noah':('노아 · 연구',0,8,'hub'),
 'irina':('이리나 · 불타는 광산',160,-14,'mine'),'riana':('리아나 · 얼어붙은 수로',0,146,'canal'),
 'rowen':('로웬 · 침식된 숲',-160,-14,'forest'),'theo':('테오 · 낙뢰 평원',0,-174,'storm'),
 'rachel':('라헬 · 봉인서고',160,146,'archive'),'edric':('에드릭 · 수도 방어',-160,146,'capital'),
 'elena':('엘레나 · 북부 전선',-160,-174,'north'),'claude':('클라우드 · 동부 전선',160,-174,'east'),
 'bernard':('베른하르트 · 남부 전선',320,-14,'south'),'headmaster':('헤론 · 마왕성',320,140,'castle')}
regions=['mine','canal','forest','storm'];fronts=['north','east','south']
objs=['fa_stage','fa_gear','fa_heal','fa_supplies','fa_deaths','fa_prevdeath','fa_ok','fa_timer','fa_archive','fa_ending']+[f'fa_{x}' for x in regions+fronts]
write('pack.mcmeta',js({'pack':{'pack_format':48,'description':'Fantasia 1.1 · 아카데미부터 엔딩까지 / Minecraft 1.21.1'}}))
write('data/minecraft/tags/function/load.json',js({'values':['fantasia:load']}));write('data/minecraft/tags/function/tick.json',js({'values':['fantasia:tick']}))
load=['scoreboard objectives add fa_world dummy','scoreboard objectives add fa_action trigger']+[f'scoreboard objectives add {o} '+('deathCount' if o=='fa_deaths' else 'dummy') for o in objs]
load+=['scoreboard players set #clock fa_world 0','execute unless score #ready fa_world matches 1 run function fantasia:map/build','execute if score #ready fa_world matches 1 run function fantasia:resume','bossbar add fantasia:belkarion {"text":"벨카리온","color":"dark_purple"}','bossbar set fantasia:belkarion color purple','bossbar set fantasia:belkarion max 3','bossbar set fantasia:belkarion visible false']
fun('load',load)
encounters=['tutorial','mine','canal','forest','storm','defense','north','east','south','castle']
fun('resume',[f'execute in fantasia:campaign run function fantasia:encounter/{e}/abort' for e in encounters]+['function fantasia:npc/load'])
fun('tick',[
 'execute if score #ready fa_world matches 1 unless score #npcs fa_world matches 1..2 run function fantasia:resume',
 'execute if score #ready fa_world matches 1 as @a[tag=!fa_joined] at @s run function fantasia:join',
 'execute if score #ready fa_world matches 1 as @a[scores={fa_action=1..}] at @s run function fantasia:action',
 'scoreboard players add #clock fa_world 1',
 'execute if score #ready fa_world matches 1 if score #clock fa_world matches 20.. run function fantasia:second',
 'execute if score #clock fa_world matches 20.. run scoreboard players set #clock fa_world 0'])
join=[
 'execute unless score #ready fa_world matches 1 run return 0',
 'execute if entity @s[tag=fa_joined] run return 0','tag @s add fa_joined']
join += [f'scoreboard players add @s {o} 0' for o in objs if o!='fa_deaths']
join += ['scoreboard players add @s fa_deaths 0','scoreboard players operation @s fa_prevdeath = @s fa_deaths','scoreboard players set @s fa_action 0','scoreboard players enable @s fa_action','execute in fantasia:campaign run tp @s 0 65 -8 0 0','execute in fantasia:campaign run spawnpoint @s 0 65 -8','gamemode adventure @s','effect give @s minecraft:resistance 10 4 true',msg('Fantasia: 균열의 왕 — 아델린을 우클릭해 이야기를 시작하세요. 입학 검사 선택지는 채팅에서 클릭합니다.'),msg('NPC 우클릭 → 버튼으로 이동/진행. 장비는 카일에게 수령, 회복은 세라핀에게 요청하세요.','white')]
fun('join',join)
second=[
 'scoreboard players remove @a[scores={fa_heal=1..}] fa_heal 1',
 'scoreboard players remove @a[scores={fa_supplies=1..}] fa_supplies 1',
 'execute as @a[tag=fa_joined] at @s unless score @s fa_deaths = @s fa_prevdeath run function fantasia:recover',
 'execute as @a[tag=fa_joined] at @s if dimension fantasia:campaign if entity @s[y=-64,dy=108] run function fantasia:recover',
 'execute as @a[scores={fa_timer=1..}] run scoreboard players remove @s fa_timer 1',
 'execute as @a[scores={fa_storm=1..2,fa_timer=0}] run function fantasia:puzzle/storm_timeout',
 'execute as @a[tag=fa_joined] run scoreboard players enable @s fa_action']
second += [f'execute in fantasia:campaign if score #{e} fa_world matches 1 run function fantasia:encounter/{e}/tick' for e in encounters]
second+=['execute as @a[scores={fa_stage=1,fa_mine=5,fa_canal=5,fa_forest=5,fa_storm=5}] run function fantasia:milestone/regions','execute as @a[scores={fa_stage=4,fa_north=5,fa_east=5,fa_south=5}] run function fantasia:milestone/fronts']
fun('second',second)
clear_tags=['tag @s remove fa_fighting']+[f'tag @s remove fa_in_{e}' for e in encounters]
fun('recover',clear_tags+['scoreboard players operation @s fa_prevdeath = @s fa_deaths','execute in fantasia:campaign run tp @s 0 65 -8','effect give @s minecraft:regeneration 6 2 true','effect give @s minecraft:resistance 10 4 true',msg('아카데미로 구조되었습니다. 이미 완료한 조사 기록은 유지됩니다. 다시 NPC에게 도전을 요청할 수 있습니다.','yellow')])
fun('home',clear_tags+['execute in fantasia:campaign run tp @s 0 65 -8','scoreboard players set @s fa_ok 1'])
fun('admin/reset_player',clear_tags+[f'scoreboard players set @s {o} 0' for o in objs if o not in ('fa_deaths','fa_prevdeath')]+['scoreboard players operation @s fa_prevdeath = @s fa_deaths']+[f'advancement revoke @s only fantasia_research:campaign/{event}' for event in ['intro','mine','canal','forest','storm','regions','defense','truth','north','east','south','fronts','castle','ending']]+['tag @s remove fa_joined','function fantasia:join',msg('개인 캠페인 진행만 초기화했습니다. 맵과 다른 플레이어 진행은 유지됩니다.')])
# NPC spawning is repeatable and never duplicates the old entities.
spawn=['kill @e[tag=fa_npc]','kill @e[tag=fa_station]','kill @e[tag=fa_label]', 'gamerule keepInventory true','gamerule mobGriefing false','gamerule doFireTick false','gamerule doMobSpawning false','difficulty normal','team add fa_npcs','team modify fa_npcs collisionRule never']
for id,(name,x,z,area) in npcs.items():
 spawn += [f'summon minecraft:villager {x} 65 {z} '+"{Tags:[\"fa_npc\",\"fa_npc_"+id+"\"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomName:"+json.dumps(js({'text':name,'color':'gold'}),ensure_ascii=False)+",CustomNameVisible:1b,VillagerData:{type:\"minecraft:plains\",profession:\"minecraft:librarian\",level:5},Offers:{Recipes:[]}}"]
 write(f'data/fantasia/advancement/npc/{id}.json',js({'criteria':{'talk':{'trigger':'minecraft:player_interacted_with_entity','conditions':{'entity':{'type':'minecraft:villager','nbt':'{Tags:["fa_npc_'+id+'"]}'}}}},'rewards':{'function':f'fantasia:npc/{id}'}}))
# Menus: click replay only works near the matching NPC and with current eligibility.
for id,(name,x,z,area) in npcs.items():
 lines=[f'advancement revoke @s only fantasia:npc/{id}',msg(name)]
 if id=='adeline':
  lines += [msg('네 마력핵이 동시에 약해졌어요. 입학 검사를 마치고 카일의 기초 훈련을 통과하면 조사 허가를 드릴게요.','white'),'function fantasia:status']
  lines += [buttons([('광산',101),('수로',102),('숲',103),('평원',104)]),buttons([('수도 방어',105),('봉인서고',106),('북부',107),('동부',108),('남부',109),('마왕성',110)])]
 elif id=='kyle': lines += [msg('장비를 받고 훈련장에서 세 적을 쓰러뜨려라. 검사를 마쳐야 훈련을 시작할 수 있다.','white'),buttons([('훈련 장비 수령',11),('기초 훈련 시작',12),('선택 실습 재료',14)])]
 elif id=='seraphine': lines += [msg('쓰러져도 조사 기록은 사라지지 않아요. 여기서 치료와 식량을 받아 가세요.','white'),buttons([('치료와 식량',13)])]
 elif id=='noah': lines += [msg('네 지역 조사, 봉인의 진실, 세 전선을 통해 연구가 단계적으로 열립니다. 지역 봉인은 누구나 자신의 조사 기록을 완성해야 합니다.','white'),'function fantasia:status','execute if entity @s[tag=fa_modded] run tellraw @s '+js({'text':'[ 마법 연구·주문서 받기 ]','color':'aqua','clickEvent':{'action':'run_command','value':'/fantasia_magic'}})]
 elif area in regions:
  hints={'mine':'광산의 마물들을 쓰러뜨린 다음 서쪽 광부를 구하고 동쪽 화염핵을 회수하세요.','canal':'수로 흐름은 동쪽 → 서쪽 → 중앙 순서입니다. 세 수문을 조절한 뒤 경비대를 쓰러뜨리세요.','forest':'서쪽 뿌리 → 중앙 정화석 → 동쪽 꽃 순서로 정화한 뒤 숲의 마물을 물리치세요.','storm':'서쪽 장치를 켠 뒤 20초 안에 동쪽 장치와 중앙 집전기에 도착해 누르세요. 그다음 폭풍 경비대를 쓰러뜨리세요.'}
  lines += [msg(hints[area],'white'),buttons([('실전 도전',20+regions.index(area))])]
 elif area=='capital': lines += [msg('방어선 안에서 세 차례의 습격을 막아 주세요. 전원이 이탈하거나 쓰러지면 다시 시작할 수 있습니다.','white'),buttons([('방어전 시작',30)])]
 elif area=='archive': lines += [msg('서쪽 옛 기록, 동쪽 실험 기록, 중앙 교수의 편지를 읽으세요. 그 후 저에게 보고하면 봉인의 진실을 알려드리겠습니다.','white'),buttons([('조사 보고',31)])]
 elif area in fronts: lines += [msg('전선의 정예군을 격퇴하고 봉인 장치를 확보해 주세요. 세 전선이 모두 안정되어야 왕좌로 가는 길이 열립니다.','white'),buttons([('전선 전투 시작',40+fronts.index(area))])]
 elif area=='castle': lines += [msg('벨카리온은 세 단계로 싸운다. 첫 육체를 쓰러뜨리고 서쪽과 동쪽 봉인석을 작동한 다음 폭주한 왕과 호위병을 쓰러뜨려라.','white'),buttons([('왕좌의 문 열기',50)]),'execute if score @s fa_stage matches 6.. run function fantasia:ending/menu']
 lines += [buttons([('현재 목표',2),('아카데미 귀환',1)])]
 links=[{'text':'[ 대화 ] ','color':'yellow','clickEvent':{'action':'run_command','value':f'/fantasia_npc {id} talk'}},{'text':'[ 선물 ] ','color':'light_purple','clickEvent':{'action':'run_command','value':f'/fantasia_npc {id} gift'}},{'text':'[ 내 정보 ]','color':'white','clickEvent':{'action':'run_command','value':'/fantasia_stats'}}]
 lines += ['execute if entity @s[tag=fa_modded] run tellraw @s '+js(links)]
 fun(f'npc/{id}',lines)
# World interaction stations, one advancement per station makes event dispatch unambiguous.
stations=[]
def station(id,area,dx,dz,label,fn):
 cx,cz=areas[area];x=cx+dx;z=cz+dz
 stations.append((id,x,z,fn))
 spawn.append(f'summon minecraft:interaction {x} 65 {z} {{Tags:["fa_station","fa_station_{id}"],width:1.8f,height:2.0f,response:1b}}')
 spawn.append(f'summon minecraft:text_display {x} 67.2 {z} '+ '{Tags:["fa_label"],billboard:"center",background:1073741824,text:'+json.dumps(js({'text':label,'color':'aqua'}),ensure_ascii=False)+'}')
 write(f'data/fantasia/advancement/station/{id}.json',js({'criteria':{'use':{'trigger':'minecraft:player_interacted_with_entity','conditions':{'entity':{'type':'minecraft:interaction','nbt':'{Tags:["fa_station_'+id+'"]}'}}}},'rewards':{'function':f'fantasia:station/{id}'}}))
 fun(f'station/{id}',[f'advancement revoke @s only fantasia:station/{id}',f'execute if dimension fantasia:campaign positioned {x} 65 {z} if entity @s[distance=..5] run function fantasia:{fn}'])
station('miner','mine',-8,0,'구조를 기다리는 광부','puzzle/miner')
station('fire_core','mine',8,0,'화염 마력핵','puzzle/fire_core')
for area in ['canal','forest','storm']:
 for side,dx,dz in [('west',-8,0),('east',8,0),('center',0,-5)]:station(area+'_'+side,area,dx,dz,{'west':'서쪽','east':'동쪽','center':'중앙'}[side]+' · '+{'canal':'수문','forest':'정화석','storm':'집전기'}[area],f'puzzle/{area}_{side}')
for side,dx,dz in [('west',-8,0),('east',8,0),('center',0,-5)]:station('archive_'+side,'archive',dx,dz,{'west':'옛 연맹의 기록','east':'마력 실험 기록','center':'베른하르트의 편지'}[side],f'puzzle/archive_{side}')
station('seal_west','castle',-10,15,'서쪽 봉인석 · 붕괴 단계에 가동','puzzle/seal_west')
station('seal_east','castle',10,15,'동쪽 봉인석 · 붕괴 단계에 가동','puzzle/seal_east')
# Entity summons require loaded chunks. Retain tickets until each NPC/station
# chunk is ticking, then replace actors and release only these setup tickets.
actor_chunks=sorted({(x//16,z//16) for _,x,z,_ in stations}|{(x//16,z//16) for _,x,z,_ in npcs.values()})
fun('npc/load',['scoreboard players set #npcs fa_world 2']+[f'execute in fantasia:campaign run forceload add {x*16} {z*16}' for x,z in actor_chunks]+['schedule function fantasia:npc/wait 10t replace'])
fun('npc/wait',['scoreboard players set #actor_chunks fa_world 0']+[f'execute in fantasia:campaign if loaded {x*16} 65 {z*16} run scoreboard players add #actor_chunks fa_world 1' for x,z in actor_chunks]+[f'execute unless score #actor_chunks fa_world matches {len(actor_chunks)} run schedule function fantasia:npc/wait 10t replace',f'execute if score #actor_chunks fa_world matches {len(actor_chunks)} in fantasia:campaign run function fantasia:npc/spawn'])
fun('npc/spawn',spawn+['team join fa_npcs @e[tag=fa_npc]']+[f'forceload remove {x*16} {z*16}' for x,z in actor_chunks]+['scoreboard players set #npcs fa_world 1'])
# Action validation never trusts a displayed menu or stale trigger number.
actions=['scoreboard players set @s fa_ok 0']
def action(value,npc,condition,fn):
 x,z=npcs[npc][1:3]
 actions.append(f'execute if score @s fa_action matches {value} if dimension fantasia:campaign positioned {x} 65 {z} if entity @s[distance=..7] {condition}run function fantasia:{fn}')
actions += ['execute if score @s fa_action matches 1 if dimension fantasia:campaign if entity @e[tag=fa_npc,distance=..7,limit=1] run function fantasia:home','execute if score @s fa_action matches 2 run function fantasia:status','execute if score @s fa_action matches 2 run scoreboard players set @s fa_ok 1']
action(11,'kyle','if score @s fa_gear matches 0 ','gear')
action(12,'kyle','if score @s fa_stage matches 0 if score @s fa_gear matches 1.. if entity @s[advancements={fantasia_research:exam/complete=true}] ','encounter/tutorial/request')
action(13,'seraphine','if score @s fa_heal matches 0 ','heal')
action(14,'kyle','if score @s fa_supplies matches 0 if entity @s[advancements={fantasia_research:exam/complete=true}] ','supplies')
for i,area in enumerate(regions):action(20+i,{'mine':'irina','canal':'riana','forest':'rowen','storm':'theo'}[area],f'if score @s fa_stage matches 1 if score @s fa_{area} matches '+('0' if area=='mine' else '3')+' ',f'encounter/{area}/request')
action(30,'edric','if score @s fa_stage matches 2 ','encounter/defense/request')
action(31,'rachel','if score @s fa_stage matches 3 if score @s fa_archive matches 3 ','milestone/truth')
for i,area in enumerate(fronts):action(40+i,{'north':'elena','east':'claude','south':'bernard'}[area],f'if score @s fa_stage matches 4 if score @s fa_{area} matches 0 ',f'encounter/{area}/request')
action(50,'headmaster','if score @s fa_stage matches 5 ','encounter/castle/request')
travel=[('mine',1),('canal',1),('forest',1),('storm',1),('capital',2),('archive',3),('north',4),('east',4),('south',4),('castle',5)]
for i,(area,stage) in enumerate(travel):
 action(101+i,'adeline',f'if score @s fa_stage matches {stage}.. unless entity @s[tag=fa_fighting] ',f'travel/{area}')
 x,z=areas[area]; zz=z-20
 fun(f'travel/{area}',[f'execute in fantasia:campaign run tp @s {x} 65 {zz} 0 0','scoreboard players set @s fa_ok 1',msg('주변 안내 NPC를 우클릭하세요. 공중 글자가 있는 장치는 가까이서 우클릭할 수 있습니다.','white')])
for v in range(61,65):action(v,'headmaster','if score @s fa_stage matches 6 ',f'ending/{v-60}')
actions += ['execute if score @s fa_ok matches 0 run '+msg('지금은 사용할 수 없는 선택지입니다. 해당 NPC에게 가까이 가서 현재 조건과 목표를 확인하세요.','yellow'),'scoreboard players set @s fa_action 0','scoreboard players enable @s fa_action']
fun('action',actions)
fun('gear',['scoreboard players set @s fa_gear 1','scoreboard players set @s fa_ok 1','give @s minecraft:iron_sword','give @s minecraft:shield','give @s minecraft:bow','give @s minecraft:arrow 64','give @s minecraft:iron_helmet','give @s minecraft:iron_chestplate','give @s minecraft:iron_leggings','give @s minecraft:iron_boots','give @s minecraft:cooked_beef 32',msg('훈련 장비를 지급했습니다. 갑옷과 방패를 장착하고 입학 검사를 마친 다음 훈련을 시작하세요.','green')])
fun('heal',['scoreboard players set @s fa_ok 1','scoreboard players set @s fa_heal 30','effect give @s minecraft:instant_health 1 5 true','effect give @s minecraft:saturation 1 3 true','give @s minecraft:cooked_beef 16','give @s minecraft:arrow 32',msg('회복 완료. 다음 보급은 30초 뒤에 받을 수 있습니다.','green')])
fun('supplies',['scoreboard players set @s fa_ok 1','scoreboard players set @s fa_supplies 180','give @s minecraft:lapis_lazuli 16','give @s minecraft:book 3','give @s minecraft:blaze_powder 8','give @s minecraft:nether_wart 8','give @s minecraft:sugar 8','give @s minecraft:potion[minecraft:potion_contents={potion:"minecraft:water"}] 3','experience add @s 5 levels',msg('북서쪽 마법부여실: 청금석과 경험치로 책을 마법부여하세요. 북동쪽 연금실: 물병 → 네더 사마귀 → 설탕 순서로 양조하세요. 동쪽 표적은 활로 중심을 맞히세요.','white')])
# Individual region puzzles.
fun('puzzle/miner',['execute unless score @s fa_stage matches 1 run return 0','execute unless score @s fa_mine matches 1 run return 0','scoreboard players set @s fa_mine 2',msg('광부를 구출했다. “교수님은 동쪽 화염핵에서 검은 표식을 보셨어요. 그 뒤로 사라지셨죠.”','white')])
fun('puzzle/fire_core',['execute unless score @s fa_stage matches 1 run return 0','execute unless score @s fa_mine matches 2 run return 0','function fantasia:milestone/mine'])
orders={'canal':['east','west','center'],'forest':['west','center','east'],'storm':['west','east','center'],'archive':['west','east','center']}
for area,order in orders.items():
 for idx,side in enumerate(order):
  obj='fa_'+area; stage=3 if area=='archive' else 1
  lines=[f'execute unless score @s fa_stage matches {stage} run return 0',f'execute unless score @s {obj} matches {idx} run return 0',f'scoreboard players set @s {obj} {idx+1}']
  if area=='storm' and idx==0:lines+=['scoreboard players set @s fa_timer 20',msg('20초 안에 동쪽 장치 → 중앙 집전기 순서로 가동하세요.','yellow')]
  elif area=='archive':
   lines += [msg(['연맹은 마왕을 봉인했지만 그의 마력을 아카데미로 흘려보냈다.','세대에 걸친 마력 추출로 봉인핵이 손상되었다. 교단은 균열을 넓히고 있다.','“마력을 추출하지 않아도 봉인은 재구축할 수 있다. 세 전선의 공명석을 모아 달라.” — 베른하르트'][idx],'white')]
  else:lines += [msg(f'장치 {idx+1}/3 가동. '+('안내 NPC에게 실전 도전을 요청하세요.' if idx==2 else '다음 장치로 이동하세요.'),'green')]
  fun(f'puzzle/{area}_{side}',lines)
fun('puzzle/storm_timeout',['scoreboard players set @s fa_storm 0',msg('시간이 지났습니다. 서쪽 집전기에서 다시 시작할 수 있습니다.','yellow')])
# Per-region reward functions: each is called only from a checked encounter/puzzle path.
for area in regions+fronts:
 lines=[f'scoreboard players set @s fa_{area} 5',reward(area),f'tag @s remove fa_in_{area}','tag @s remove fa_fighting',msg({'mine':'화염핵 회수와 광부 구출 완료','canal':'수로 복구 완료','forest':'숲의 균열 봉합 완료','storm':'낙뢰 평원 안정화 완료','north':'북부 전선 확보','east':'동부 전선 확보','south':'남부 전선 확보'}[area]+'! 아카데미에서 다음 목적지를 선택하세요.','green')]
 school={'mine':'fire','canal':'ice','forest':'nature','storm':'lightning','north':'void','east':'holy','south':'blood'}[area]
 lines += [grant(f'{school}_tier_1'),grant(f'{school}_tier_2'),'give @s minecraft:golden_apple 2','experience add @s 5 levels']
 if area=='mine':lines += [grant(x) for x in ['course/field/nether_entry','course/field/blaze_combat','course/field/blaze_sample','course/dungeon/ignited_revenant']]
 if area=='canal':lines += [grant('course/dungeon/ender_golem')]
 fun(f'milestone/{area}',lines)
fun('milestone/intro',['scoreboard players set @s fa_stage 1',reward('intro'),grant('course/foundation/combat'),'tag @s remove fa_in_tutorial','tag @s remove fa_fighting',msg('견습 마도사 임명. 이제 아델린에게 돌아가 네 지역을 원하는 순서로 조사하세요.','green')])
fun('milestone/regions',['scoreboard players set @s fa_stage 2',reward('regions'),msg('네 마력핵의 표식이 하나로 이어졌다. 아카데미에 경보가 울린다! 아델린을 통해 수도 방어전으로 이동하세요.','red')])
fun('milestone/defense',['scoreboard players set @s fa_stage 3',reward('defense'),'tag @s remove fa_in_defense','tag @s remove fa_fighting',msg('세 차례의 습격을 막았다. 적의 문장에서 교수의 연구 번호가 발견됐다. 봉인서고의 라헬을 찾아가세요.','green')])
fun('milestone/truth',['scoreboard players set @s fa_ok 1','scoreboard players set @s fa_stage 4',reward('truth'),grant('course/advanced/amethyst'),'give @s minecraft:amethyst_shard 16','give @s minecraft:diamond_sword','give @s minecraft:diamond_chestplate','give @s minecraft:diamond_leggings',grant('ender_tier_1'),grant('evocation_tier_1'),msg('진실: 아카데미는 마왕의 힘을 이용해 왔다. 베른하르트는 봉인 재구축법을 찾았지만 납치되었다. 세 전선의 공명석을 확보하자.','light_purple')])
fun('milestone/fronts',['scoreboard players set @s fa_stage 5',reward('fronts'),grant('course/advanced/nether_star'),'give @s minecraft:nether_star','give @s minecraft:diamond_helmet','give @s minecraft:diamond_boots','give @s minecraft:golden_apple 8','give @s minecraft:arrow 64']+[grant(f'{s}_tier_{t}') for s in ['fire','ice','nature','lightning','holy','ender','blood','evocation','void'] for t in [1,2,3]]+[msg('세 공명석이 완성됐다. 구출된 베른하르트의 기록으로 왕좌의 문을 열 수 있다. 아델린에게 마왕성 이동을 요청하세요.','gold')])
fun('milestone/castle',['scoreboard players set @s fa_stage 6',reward('castle'),grant('course/graduation/capstone'),grant('course/advanced/end_crystal'),'give @s minecraft:end_crystal','tag @s remove fa_in_castle','tag @s remove fa_fighting',msg('벨카리온의 폭주가 멈췄다. 마지막 선택은 당신에게 달렸다. 입구의 헤론에게 돌아가 결말을 선택하세요.','gold')])
# Encounters share enemies but only enrolled, nearby surviving players receive completion.
settings={
 'tutorial':('hub',0,22,0,3),'mine':('mine',160,5,1,4),'canal':('canal',0,165,1,4),'forest':('forest',-160,5,1,4),'storm':('storm',0,-155,1,4),'defense':('capital',-160,165,2,4),'north':('north',-160,-155,4,5),'east':('east',160,-155,4,5),'south':('south',320,5,4,5),'castle':('castle',320,175,5,1)}
for eid,(area,x,z,stage,total) in settings.items():
 extra=''
 if eid in regions:extra=f',fa_{eid}='+('0' if eid=='mine' else '3')
 if eid in fronts:extra=f',fa_{eid}=0'
 eligible=f'@a[distance=..12,tag=!fa_fighting,scores={{fa_stage={stage}{extra}}}]'
 if eid=='tutorial':eligible=f'@a[distance=..12,tag=!fa_fighting,scores={{fa_stage=0,fa_gear=1..}},advancements={{fantasia_research:exam/complete=true}}]'
 fun(f'encounter/{eid}/request',['scoreboard players set @s fa_ok 1',f'execute if score #{eid} fa_world matches 1 run '+msg('이미 전투가 진행 중입니다. 이 도전이 끝나거나 전원이 귀환한 뒤 다시 요청하세요.','yellow'),f'execute unless score #{eid} fa_world matches 1 run function fantasia:encounter/{eid}/start'])
 start=[f'kill @e[tag=fa_enemy_{eid}]',f'scoreboard players set #{eid} fa_world 1',f'scoreboard players set #kills_{eid} fa_world 0',f'scoreboard players set #time_{eid} fa_world 0',f'scoreboard players set #wave_{eid} fa_world 1',f'execute as {eligible} run tag @s add fa_in_{eid}',f'tag @a[tag=fa_in_{eid}] add fa_fighting',f'execute as @a[tag=fa_in_{eid}] in fantasia:campaign run tp @s {x} 65 {z-6}',f'execute as @a[tag=fa_in_{eid}] run effect give @s minecraft:resistance 5 2 true',f'execute as @a[tag=fa_in_{eid}] run '+msg('도전 시작! 아레나에서 적을 모두 쓰러뜨리세요. 사망·이탈 시 보상이 지급되지 않으며, 전원 이탈 시 도전이 초기화됩니다.','yellow'),f'function fantasia:encounter/{eid}/spawn']
 if eid=='castle':start+=['scoreboard players set #seal_west fa_world 0','scoreboard players set #seal_east fa_world 0','bossbar set fantasia:belkarion players @a[tag=fa_in_castle]','bossbar set fantasia:belkarion value 3','bossbar set fantasia:belkarion visible true']
 fun(f'encounter/{eid}/start',start)
 enemy_types={'tutorial':['zombie','skeleton','spider'],'mine':['husk','husk','skeleton','spider'],'canal':['stray','stray','zombie','spider'],'forest':['spider','spider','zombie','skeleton'],'storm':['skeleton','skeleton','husk','spider'],'defense':['pillager','pillager','vindicator','zombie'],'north':['stray','stray','vindicator','skeleton','husk'],'east':['spider','spider','vindicator','pillager','zombie'],'south':['husk','husk','vindicator','skeleton','pillager'],'castle':['skeleton']}[eid]
 spawn_lines=[f'scoreboard players set #kills_{eid} fa_world 0',f'scoreboard players set #need_{eid} fa_world {len(enemy_types)}']
 for n,typ in enumerate(enemy_types):
  px=x+[-4,4,0,-3,3][n];pz=z+[2,2,5,-3,-3][n]
  hp=100 if eid=='castle' else (18 if eid=='tutorial' else 24 if eid in regions else 28)
  nm='벨카리온 · 첫 육체' if eid=='castle' else '훈련 잔상' if eid=='tutorial' else '균열의 수호병'
  weapon='bow' if typ in ['skeleton','stray'] else 'crossbow' if typ=='pillager' else 'iron_axe' if typ=='vindicator' else 'stone_sword'
  nbt='{Tags:["fa_enemy","fa_enemy_'+eid+'"],PersistenceRequired:1b,CanPickUpLoot:0b,CustomName:'+json.dumps(js({'text':nm,'color':'dark_purple'}),ensure_ascii=False)+',CustomNameVisible:1b,Health:'+str(hp)+'.0f,Attributes:[{Name:"minecraft:generic.max_health",Base:'+str(hp)+'.0d}],HandItems:[{id:"minecraft:'+weapon+'",count:1},{}],ArmorItems:[{},{},{},{id:"minecraft:iron_helmet",count:1}],HandDropChances:[0.0f,0.0f],ArmorDropChances:[0.0f,0.0f,0.0f,0.0f]}'
  spawn_lines += [f'summon minecraft:{typ} {px} 65 {pz} {nbt}']
 fun(f'encounter/{eid}/spawn',spawn_lines)
 write(f'data/fantasia/advancement/kill/{eid}.json',js({'criteria':{'kill':{'trigger':'minecraft:player_killed_entity','conditions':{'entity':{'nbt':'{Tags:["fa_enemy_'+eid+'"]}'}}}},'rewards':{'function':f'fantasia:encounter/{eid}/kill'}}))
 fun(f'encounter/{eid}/kill',[f'advancement revoke @s only fantasia:kill/{eid}',f'execute if dimension fantasia:campaign if entity @s[tag=fa_in_{eid}] if score #{eid} fa_world matches 1 run scoreboard players add #kills_{eid} fa_world 1'])
 tick=[f'scoreboard players add #time_{eid} fa_world 1',f'execute as @a[tag=fa_in_{eid}] at @s unless dimension fantasia:campaign run function fantasia:encounter/{eid}/leave',f'execute positioned {x} 65 {z} as @a[tag=fa_in_{eid},distance=40..] run function fantasia:encounter/{eid}/leave',f'execute unless entity @a[tag=fa_in_{eid}] run function fantasia:encounter/{eid}/abort',f'execute if score #time_{eid} fa_world matches 600.. run function fantasia:encounter/{eid}/abort',f'execute if score #{eid} fa_world matches 1 if score #kills_{eid} fa_world >= #need_{eid} fa_world run function fantasia:encounter/{eid}/win']
 fun(f'encounter/{eid}/tick',tick)
 fun(f'encounter/{eid}/leave',[f'tag @s remove fa_in_{eid}','tag @s remove fa_fighting'])
 fun(f'encounter/{eid}/abort',[f'execute as @a[tag=fa_in_{eid}] run '+msg('도전이 초기화되었습니다. NPC에게 다시 요청할 수 있습니다.','yellow'),f'tag @a[tag=fa_in_{eid}] remove fa_fighting',f'tag @a remove fa_in_{eid}',f'kill @e[tag=fa_enemy_{eid}]',f'scoreboard players set #{eid} fa_world 0']+(['bossbar set fantasia:belkarion visible false'] if eid=='castle' else []))
 if eid=='defense':
  fun('encounter/defense/win',['execute if score #wave_defense fa_world matches 3 run function fantasia:encounter/defense/finish','execute if score #defense fa_world matches 1 if score #wave_defense fa_world matches 1..2 run function fantasia:encounter/defense/next'])
  fun('encounter/defense/next',['scoreboard players add #wave_defense fa_world 1','execute as @a[tag=fa_in_defense] run effect give @s minecraft:instant_health 1 1 true','execute as @a[tag=fa_in_defense] run '+msg('다음 습격이 밀려옵니다! 방어선을 지켜 주세요.','red'),'function fantasia:encounter/defense/spawn'])
  fun('encounter/defense/finish',['scoreboard players set #defense fa_world 0','execute as @a[tag=fa_in_defense] run function fantasia:milestone/defense'])
 elif eid=='castle':
  fun('encounter/castle/win',['execute if score #wave_castle fa_world matches 1 run function fantasia:encounter/castle/seals','execute if score #wave_castle fa_world matches 3 run function fantasia:encounter/castle/finish'])
  fun('encounter/castle/seals',['scoreboard players set #wave_castle fa_world 2','scoreboard players set #kills_castle fa_world 0','scoreboard players set #need_castle fa_world 999','bossbar set fantasia:belkarion value 2','execute as @a[tag=fa_in_castle] run '+msg('봉인 붕괴! 서쪽과 동쪽 봉인석을 가까이서 우클릭해 안정화하세요.','light_purple'),'execute as @a[tag=fa_in_castle] run effect give @s minecraft:regeneration 6 1 true'])
  fun('encounter/castle/finish',['scoreboard players set #castle fa_world 0','bossbar set fantasia:belkarion visible false','execute as @a[tag=fa_in_castle] run function fantasia:milestone/castle'])
 elif eid=='mine':fun(f'encounter/{eid}/win',[f'scoreboard players set #{eid} fa_world 0',f'execute as @a[tag=fa_in_{eid}] run scoreboard players set @s fa_mine 1',f'execute as @a[tag=fa_in_{eid}] run '+msg('광산을 확보했습니다. 서쪽 광부를 구출한 뒤 동쪽 화염핵을 회수하세요.','green'),f'tag @a[tag=fa_in_{eid}] remove fa_fighting',f'tag @a remove fa_in_{eid}'])
 else:fun(f'encounter/{eid}/win',[f'scoreboard players set #{eid} fa_world 0',f'execute as @a[tag=fa_in_{eid}] run function fantasia:milestone/'+('intro' if eid=='tutorial' else eid)])
# Final seals are shared only by actual current participants.
for side in ['west','east']:
 fun('puzzle/seal_'+side,['execute unless entity @s[tag=fa_in_castle] run return 0','execute unless score #castle fa_world matches 1 run return 0','execute unless score #wave_castle fa_world matches 2 run return 0',f'scoreboard players set #seal_{side} fa_world 1',msg(('서쪽' if side=='west' else '동쪽')+' 봉인석 안정화.','green'),'execute if score #seal_west fa_world matches 1 if score #seal_east fa_world matches 1 run function fantasia:encounter/castle/final'])
fun('encounter/castle/final',['scoreboard players set #wave_castle fa_world 3','scoreboard players set #kills_castle fa_world 0','scoreboard players set #need_castle fa_world 3','bossbar set fantasia:belkarion value 1','summon minecraft:husk 320 65 180 {Tags:["fa_enemy","fa_enemy_castle"],PersistenceRequired:1b,Health:140.0f,Attributes:[{Name:"minecraft:generic.max_health",Base:140.0d},{Name:"minecraft:generic.movement_speed",Base:0.27d}],CustomName:\'{"text":"벨카리온 · 최후의 폭주","color":"dark_red"}\',CustomNameVisible:1b,HandItems:[{id:"minecraft:iron_axe",count:1},{}],ArmorItems:[{},{},{id:"minecraft:iron_chestplate",count:1},{id:"minecraft:iron_helmet",count:1}],HandDropChances:[0.0f,0.0f],ArmorDropChances:[0.0f,0.0f,0.0f,0.0f]}','summon minecraft:skeleton 314 65 176 {Tags:["fa_enemy","fa_enemy_castle"],PersistenceRequired:1b,HandItems:[{id:"minecraft:bow",count:1},{}],ArmorItems:[{},{},{},{id:"minecraft:iron_helmet",count:1}]}','summon minecraft:skeleton 326 65 176 {Tags:["fa_enemy","fa_enemy_castle"],PersistenceRequired:1b,HandItems:[{id:"minecraft:bow",count:1},{}],ArmorItems:[{},{},{},{id:"minecraft:iron_helmet",count:1}]}','execute as @a[tag=fa_in_castle] run '+msg('최후의 폭주! 왕과 두 호위병을 모두 쓰러뜨리세요.','red')])
# Ending selection is one-time, player-scoped, and made at Headmaster.
fun('ending/menu',[msg('결말을 선택하세요. 선택은 개인 기록에 영구 저장됩니다.','yellow'),buttons([('봉인 재구축',61),('마력 소멸',62),('힘 통제',63),('진실 공개',64)])])
endings={1:('봉인 재구축','네 마력핵과 세 공명석이 새로운 봉인이 되었다. 아카데미는 더 이상 마왕의 힘을 빌리지 않고, 학생들은 스스로의 마법을 연구한다.'),2:('마력 소멸','당신은 균열 너머의 힘을 완전히 끊었다. 아카데미의 화려한 마력등은 꺼졌지만, 사람들은 처음으로 두려움 없는 밤을 맞았다.'),3:('힘 통제','당신은 마왕의 힘을 공동 감시 아래 두었다. 연구에는 엄격한 한계가 생겼고, 사람들은 같은 잘못을 반복하지 않겠다고 맹세했다.'),4:('진실 공개','교수의 편지와 실험 기록을 세상에 공개했다. 옛 영웅들의 그림자까지 마주한 아카데미는, 힘을 얻는 법보다 힘을 책임지는 법을 가르치기 시작했다.')}
for num,(name,desc) in endings.items():
 fun(f'ending/{num}',['scoreboard players set @s fa_ok 1','scoreboard players set @s fa_stage 7',f'scoreboard players set @s fa_ending {num}',reward('ending'),'title @s times 20 100 30','title @s title '+js({'text':name,'color':'gold'}),'title @s subtitle '+js({'text':'Fantasia: 균열의 왕 · 캠페인 완료','color':'white'}),msg(desc,'white'),msg('캠페인 완료. NPC 인연과 마법 연구를 계속하거나 아카데미를 자유롭게 탐험하세요.','green')])
status=[msg('══ Fantasia · 현재 목표 ══')]
for st,text in enumerate(['입학 검사 완료 → 카일에게 장비 수령 → 기초 훈련 통과','네 지역을 조사하세요. 광산/수로/숲/평원은 원하는 순서로 진행합니다.','수도 방어전에서 세 차례의 습격을 막으세요.','봉인서고의 세 기록을 읽고 라헬에게 보고하세요.','북부·동부·남부 전선의 공명석을 확보하세요.','마왕성에서 벨카리온의 세 전투 단계를 돌파하세요.','헤론에게 돌아가 결말을 선택하세요.','캠페인 완료. 자유 연구와 인연 활동을 계속할 수 있습니다.']):status.append(f'execute if score @s fa_stage matches {st} run '+msg(text,'white'))
for area,name in [('mine','광산'),('canal','수로'),('forest','숲'),('storm','평원'),('north','북부'),('east','동부'),('south','남부')]:status.append(f'execute if score @s fa_{area} matches 5 run '+msg(name+' ✓','green'))
fun('status',status)
print('Generated campaign functions:',len(list(FN.rglob('*.mcfunction'))))
