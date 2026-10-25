const FANTASIA_NPCS = {
 adeline:{name:'아델린 로아',fav:'minecraft:amethyst_shard',relation:true},
 kyle:{name:'카일 베른',fav:'minecraft:iron_ingot',relation:true},
 seraphine:{name:'세라핀 루메르',fav:'minecraft:glowstone_dust',relation:true},
 irina:{name:'이리나 벨',fav:'minecraft:blaze_powder',relation:true},
 noah:{name:'노아 크레이',fav:'minecraft:book',relation:true},
 riana:{name:'리아나 펠',fav:'minecraft:compass',relation:true},
 claude:{name:'클라우드 레인',fav:'minecraft:golden_apple',relation:true},
 headmaster:{name:'헤론 아슈',fav:'',relation:false},
 orphen:{name:'오르펜',fav:'',relation:false},
 milo:{name:'마일로',fav:'',relation:false},
 edric:{name:'에드릭',fav:'',relation:false},
 rachel:{name:'라헬 모르',fav:'',relation:false},
 bernard:{name:'베른하르트',fav:'',relation:false},
 rowen:{name:'로웬',fav:'',relation:false},
 theo:{name:'테오',fav:'',relation:false},
 elena:{name:'엘레나',fav:'',relation:false}
}

// Campaign progress is owned by the fantasia datapack (fa_stage), never a second JS state machine.
const STORY_NAMES = ['입학과 첫 훈련','네 개의 흔적','아카데미 방어전','봉인의 진실','세 전선','마왕성 결전','엔딩 선택','캠페인 완료']
const BOND_EPILOGUES = {
 adeline:'모든 여정이 끝나도 이곳에 당신의 자리를 남겨 둘게요.',
 kyle:'넌 이제 내 훈련 상대다. 다음 세대에게도 네가 배운 것을 전해 줘.',
 seraphine:'우리가 지켜낸 사람들의 내일이 당신의 마법보다 더 오래 남을 거예요.',
 irina:'위험한 연구일수록 혼자 하지 않겠어요. 다음 탐사에도 함께 가요.',
 noah:'새 봉인 기록의 첫 장에 당신과 동료들의 이름을 적겠습니다.',
 riana:'지도에 없는 길도 당신과 함께라면 찾아갈 수 있겠어요.',
 claude:'한때는 혼자 살아남는 것만 생각했지. 이제 함께 돌아갈 곳이 생겼어.'
}
function pc(p){ return p.persistentData }
function pn(p){ return p.getGameProfile().getName() }
function sc(p,key){ return pc(p).getInt(key) }
function setsc(p,key,v){ pc(p).putInt(key,v) }
function affKey(id){ return `fantasia_affection_${id}` }
function getAff(p,id){ return Math.max(0,Math.min(100,sc(p,affKey(id)))) }
function tier(v){
 if(v>=80) return '인연'
 if(v>=60) return '신뢰'
 if(v>=40) return '친구'
 if(v>=20) return '친숙'
 return '낯선 사이'
}
function campaignPlayerCommand(e){
 if(e.player) return true
 e.respond('이 명령은 게임에 접속한 플레이어가 사용해야 합니다.')
 return false
}
function nearNpc(server,p,id){
 // Commands are public for clickable UI, so every state-changing action validates location.
 // KubeJS 2101 runCommandSilent returns void, never a Brigadier result.
 return server.getCommands().getDispatcher().execute(
  `execute as ${pn(p)} at @s if dimension fantasia:campaign if entity @e[tag=fa_npc_${id},distance=..6,limit=1]`,
  server.createCommandSourceStack().withSuppressedOutput())>0
}
function syncAff(server,p,id){
 server.runCommandSilent(`scoreboard players set ${pn(p)} fa_b_${id} ${getAff(p,id)}`)
}
function campaignStage(server,p){
 const board=server.getScoreboard(), objective=board.getObjective('fa_stage')
 if(objective===null) return 0
 const score=board.getPlayerScoreInfo(p,objective)
 return score===null?0:Math.max(0,Math.min(7,score.value()))
}
function npcTalk(server,p,id){
 const npc=FANTASIA_NPCS[id]
 if(!npc){ p.tell('§c알 수 없는 NPC입니다.'); return }
 if(!nearNpc(server,p,id)){ p.tell('§e해당 NPC 가까이에서 대화해 주세요.'); return }
 const st=campaignStage(server,p)
 const lines={
  adeline:st<2?'네 지역의 균열을 조사하고 돌아와 주세요. 현지 안내인의 부탁을 따라가면 봉인의 흔적을 찾을 수 있어요.':'우리가 지켜야 할 것은 연구 성과가 아니라 이곳의 사람들이에요.',
  kyle:'전투에서는 방패와 간격이 중요하다. 장비를 받았다면 준비를 마친 뒤 출발해.',
  seraphine:'치료소는 언제든 열려 있어요. 부상을 숨기지 말고 동료와 함께 돌아와 주세요.',
  irina:'광산의 화염을 조사하고 수호병을 제압해 주세요. 용암 가까이에서는 발밑을 보세요.',
  noah:st<3?'네 지역의 봉인을 먼저 확인해 주세요. 아직 봉인서고에 들어갈 허가가 없습니다.':'봉인에는 대가가 있었습니다. 서고의 기록을 직접 읽고 결정을 내려 주세요.',
  riana:'얼어붙은 수로의 장치를 차례대로 살펴보세요. 서두르다 물에 빠지지 않도록 해요.',
  claude:'먼저 장비를 정비하고 전선으로 나가자. 살아 돌아와서 다음 이야기를 들려줘.',
  headmaster:'지금까지의 선택이 이 왕좌 앞까지 당신을 이끌었습니다. 마지막 결정은 당신의 몫입니다.',
  orphen:'연구에는 단계가 있습니다. 앞선 연구를 마친 뒤 다음 실습에 도전하세요.',
  milo:'보급품은 필요한 만큼 챙겨요. 모험을 계속할 수 있도록 준비하는 것도 실력이죠.',
  edric:'방어전은 시작한 사람들과 함께 진행된다. 전투 중 이탈했다면 재정비하고 다시 도전하게.',
  rachel:'오래된 기록과 실제 장치를 함께 확인하세요. 눈앞의 마력만 믿어서는 안 됩니다.',
  bernard:'날 구하러 와 줘서 고맙네. 내 연구가 남긴 상처를 함께 바로잡아 주게.',
  rowen:'숲은 전쟁터가 아니었어요. 오염원을 제거하고 균열을 닫아 주세요.',
  theo:'낙뢰 장치를 가동하기 전 순서를 확인하세요. 안전한 길을 따라 움직이세요.',
  elena:'북부 전선은 추위보다 고립이 위험해요. 준비를 마치고 함께 출발해요.'
 }
 let line=lines[id]
 if(npc.relation && getAff(p,id)>=80 && st>=7) line=BOND_EPILOGUES[id]
 p.tell(`§6[${npc.name}] §f${line}`)
 if(npc.relation) p.tell(`§7호감도: §d${getAff(p,id)} §7(${tier(getAff(p,id))})`)
}
function npcGift(server,p,id){
 const npc=FANTASIA_NPCS[id]
 if(!npc || !npc.relation){ p.tell('§7이 NPC에게는 호감도 선물 기능이 없습니다.'); return }
 if(!nearNpc(server,p,id)){ p.tell('§e선물할 NPC에게 가까이 다가가 주세요.'); return }
 const held=p.getMainHandItem()
 if(held.isEmpty() || String(held.id)==='minecraft:air'){
  p.tell('§e선물할 아이템을 주 손에 들어주세요.'); return
 }
 const before=getAff(p,id)
 if(before>=100){ p.tell('§d이미 가장 깊은 인연을 맺었습니다.'); return }
 const now=Number(server.overworld().getGameTime()), key=`fantasia_gift_time_${id}`
 const previous=Number(pc(p).getLong(key))
 if(pc(p).contains(key) && now>=previous && now-previous<600){
  p.tell('§e선물을 받은 뒤에는 30초 동안 이야기를 나눌 시간을 주세요.'); return
 }
 const gain=String(held.id)===npc.fav?5:1
 // Consume exactly the item in the hand, including its components; clear could remove another slot.
 held.shrink(1)
 p.sendInventoryUpdate()
 pc(p).putLong(key,now)
 setsc(p,affKey(id),Math.min(100,before+gain))
 syncAff(server,p,id)
 p.tell(`§d[인연] ${npc.name} 호감도 +${getAff(p,id)-before} §7(${getAff(p,id)}/100)`)
 ;[20,40,60,80].forEach(threshold=>{
  if(before<threshold && getAff(p,id)>=threshold){
   p.tell(`§6[인연] ${npc.name}와 ${tier(threshold)} 사이가 되었습니다.`)
   server.runCommandSilent(`tag ${pn(p)} add fantasia_bond_${id}_${threshold}`)
   if(threshold===80) server.runCommandSilent(`advancement grant ${pn(p)} only fantasia_research:bond/${id}`)
  }
 })
}
function fantasiaResetBonds(server,p){
 Object.keys(FANTASIA_NPCS).forEach(id=>{
  if(!FANTASIA_NPCS[id].relation) return
  setsc(p,affKey(id),0)
  pc(p).remove(`fantasia_gift_time_${id}`)
  syncAff(server,p,id)
  ;[20,40,60,80].forEach(t=>server.runCommandSilent(`tag ${pn(p)} remove fantasia_bond_${id}_${t}`))
 })
}
function storyInfo(server,p){
 server.runCommandSilent(`execute as ${pn(p)} at @s run function fantasia:status`)
}
ServerEvents.loaded(e=>{
 Object.keys(FANTASIA_NPCS).forEach(id=>{
  if(FANTASIA_NPCS[id].relation) e.server.runCommandSilent(`scoreboard objectives add fa_b_${id} dummy`)
 })
 e.server.runCommandSilent('scoreboard players set #kubejs fa_world 1')
})
PlayerEvents.loggedIn(e=>{
 e.server.runCommandSilent(`tag ${pn(e.player)} add fa_modded`)
 e.server.runCommandSilent(`execute as ${pn(e.player)} at @s if entity @s[tag=fa_joined] if score #ready fa_world matches 1 run function fantasia:recover`)
 Object.keys(FANTASIA_NPCS).forEach(id=>{
  if(FANTASIA_NPCS[id].relation){
   syncAff(e.server,e.player,id)
   if(getAff(e.player,id)>=80)e.server.runCommandSilent(`advancement grant ${pn(e.player)} only fantasia_research:bond/${id}`)
  }
 })
})
ServerEvents.basicCommand('fantasia_npc',e=>{
 if(!campaignPlayerCommand(e)) return
 const a=String(e.input||'').trim().split(/\s+/).filter(x=>x.length>0)
 if(a.length<1 || a.length>2){ e.player.tell('§eNPC를 우클릭하고 대화 항목을 선택하세요.'); return }
 const id=a[0], action=(a[1]||'talk').toLowerCase(), npc=FANTASIA_NPCS[id]
 if(!npc){ e.player.tell('§c알 수 없는 NPC입니다.'); return }
 if(action==='talk'){ npcTalk(e.server,e.player,id); return }
 if(action==='gift'){ npcGift(e.server,e.player,id); return }
 if(action==='status'){
  e.player.tell(`§6${npc.name}`)
  if(npc.relation) e.player.tell(`§d호감도 ${getAff(e.player,id)}/100 (${tier(getAff(e.player,id))})`)
  return
 }
 e.player.tell('§c사용 가능: talk, gift, status')
})
ServerEvents.basicCommand('fantasia_story',e=>{
 if(!campaignPlayerCommand(e)) return
 const input=String(e.input||'').trim()
 if(input===''||input==='status'){ storyInfo(e.server,e.player); return }
 e.player.tell('§e스토리는 실제 목표를 달성하면 자동으로 진행됩니다.')
})
ServerEvents.basicCommand('fantasia_bonds',e=>{
 if(!campaignPlayerCommand(e)) return
 e.player.tell('§6════ NPC 인연 ════')
 Object.keys(FANTASIA_NPCS).forEach(id=>{
  const n=FANTASIA_NPCS[id]
  if(n.relation) e.player.tell(`§f${n.name}: §d${getAff(e.player,id)}/100 §7(${tier(getAff(e.player,id))})`)
 })
})
