// Keep bindings local; avoid Rhino block-level const redeclaration during script loading.
;(function(){
// Iron's 1.21 API: SpellPreCastEvent + ISpellContainer. No custom JAR required.
const FANTASIA_SPELL_GATES = {
 "irons_spellbooks:blood_slash": "blood_tier_1",
 "irons_spellbooks:blood_needles": "blood_tier_1",
 "irons_spellbooks:heartstop": "blood_tier_1",
 "irons_spellbooks:blood_step": "blood_tier_2",
 "irons_spellbooks:ray_of_siphoning": "blood_tier_2",
 "irons_spellbooks:wither_skull": "blood_tier_2",
 "irons_spellbooks:raise_dead": "blood_tier_2",
 "irons_spellbooks:acupuncture": "blood_tier_3",
 "irons_spellbooks:devour": "blood_tier_3",
 "irons_spellbooks:sacrifice": "blood_tier_3",
 "irons_spellbooks:magic_missile": "ender_tier_1",
 "irons_spellbooks:teleport": "ender_tier_1",
 "irons_spellbooks:evasion": "ender_tier_1",
 "irons_spellbooks:summon_ender_chest": "ender_tier_1",
 "irons_spellbooks:recall": "ender_tier_1",
 "irons_spellbooks:magic_arrow": "ender_tier_2",
 "irons_spellbooks:dragon_breath": "ender_tier_2",
 "irons_spellbooks:counterspell": "ender_tier_2",
 "irons_spellbooks:portal": "ender_tier_2",
 "irons_spellbooks:echoing_strikes": "ender_tier_2",
 "irons_spellbooks:starfall": "ender_tier_3",
 "irons_spellbooks:black_hole": "ender_tier_3",
 "irons_spellbooks:summon_swords": "ender_tier_3",
 "irons_spellbooks:shadow_slash": "ender_tier_3",
 "irons_spellbooks:arcane_shackle": "ender_tier_3",
 "irons_spellbooks:gravity_fissure": "ender_tier_3",
 "irons_spellbooks:fang_strike": "evocation_tier_1",
 "irons_spellbooks:shield": "evocation_tier_1",
 "irons_spellbooks:summon_horse": "evocation_tier_1",
 "irons_spellbooks:summon_vex": "evocation_tier_1",
 "irons_spellbooks:gust": "evocation_tier_1",
 "irons_spellbooks:slow": "evocation_tier_1",
 "irons_spellbooks:firecracker": "evocation_tier_1",
 "irons_spellbooks:fang_ward": "evocation_tier_2",
 "irons_spellbooks:fang_swirl": "evocation_tier_2",
 "irons_spellbooks:invisibility": "evocation_tier_2",
 "irons_spellbooks:lob_creeper": "evocation_tier_2",
 "irons_spellbooks:arrow_volley": "evocation_tier_2",
 "irons_spellbooks:throw": "evocation_tier_2",
 "irons_spellbooks:chain_creeper": "evocation_tier_3",
 "irons_spellbooks:spectral_hammer": "evocation_tier_3",
 "irons_spellbooks:wololo": "evocation_tier_3",
 "irons_spellbooks:scapegoat": "evocation_tier_3",
 "irons_spellbooks:firebolt": "fire_tier_1",
 "irons_spellbooks:burning_dash": "fire_tier_1",
 "irons_spellbooks:fireball": "fire_tier_1",
 "irons_spellbooks:fire_breath": "fire_tier_2",
 "irons_spellbooks:wall_of_fire": "fire_tier_2",
 "irons_spellbooks:scorch": "fire_tier_2",
 "irons_spellbooks:fire_arrow": "fire_tier_2",
 "irons_spellbooks:heat_surge": "fire_tier_2",
 "irons_spellbooks:blaze_storm": "fire_tier_3",
 "irons_spellbooks:magma_bomb": "fire_tier_3",
 "irons_spellbooks:flaming_barrage": "fire_tier_3",
 "irons_spellbooks:flaming_strike": "fire_tier_3",
 "irons_spellbooks:raise_hell": "fire_tier_3",
 "irons_spellbooks:heal": "holy_tier_1",
 "irons_spellbooks:wisp": "holy_tier_1",
 "irons_spellbooks:guiding_bolt": "holy_tier_1",
 "irons_spellbooks:haste": "holy_tier_1",
 "irons_spellbooks:greater_heal": "holy_tier_2",
 "irons_spellbooks:healing_circle": "holy_tier_2",
 "irons_spellbooks:blessing_of_life": "holy_tier_2",
 "irons_spellbooks:fortify": "holy_tier_2",
 "irons_spellbooks:cleanse": "holy_tier_2",
 "irons_spellbooks:cloud_of_regeneration": "holy_tier_3",
 "irons_spellbooks:sunbeam": "holy_tier_3",
 "irons_spellbooks:angel_wing": "holy_tier_3",
 "irons_spellbooks:divine_smite": "holy_tier_3",
 "irons_spellbooks:icicle": "ice_tier_1",
 "irons_spellbooks:ray_of_frost": "ice_tier_1",
 "irons_spellbooks:frost_step": "ice_tier_1",
 "irons_spellbooks:snowball": "ice_tier_1",
 "irons_spellbooks:cone_of_cold": "ice_tier_2",
 "irons_spellbooks:frostwave": "ice_tier_2",
 "irons_spellbooks:ice_spikes": "ice_tier_2",
 "irons_spellbooks:frostbite": "ice_tier_2",
 "irons_spellbooks:ice_block": "ice_tier_3",
 "irons_spellbooks:ice_tomb": "ice_tier_3",
 "irons_spellbooks:summon_polar_bear": "ice_tier_3",
 "irons_spellbooks:blizzard": "ice_tier_3",
 "irons_spellbooks:electrocute": "lightning_tier_1",
 "irons_spellbooks:charge": "lightning_tier_1",
 "irons_spellbooks:lightning_bolt": "lightning_tier_1",
 "irons_spellbooks:lightning_lance": "lightning_tier_2",
 "irons_spellbooks:ascension": "lightning_tier_2",
 "irons_spellbooks:chain_lightning": "lightning_tier_2",
 "irons_spellbooks:shockwave": "lightning_tier_2",
 "irons_spellbooks:thunderstorm": "lightning_tier_3",
 "irons_spellbooks:ball_lightning": "lightning_tier_3",
 "irons_spellbooks:volt_strike": "lightning_tier_3",
 "irons_spellbooks:poison_breath": "nature_tier_1",
 "irons_spellbooks:poison_arrow": "nature_tier_1",
 "irons_spellbooks:acid_orb": "nature_tier_1",
 "irons_spellbooks:root": "nature_tier_1",
 "irons_spellbooks:oakskin": "nature_tier_1",
 "irons_spellbooks:poison_splash": "nature_tier_2",
 "irons_spellbooks:blight": "nature_tier_2",
 "irons_spellbooks:spider_aspect": "nature_tier_2",
 "irons_spellbooks:firefly_swarm": "nature_tier_2",
 "irons_spellbooks:stomp": "nature_tier_2",
 "irons_spellbooks:earthquake": "nature_tier_3",
 "irons_spellbooks:gluttony": "nature_tier_3",
 "irons_spellbooks:touch_dig": "nature_tier_3",
 "irons_spellbooks:planar_sight": "void_tier_1",
 "irons_spellbooks:telekinesis": "void_tier_1",
 "irons_spellbooks:abyssal_shroud": "void_tier_1",
 "irons_spellbooks:sculk_tentacles": "void_tier_2",
 "irons_spellbooks:sonic_boom": "void_tier_2",
 "irons_spellbooks:eldritch_blast": "void_tier_2",
 "irons_spellbooks:pocket_dimension": "void_tier_3"
}

if(Platform.isLoaded('irons_spellbooks')){
 var FaResourceLocation=Java.loadClass('net.minecraft.resources.ResourceLocation')
 var FaSpellRegistry=Java.loadClass('io.redspace.ironsspellbooks.api.registry.SpellRegistry')
 var FaSpellContainer=Java.loadClass('io.redspace.ironsspellbooks.api.spells.ISpellContainer')
 var faHasResearch=function(p,path){
  const advancement=p.getServer().getAdvancements().get(FaResourceLocation.fromNamespaceAndPath('fantasia_research',path))
  return advancement!==null && p.getAdvancements().getOrStartProgress(advancement).isDone()
 }
 if(!Platform.isLoaded('fantasia_core')){
  NativeEvents.onEvent(Java.loadClass('io.redspace.ironsspellbooks.api.events.SpellPreCastEvent'),event=>{
   const p=event.getEntity()
   if(p.getServer()===null) return
   const id=String(event.getSpellId()), gate=FANTASIA_SPELL_GATES[id]
   const destructive=id==='irons_spellbooks:touch_dig'||id==='irons_spellbooks:spectral_hammer'
   const inMap=String(p.level().dimension().location())==='fantasia:campaign'
   if(destructive && (inMap || !faHasResearch(p,'map_breaking_magic'))){
    event.setCanceled(true); p.tell('§c이 주문은 맵 보호를 위해 봉인되어 있습니다.'); return
   }
   if(gate && !faHasResearch(p,gate)){
    event.setCanceled(true); p.tell('§c아직 연구하지 않은 주문입니다. 지역 임무와 연구를 진행하세요.')
   }
  })
 }
 ServerEvents.basicCommand('fantasia_magic',e=>{
  const p=e.player
  if(!p){ e.respond('게임 안에서 노아에게 연구를 요청하세요.'); return }
  const name=p.getGameProfile().getName()
  const nearby=e.server.getCommands().getDispatcher().execute(
   `execute as ${name} at @s if dimension fantasia:campaign if entity @e[tag=fa_npc_noah,distance=..6,limit=1]`,
   e.server.createCommandSourceStack().withSuppressedOutput())>0
  if(!nearby){ p.tell('§e아카데미의 노아에게 가까이 가서 연구를 요청하세요.'); return }
  if(!faHasResearch(p,'exam/complete')){ p.tell('§e입학 검사를 먼저 완료하세요.'); return }
  const args=String(e.input||'').trim().split(/\s+/), action=args[0]
  function say(components){e.server.runCommandSilent(`tellraw ${name} ${JSON.stringify(components)}`)}
  if(action==='book' && args.length===1){
   const now=Number(e.server.overworld().getGameTime()), data=p.persistentData
   const previous=Number(data.getLong('fantasia_book_time'))
   if(data.contains('fantasia_book_time') && now>=previous && now-previous<1200){p.tell('§e마법서는 1분마다 한 권 받을 수 있습니다.');return}
   const book=Item.of('irons_spellbooks:iron_spell_book')
   FaSpellContainer.set(book,FaSpellContainer.create(6,true,true))
   p.give(book); data.putLong('fantasia_book_time',now)
   p.tell('§b마법서를 주 손에 들고 연구 메뉴에서 주문을 각인하세요. 장착한 뒤 Iron’s 주문 선택·시전 키를 사용합니다.');return
  }
  if(action==='learn' && args.length===2){
   const id='irons_spellbooks:'+args[1], gate=FANTASIA_SPELL_GATES[id]
   if(!gate || !faHasResearch(p,gate)){p.tell('§e해당 주문의 연구를 먼저 완료하세요.');return}
   if(args[1]==='touch_dig'||args[1]==='spectral_hammer'){p.tell('§e지형 파괴 주문은 캠페인에서 사용할 수 없습니다.');return}
   const held=p.getMainHandItem()
   if(held.isEmpty() || String(held.id)!=='irons_spellbooks:iron_spell_book'){p.tell('§e노아에게 받은 철 마법서를 주 손에 들어주세요.');return}
   const spell=FaSpellRegistry.REGISTRY.get(FaResourceLocation.parse(id))
   if(spell===null || spell===FaSpellRegistry.none()){p.tell('§c현재 Iron’s 버전에 등록되지 않은 주문입니다.');return}
   const current=FaSpellContainer.getOrCreate(held)
   if(current.getIndexForSpell(spell)>=0){p.tell('§e이미 이 책에 각인한 주문입니다.');return}
   const mutable=current.mutableCopy()
   if(!mutable.addSpell(spell,1,false)){p.tell('§e책의 6개 슬롯이 찼습니다. 다른 연구용 책을 사용하세요.');return}
   FaSpellContainer.set(held,mutable.toImmutable());p.sendInventoryUpdate()
   p.tell('§a1레벨 주문을 각인했습니다. 마법서를 장착해 사용하세요.');return
  }
  const schools={fire:'화염',ice:'빙결',lightning:'전격',nature:'자연',holy:'신성',ender:'엔더',blood:'혈마법',evocation:'소환',void:'공허'}
  if(action==='school' && args.length===2 && schools[args[1]]){
   p.tell('§6'+schools[args[1]]+' 연구 — 해금된 주문을 클릭해 들고 있는 책에 각인하세요.')
   Object.keys(FANTASIA_SPELL_GATES).forEach(id=>{
    const gate=FANTASIA_SPELL_GATES[id]
    if(gate.indexOf(args[1]+'_tier_')!==0 || !faHasResearch(p,gate))return
    const spell=id.split(':')[1]
    if(spell==='touch_dig'||spell==='spectral_hammer')return
    say([{text:'[ 각인 ] ',color:'aqua',clickEvent:{action:'run_command',value:'/fantasia_magic learn '+spell}},{translate:'spell.irons_spellbooks.'+spell,color:'white'},{text:' · 연구 '+gate.slice(-1),color:'gray'}])
   });return
  }
  say([{text:'[ 연구용 마법서 받기 ]',color:'green',clickEvent:{action:'run_command',value:'/fantasia_magic book'}}])
  Object.keys(schools).forEach(school=>say([{text:'[ '+schools[school]+' 연구 ]',color:'aqua',clickEvent:{action:'run_command',value:'/fantasia_magic school '+school}}]))
 })
}else{
 ServerEvents.basicCommand('fantasia_magic',e=>{
  if(e.player)e.player.tell('§eIron’s Spells ’n Spellbooks를 설치하면 주문 연구를 이용할 수 있습니다.')
  else e.respond('Iron’s Spells ’n Spellbooks가 설치되지 않았습니다.')
 })
}

// Native NeoForge hook is available in KubeJS 2101 server scripts.
if(!Platform.isLoaded('fantasia_core')){
 NativeEvents.onEvent(Java.loadClass('net.neoforged.neoforge.event.level.ExplosionEvent$Detonate'),event=>{
  if(String(event.getLevel().dimension().location())==='fantasia:campaign')event.getAffectedBlocks().clear()
 })
}

})();
