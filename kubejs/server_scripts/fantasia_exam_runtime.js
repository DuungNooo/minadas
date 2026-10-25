// Fantasia 1.1.0 — Minecraft 1.21.1 / KubeJS 2101. Persistent data is per player.
const SCHOOL_LABELS = {
  fire:'불', ice:'물/빙결', lightning:'전격', nature:'풀/자연',
  holy:'신성', ender:'엔더', blood:'혈마법', evocation:'소환/환술', void:'공허'
}
const WEAPON_LABELS = {
  sword:'검', greatsword:'대검', dagger:'단검', spear:'창/할버드',
  axe:'도끼', hammer:'망치/둔기', bow:'활', crossbow:'석궁',
  staff:'스태프', spellbook:'마법서', hybrid:'마검/하이브리드'
}
const STAT_KEYS = ['str','vit','agi','mag','mnd']
const SCHOOL_KEYS = ['fire','ice','lightning','nature','holy','ender','blood','evocation','void']
const WEAPON_KEYS = ['sword','greatsword','dagger','spear','axe','hammer','bow','crossbow','staff','spellbook','hybrid']

const QUESTIONS = [
 {title:'신체 검사 I',text:'정면에서 무거운 훈련 골렘이 돌진한다. 가장 먼저 취할 행동은?',choices:[
  {text:'정면에서 힘으로 밀어낸다',stat:{str:3,vit:1},weapon:{greatsword:2,axe:1,hammer:2}},
  {text:'공격을 받아내고 빈틈을 만든다',stat:{vit:3,str:1},weapon:{sword:2,spear:1,hammer:1}},
  {text:'옆으로 피하고 약점을 노린다',stat:{agi:3,str:1},weapon:{dagger:2,bow:1,spear:1}}
 ]},
 {title:'신체 검사 II',text:'긴 전투가 계속된다. 가장 자신 있는 방식은?',choices:[
  {text:'한 번의 큰 공격으로 끝낸다',stat:{str:3},weapon:{greatsword:2,axe:2}},
  {text:'끝까지 버티며 확실하게 싸운다',stat:{vit:3},weapon:{hammer:2,sword:1}},
  {text:'계속 움직이며 공격을 흘린다',stat:{agi:3},weapon:{dagger:2,bow:2}}
 ]},
 {title:'마력량 검사',text:'수정구가 마력을 요구한다. 어떤 식으로 마력을 주입할 것인가?',choices:[
  {text:'가능한 한 많은 마력을 한 번에 밀어 넣는다',stat:{mag:4},weapon:{staff:2},affinity:{fire:1,lightning:1}},
  {text:'출력을 유지하면서 천천히 높인다',stat:{mag:2,mnd:2},weapon:{spellbook:2},affinity:{ice:1,holy:1}},
  {text:'최소량으로 최대 반응을 끌어낸다',stat:{mnd:3,mag:1},weapon:{hybrid:2},affinity:{ender:1,void:1}}
 ]},
 {title:'마력 제어 검사',text:'불안정한 마법진을 안정시켜야 한다.',choices:[
  {text:'강한 마력으로 강제로 안정시킨다',stat:{mag:3,mnd:1},affinity:{fire:1,blood:1}},
  {text:'흐름을 읽어 정확히 맞춘다',stat:{mnd:4},affinity:{ice:1,holy:1,void:1}},
  {text:'빠르게 여러 번 보정한다',stat:{agi:2,mnd:2},affinity:{lightning:1,ender:1}}
 ]},
 {title:'무기 적성 I',text:'근접전에 가장 끌리는 전투 방식은?',choices:[
  {text:'검과 방어의 균형',weapon:{sword:4,hybrid:1},stat:{vit:1}},
  {text:'대검/도끼의 압도적인 한 방',weapon:{greatsword:3,axe:3},stat:{str:1}},
  {text:'단검/창의 빠른 간격 싸움',weapon:{dagger:3,spear:3},stat:{agi:1}}
 ]},
 {title:'무기 적성 II',text:'원거리 전투라면 어떤 방식을 택할 것인가?',choices:[
  {text:'활로 움직이며 연속 사격',weapon:{bow:4},stat:{agi:1}},
  {text:'석궁으로 정확한 강한 사격',weapon:{crossbow:4},stat:{str:1}},
  {text:'원거리보다 둔기로 진입',weapon:{hammer:4},stat:{vit:1}}
 ]},
 {title:'무기 적성 III',text:'마법과 무기를 함께 쓴다면?',choices:[
  {text:'스태프로 순수 마법을 강화',weapon:{staff:4},stat:{mag:1}},
  {text:'마법서로 다양한 주문을 운용',weapon:{spellbook:4},stat:{mnd:1}},
  {text:'마검으로 근접전과 주문을 병행',weapon:{hybrid:4,sword:1},stat:{str:1,mag:1}}
 ]},
 {title:'속성 감응 I',text:'막힌 길을 마법으로 열어야 한다.',choices:[
  {text:'불태워 길을 만든다',affinity:{fire:4}},
  {text:'얼려서 안전한 길을 만든다',affinity:{ice:4}},
  {text:'식물을 자라게 해 길을 만든다',affinity:{nature:4}}
 ]},
 {title:'속성 감응 II',text:'아군이 위험에 빠졌다. 가장 먼저 떠오르는 힘은?',choices:[
  {text:'번개처럼 빠르게 적을 제압한다',affinity:{lightning:4}},
  {text:'치유와 보호로 아군을 살린다',affinity:{holy:4}},
  {text:'공간을 넘어 아군을 빼낸다',affinity:{ender:4}}
 ]},
 {title:'속성 감응 III',text:'금지된 연구실에서 알 수 없는 힘이 반응한다.',choices:[
  {text:'생명력을 대가로 힘을 끌어낸다',affinity:{blood:4}},
  {text:'소환체를 만들어 대신 조사한다',affinity:{evocation:4}},
  {text:'공허의 흐름 자체를 관찰한다',affinity:{void:4}}
 ]},
 {title:'속성 감응 IV',text:'전투에서 가장 이상적인 승리 방식은?',choices:[
  {text:'압도적인 공격으로 전장을 지배',affinity:{fire:2,lightning:2,blood:1}},
  {text:'제어와 생존으로 상대를 무력화',affinity:{ice:2,nature:2,holy:1}},
  {text:'위치와 특수 능력으로 판을 바꾼다',affinity:{ender:2,evocation:2,void:1}}
 ]},
 {title:'최종 검사',text:'마법사가 된 뒤 가장 중요하게 생각할 것은?',choices:[
  {text:'강해지는 것',stat:{str:1,mag:2},affinity:{fire:1,lightning:1,blood:1}},
  {text:'살아남고 지키는 것',stat:{vit:2,mnd:1},affinity:{ice:1,nature:1,holy:1}},
  {text:'더 많은 것을 이해하는 것',stat:{mnd:2,mag:1},affinity:{ender:1,evocation:1,void:1}}
 ]}
]

function pname(p){ return p.getGameProfile().getName() }
function d(p){ return p.persistentData }
function gi(x,k){ return x.getInt(k) }
function pi(x,k,v){ x.putInt(k,v) }
function gs(x,k){ return x.getString(k) }
function ps(x,k,v){ x.putString(k,v) }

function tellraw(server,p,parts){
 server.runCommandSilent(`tellraw ${pname(p)} ${JSON.stringify(parts)}`)
}
function btn(label,cmd,color){
 return {
  text:`[ ${label} ]`,
  color:color,
  bold:true,
  underlined:true,
  clickEvent:{action:'run_command',value:cmd},
  hoverEvent:{action:'show_text',contents:{text:'클릭해서 선택'}}
 }
}
function strictInt(value){
 const text=String(value)
 if(!/^-?\d+$/.test(text)) return null
 const result=Number(text)
 return Number.isSafeInteger(result) ? result : null
}
function clampStat(value){ return Math.max(0,Math.min(100,value)) }
function playerCommand(e){
 if(e.player) return true
 e.respond('이 명령은 게임에 접속한 플레이어가 사용해야 합니다.')
 return false
}
function resetScores(p){
 const x=d(p)
 pi(x,'fantasia_exam_session',(gi(x,'fantasia_exam_session')+1)%2147483647)
 STAT_KEYS.forEach(k=>pi(x,`fantasia_${k}`,5))
 SCHOOL_KEYS.forEach(k=>pi(x,`fantasia_aff_${k}`,0))
 WEAPON_KEYS.forEach(k=>pi(x,`fantasia_weapon_${k}`,0))
 ps(x,'fantasia_primary',''); ps(x,'fantasia_secondary',''); ps(x,'fantasia_weapon_main','')
 pi(x,'fantasia_exam_stage',0)
 x.putBoolean('fantasia_exam_started',true)
 x.putBoolean('fantasia_exam_complete',false)
}
function addFx(p,c){
 const x=d(p)
 if(c.stat) Object.keys(c.stat).forEach(k=>pi(x,`fantasia_${k}`,gi(x,`fantasia_${k}`)+c.stat[k]))
 if(c.affinity) Object.keys(c.affinity).forEach(k=>pi(x,`fantasia_aff_${k}`,gi(x,`fantasia_aff_${k}`)+c.affinity[k]))
 if(c.weapon) Object.keys(c.weapon).forEach(k=>pi(x,`fantasia_weapon_${k}`,gi(x,`fantasia_weapon_${k}`)+c.weapon[k]))
}
function grant(server,p,id){ server.runCommandSilent(`advancement grant ${pname(p)} only fantasia_research:${id}`) }
function showQ(server,p){
 const x=d(p), s=gi(x,'fantasia_exam_stage')
 if(x.getBoolean('fantasia_exam_complete')) return showResult(server,p)
 if(s<0 || s>=QUESTIONS.length){
  p.tell('§c검사 데이터의 문항 번호가 올바르지 않습니다. 관리자에게 재검사를 요청하세요.')
  return
 }
 const q=QUESTIONS[s]
 tellraw(server,p,[
  {text:'\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n',color:'dark_gray'},
  {text:`[아카데미 입학 검사 ${s+1}/${QUESTIONS.length}] `,color:'gold',bold:true},
  {text:q.title+'\n',color:'yellow',bold:true},{text:q.text+'\n\n',color:'white'},{text:'선택지를 클릭하거나 채팅에 1 / 2 / 3 입력\n\n',color:'gray'},
  btn('1. '+q.choices[0].text,`/fantasia_exam choose ${gi(x,'fantasia_exam_session')} ${s} 1`,'green'),{text:'\n'},
  btn('2. '+q.choices[1].text,`/fantasia_exam choose ${gi(x,'fantasia_exam_session')} ${s} 2`,'aqua'),{text:'\n'},
  btn('3. '+q.choices[2].text,`/fantasia_exam choose ${gi(x,'fantasia_exam_session')} ${s} 3`,'light_purple'),
  {text:'\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━',color:'dark_gray'}
 ])
}
function milestone(server,p,i){
 if(i===1) grant(server,p,'exam/physical')
 if(i===2) grant(server,p,'exam/mana')
 if(i===3) grant(server,p,'exam/control')
 if(i===6) grant(server,p,'exam/weapon')
 if(i===10) grant(server,p,'exam/affinity')
}
function sorted(x,prefix,keys){ return keys.slice().sort((a,b)=>gi(x,prefix+b)-gi(x,prefix+a)) }
function applyStats(server,p){
 const x=d(p), n=pname(p)
 STAT_KEYS.forEach(k=>pi(x,`fantasia_${k}`,clampStat(gi(x,`fantasia_${k}`))))
 const str=gi(x,'fantasia_str'), vit=gi(x,'fantasia_vit'), agi=gi(x,'fantasia_agi')
 const mag=gi(x,'fantasia_mag'), mnd=gi(x,'fantasia_mnd')
 const hp=20+Math.max(0,vit-5)*0.5
 const atk=1+Math.max(0,str-5)*0.12
 const spd=0.1+Math.max(0,agi-5)*0.001
 const mana=100+Math.max(0,mag-5)*5
 const regen=1+Math.max(0,mnd-5)*0.05
 const power=1+Math.max(0,mag-5)*0.01
 server.runCommandSilent(`attribute ${n} minecraft:generic.max_health base set ${hp}`)
 server.runCommandSilent(`attribute ${n} minecraft:generic.attack_damage base set ${atk}`)
 server.runCommandSilent(`attribute ${n} minecraft:generic.movement_speed base set ${spd}`)
 if(Platform.isLoaded('irons_spellbooks')){
  server.runCommandSilent(`attribute ${n} irons_spellbooks:max_mana base set ${mana}`)
  server.runCommandSilent(`attribute ${n} irons_spellbooks:mana_regen base set ${regen}`)
  server.runCommandSilent(`attribute ${n} irons_spellbooks:spell_power base set ${power}`)
 }
}
function finish(server,p){
 const x=d(p)
 if(x.getBoolean('fantasia_exam_complete')) return
 if(gi(x,'fantasia_exam_stage')!==QUESTIONS.length) return
 const a=sorted(x,'fantasia_aff_',SCHOOL_KEYS), w=sorted(x,'fantasia_weapon_',WEAPON_KEYS)
 ps(x,'fantasia_primary',a[0]); ps(x,'fantasia_secondary',a[1]); ps(x,'fantasia_weapon_main',w[0])
 x.putBoolean('fantasia_exam_complete',true); pi(x,'fantasia_exam_stage',QUESTIONS.length)
 grant(server,p,'exam/complete'); grant(server,p,`${a[0]}_tier_1`)
 applyStats(server,p)
 showResult(server,p)
}
function showResult(server,p){
 const x=d(p), pr=gs(x,'fantasia_primary'), se=gs(x,'fantasia_secondary'), we=gs(x,'fantasia_weapon_main')
 tellraw(server,p,[
  {text:'\n══════════ 입학 검사 결과 ══════════\n',color:'gold',bold:true},
  {text:`STR ${gi(x,'fantasia_str')}   `,color:'red'},
  {text:`VIT ${gi(x,'fantasia_vit')}   `,color:'green'},
  {text:`AGI ${gi(x,'fantasia_agi')}   `,color:'aqua'},
  {text:`MAG ${gi(x,'fantasia_mag')}   `,color:'light_purple'},
  {text:`MND ${gi(x,'fantasia_mnd')}\n`,color:'blue'},
  {text:'주 마법 적성: ',color:'gray'},{text:(SCHOOL_LABELS[pr]||pr)+'\n',color:'yellow',bold:true},
  {text:'보조 마법 적성: ',color:'gray'},{text:(SCHOOL_LABELS[se]||se)+'\n',color:'white'},
  {text:'추천 무기: ',color:'gray'},{text:(WEAPON_LABELS[we]||we)+'\n\n',color:'gold',bold:true},
  {text:`${SCHOOL_LABELS[pr]||pr} 1단계 연구가 자동 개방되었습니다.\n`,color:'green'},
  {text:'다른 무기/마법도 이후 연구로 모두 사용할 수 있습니다.\n',color:'gray'},
  btn('현재 목표','/fantasia_content','green'),{text:'\n'},
  {text:'아카데미 중앙의 아델린을 우클릭하면 여행을 시작할 수 있습니다.\n',color:'aqua'}
 ])
}
function revokeKnown(server,p){
 const n=pname(p)
 const ids=['exam/registration','exam/physical','exam/mana','exam/control','exam/weapon','exam/affinity','exam/complete']
 SCHOOL_KEYS.forEach(s=>[1,2,3].forEach(t=>ids.push(`${s}_tier_${t}`)))
 ids.forEach(id=>server.runCommandSilent(`advancement revoke ${n} only fantasia_research:${id}`))
}
function start(server,p,force){
 if(force || !d(p).getBoolean('fantasia_exam_started')) resetScores(p)
 grant(server,p,'exam/registration'); showQ(server,p)
}
function resetAll(server,p){
 resetScores(p)
 d(p).putBoolean('fantasia_exam_started',false)
 d(p).putBoolean('fantasia_exam_complete',false)
 // Reset every known research/course advancement, including the old map-breaking permission.
 server.runCommandSilent(`advancement revoke ${pname(p)} from fantasia_research:root`)
 revokeKnown(server,p)
 applyStats(server,p)
 if(Platform.isLoaded('ftbquests')) server.runCommandSilent(`ftbquests change_progress ${pname(p)} reset-all`)
 // Research access is advancement-based; there is no required isstweaks reset command.
 server.runCommandSilent(`execute as ${pname(p)} at @s run function fantasia:admin/reset_player`)
 if(typeof fantasiaResetBonds==='function') fantasiaResetBonds(server,p)
}

PlayerEvents.loggedIn(e=>{
 const p=e.player, x=d(p)
 e.server.runCommandSilent(`tag ${pname(p)} add fa_modded`)
 if(x.getBoolean('fantasia_exam_complete')){ applyStats(e.server,p); return }
 if(!x.getBoolean('fantasia_exam_started')) start(e.server,p,true)
 else tellraw(e.server,p,[{text:'[Fantasia] ',color:'gold',bold:true},{text:'입학 검사가 아직 끝나지 않았습니다. ',color:'white'},btn('검사 계속하기','/fantasia_exam resume','aqua')])
})

PlayerEvents.respawned(e=>{
 // KubeJS clones persistentData; attributes belong to the newly created player entity.
 e.server.runCommandSilent(`tag ${pname(e.player)} add fa_modded`)
 if(d(e.player).getBoolean('fantasia_exam_complete')) applyStats(e.server,e.player)
})

function chooseExamOption(server,p,c){
 const x=d(p)
 if(!Number.isInteger(c)||c<1||c>3){ p.tell('§e1, 2, 3 중 하나를 선택하세요.'); return }
 if(x.getBoolean('fantasia_exam_complete')){ showResult(server,p); return }
 if(!x.getBoolean('fantasia_exam_started')){ start(server,p,true); return }

 let s=gi(x,'fantasia_exam_stage')
 if(s<0||s>=QUESTIONS.length){ showQ(server,p); return }

 addFx(p,QUESTIONS[s].choices[c-1])
 milestone(server,p,s)
 s++
 pi(x,'fantasia_exam_stage',s)

 if(s>=QUESTIONS.length) finish(server,p)
 else showQ(server,p)
}

// INTERNAL: clickable exam choices call this. Players do not need to type it.
ServerEvents.basicCommand('fantasia_exam',e=>{
 if(!playerCommand(e)) return
 const p=e.player, x=d(p), input=(e.input||'').trim()
 if(input==='' || input==='resume'){
  if(!x.getBoolean('fantasia_exam_started')) start(e.server,p,true)
  else showQ(e.server,p)
  return
 }
 if(input==='result'){
  if(x.getBoolean('fantasia_exam_complete')) showResult(e.server,p)
  else p.tell('§c아직 검사가 끝나지 않았습니다.')
  return
 }

 const parts=input.split(/\s+/)
 if(parts[0]==='choose' && parts.length===4){
  const session=strictInt(parts[1])
  const expected=strictInt(parts[2])
  const choice=strictInt(parts[3])
  if(session===null || expected===null || choice===null){ p.tell('§c올바른 검사 선택지가 아닙니다.'); return }
  const current=gi(x,'fantasia_exam_stage')

  if(x.getBoolean('fantasia_exam_complete')){
   p.tell('§e이미 입학 검사를 완료했습니다.')
   return
  }

  if(session!==gi(x,'fantasia_exam_session') || expected!==current){
   p.tell('§7[Fantasia] 이전 문항의 선택지는 더 이상 사용할 수 없습니다.')
   showQ(e.server,p)
   return
  }

  chooseExamOption(e.server,p,choice)
  return
 }

 // 숫자 직접 입력은 언제나 "현재 문항"에만 적용
 if(/^[123]$/.test(input)) chooseExamOption(e.server,p,Number(input))
 else p.tell('§e현재 문항의 선택지 버튼을 클릭하세요.')
})

PlayerEvents.chat(e=>{
 const msg=(e.message||'').trim()

 if(msg!=='1' && msg!=='2' && msg!=='3') return
 if(!d(e.player).getBoolean('fantasia_exam_started')) return
 if(d(e.player).getBoolean('fantasia_exam_complete')) return

 e.cancel()
 chooseExamOption(e.server,e.player,Number(msg))
})

// INTERNAL: character-sheet UI/NPC button calls this.
ServerEvents.basicCommand('fantasia_stats',e=>{
 if(!playerCommand(e)) return
 if(!d(e.player).getBoolean('fantasia_exam_complete')){ e.player.tell('§c입학 검사를 먼저 완료하세요.'); return }
 showResult(e.server,e.player)
})


// INTERNAL: quest/NPC UI opens this progression summary.
ServerEvents.basicCommand('fantasia_content',e=>{
 if(!playerCommand(e)) return
 if(!d(e.player).getBoolean('fantasia_exam_complete')){
  showQ(e.server,e.player)
  return
 }
 e.server.runCommandSilent(`execute as ${pname(e.player)} at @s run function fantasia:status`)
 if(Platform.isLoaded('ftbquests')) tellraw(e.server,e.player,[btn('연구 퀘스트 보기','/ftbquests open_book','aqua')])
})

// OP ONLY: administration/testing commands.
ServerEvents.basicCommand('fantasia_admin',e=>{
 if(!playerCommand(e)) return
 const admin=e.player
 if(!e.server.playerList.isOp(admin.getGameProfile())){ admin.tell('§cOP 전용 명령입니다.'); return }
 const a=(e.input||'').trim().split(/\s+/).filter(s=>s.length>0)
 if(a.length<2){
  admin.tell('§e/fantasia_admin restart <player>')
  admin.tell('§e/fantasia_admin resetall <player>')
  admin.tell('§e/fantasia_admin addstat <player> <str|vit|agi|mag|mnd> <amount>')
  admin.tell('§e/fantasia_admin setstat <player> <str|vit|agi|mag|mnd> <value>')
  admin.tell('§e/fantasia_admin result <player>'); return
 }
 const act=a[0].toLowerCase(), target=e.server.playerList.getPlayerByName(a[1])
 if(target==null){ admin.tell('§c해당 플레이어가 온라인이 아닙니다.'); return }
 if(act==='restart'){
  // Re-taking the exam must preserve research earned in a finished campaign.
  resetScores(target)
  ;['registration','physical','mana','control','weapon','affinity','complete'].forEach(id=>
   e.server.runCommandSilent(`advancement revoke ${pname(target)} only fantasia_research:exam/${id}`))
  applyStats(e.server,target)
  start(e.server,target,false); admin.tell(`§a${pname(target)} 재검사를 시작했습니다.`); return
 }
 if(act==='resetall'){ resetAll(e.server,target); admin.tell(`§a${pname(target)} 전체 진행을 초기화했습니다.`); return }
 if(act==='result'){ if(d(target).getBoolean('fantasia_exam_complete')) showResult(e.server,target); else admin.tell('§e아직 검사 미완료입니다.'); return }
 if((act==='addstat'||act==='setstat')&&a.length===4){
  const stat=a[2].toLowerCase(), value=strictInt(a[3])
  if(!STAT_KEYS.includes(stat)||value===null){ admin.tell('§c스탯: str, vit, agi, mag, mnd'); return }
  const x=d(target), key=`fantasia_${stat}`
  if(act==='addstat') pi(x,key,clampStat(gi(x,key)+value)); else pi(x,key,clampStat(value))
  applyStats(e.server,target); admin.tell(`§a${pname(target)} ${stat.toUpperCase()} = ${gi(x,key)}`); return
 }
 admin.tell('§c알 수 없는 Fantasia 관리자 명령입니다.')
})
