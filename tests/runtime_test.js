// Tests execute the shipped scripts together. Minecraft/Java APIs are explicit
// test doubles: passing does not mean a live NeoForge server has been tested.
const assert = require('node:assert/strict')
const fs = require('node:fs')
const vm = require('node:vm')
const path = require('node:path')
const {test} = require('node:test')

class Data {
 constructor(){this.values={}}
 getInt(k){return this.values[k]||0} putInt(k,v){this.values[k]=v}
 getLong(k){return this.values[k]||0} putLong(k,v){this.values[k]=v}
 getString(k){return this.values[k]||''} putString(k,v){this.values[k]=v}
 getBoolean(k){return this.values[k]===true} putBoolean(k,v){this.values[k]=v}
 contains(k){return Object.hasOwn(this.values,k)} remove(k){delete this.values[k]}
}
function item(id,count=1){return {id,count,isEmpty(){return this.count<=0||this.id==='minecraft:air'},shrink(n){this.count-=n}}}
function container(slots,spells=[]){return {
 slots,spells,getIndexForSpell(s){return this.spells.indexOf(s.id)},
 mutableCopy(){return container(this.slots,this.spells.slice())},
 addSpell(s){if(this.spells.length>=this.slots||this.spells.includes(s.id))return false;this.spells.push(s.id);return true},
 toImmutable(){return this}
}}
function harness(mods=['kubejs','irons_spellbooks'],prelude=''){
 const events={}, commands={}, native={}, log=[], players={}, clock={time:1000}
 const p={name:'Tester',persistentData:new Data(),messages:[],inventory:[],advancements:new Set(),scores:{fa_stage:0},tags:new Set(),op:false,near:'noah',dimension:'fantasia:campaign',hand:item('minecraft:air',0),
  getGameProfile(){return {getName:()=>this.name}},tell(t){this.messages.push(t)},getMainHandItem(){return this.hand},sendInventoryUpdate(){},give(i){this.inventory.push(i)},
  getServer(){return server},getAdvancements(){return {getOrStartProgress:a=>({isDone:()=>this.advancements.has(a)})}},level(){return {dimension:()=>({location:()=>this.dimension})}}
 }
 players[p.name]=p
 const server={
  runCommandSilent(command){
   log.push(command)
   let m=command.match(/^advancement (grant|revoke) (\w+) only (\S+)/)
   if(m && players[m[2]])players[m[2]].advancements[m[1]==='grant'?'add':'delete'](m[3])
   m=command.match(/^advancement revoke (\w+) from fantasia_research:root/)
   if(m)players[m[1]].advancements.clear()
   m=command.match(/^scoreboard players set (\w+) (\S+) (-?\d+)$/)
   if(m && players[m[1]])players[m[1]].scores[m[2]]=Number(m[3])
   // Deliberately VOID, matching KubeJS 2101 (old code treated it as an int).
  },
  overworld:()=>({getGameTime:()=>clock.time}),
  createCommandSourceStack:()=>({withSuppressedOutput:()=>({})}),
  getCommands:()=>({getDispatcher:()=>({execute(command){
   const m=command.match(/execute as (\w+).*tag=fa_npc_([a-z]+),/)
   assert.ok(m,'Only audited query commands may return a result')
   const who=players[m[1]]
   return who.dimension==='fantasia:campaign'&&who.near===m[2]?1:0
  }})}),
  getScoreboard:()=>({getObjective:id=>id,getPlayerScoreInfo:(who,id)=>Object.hasOwn(who.scores,id)?{value:()=>who.scores[id]}:null}),
  getAdvancements:()=>({get:id=>id}),
  playerList:{isOp:profile=>players[profile.getName()].op,getPlayerByName:name=>players[name]||null}
 }
 function subscribe(name,fn){(events[name]??=[]).push(fn)}
 const classes={
  'net.minecraft.resources.ResourceLocation':{fromNamespaceAndPath:(ns,p)=>ns+':'+p,parse:id=>id},
  'io.redspace.ironsspellbooks.api.registry.SpellRegistry':{REGISTRY:{get:id=>({id})},none:()=>null},
  'io.redspace.ironsspellbooks.api.spells.ISpellContainer':{create:n=>container(n),set:(i,c)=>{i.container=c},getOrCreate:i=>i.container||container(6)}
 }
 const scope=vm.createContext({console,Platform:{isLoaded:id=>mods.includes(id)},
  ServerEvents:{basicCommand:(id,fn)=>{assert.ok(!commands[id],id+' registered twice');commands[id]=fn},loaded:fn=>subscribe('loaded',fn)},
  PlayerEvents:{loggedIn:fn=>subscribe('loggedIn',fn),respawned:fn=>subscribe('respawned',fn),chat:fn=>subscribe('chat',fn)},
  NativeEvents:{onEvent:(cls,fn)=>{(native[cls]??=[]).push(fn)}},
  Java:{loadClass:name=>classes[name]||name},Item:{of:id=>item(id)}
 })
 if(prelude)vm.runInContext(prelude,scope)
 for(const file of fs.readdirSync(path.join(__dirname,'../kubejs/server_scripts')).filter(f=>f.endsWith('.js')).sort()){
  vm.runInContext(fs.readFileSync(path.join(__dirname,'../kubejs/server_scripts',file),'utf8'),scope,{filename:file})
 }
 function run(id,input='',who=p){const e={player:who,server,input,respond:t=>log.push(t)};commands[id](e)}
 function emit(name,extra={}){for(const fn of events[name]||[])fn({player:p,server,...extra})}
 function complete(){emit('loggedIn');const session=p.persistentData.getInt('fantasia_exam_session');for(let i=0;i<12;i++)run('fantasia_exam',`choose ${session} ${i} 1`)}
 return {p,server,clock,events,commands,native,log,run,emit,complete,scope}
}

test('12 questions finish once, re-login and respawn restore 1.21.1 attributes',()=>{
 const h=harness();h.complete()
 assert.equal(h.p.persistentData.getBoolean('fantasia_exam_complete'),true)
 assert.ok(h.p.advancements.has('fantasia_research:exam/complete'))
 assert.equal(h.p.inventory.length,0,'No automatic exam items')
 assert.ok(h.log.some(x=>x.startsWith('attribute Tester minecraft:generic.max_health base set ')))
 assert.ok(!h.log.some(x=>x.startsWith('attribute Tester minecraft:max_health')))
 const stats={...h.p.persistentData.values};h.run('fantasia_exam','choose 1 11 1')
 assert.deepEqual(h.p.persistentData.values,stats)
 h.log.length=0;h.emit('respawned');assert.equal(h.log.filter(x=>x.startsWith('attribute ')).length,6)
 h.emit('loggedIn');assert.deepEqual(h.p.persistentData.values,stats)
})
test('invalid input, duplicate question and stale session never change scores',()=>{
 const h=harness();h.emit('loggedIn')
 const session=h.p.persistentData.getInt('fantasia_exam_session')
 for(const bad of ['1abc','1.5','choose 1 0 NaN','choose 1 0 1 extra','choose 1 0 99'])h.run('fantasia_exam',bad)
 assert.equal(h.p.persistentData.getInt('fantasia_exam_stage'),0)
 h.run('fantasia_exam',`choose ${session} 0 1`)
 const state={...h.p.persistentData.values};h.run('fantasia_exam',`choose ${session} 0 2`)
 assert.deepEqual(h.p.persistentData.values,state)
 h.p.op=true;h.run('fantasia_admin','restart Tester')
 h.run('fantasia_exam',`choose ${session} 0 1`)
 assert.equal(h.p.persistentData.getInt('fantasia_exam_stage'),0)
})
test('re-taking exam preserves campaign research; full reset removes it',()=>{
 const h=harness();h.complete();h.p.op=true
 h.p.advancements.add('fantasia_research:fire_tier_3')
 h.run('fantasia_admin','restart Tester')
 assert.ok(h.p.advancements.has('fantasia_research:fire_tier_3'))
 h.run('fantasia_admin','resetall Tester')
 assert.equal(h.p.advancements.has('fantasia_research:fire_tier_3'),false)
})
test('numeric chat resumes and completed exams no longer consume chat',()=>{
 const h=harness();h.emit('loggedIn');let cancelled=false
 h.emit('chat',{message:'2',cancel:()=>{cancelled=true}})
 assert.ok(cancelled);assert.equal(h.p.persistentData.getInt('fantasia_exam_stage'),1)
 h.complete();cancelled=false;h.emit('chat',{message:'3',cancel:()=>{cancelled=true}});assert.equal(cancelled,false)
})
test('console commands are safe and non-OP cannot alter stats or reset others',()=>{
 const h=harness();h.emit('loggedIn');const state={...h.p.persistentData.values}
 for(const cmd of Object.keys(h.commands))h.run(cmd,'',null)
 h.run('fantasia_admin','setstat Tester str 99');assert.deepEqual(h.p.persistentData.values,state)
 h.p.op=true;h.run('fantasia_admin','setstat Tester str 999999');assert.equal(h.p.persistentData.getInt('fantasia_str'),100)
 h.run('fantasia_admin','addstat Tester str -999999');assert.equal(h.p.persistentData.getInt('fantasia_str'),0)
 h.run('fantasia_admin','setstat Tester str 12junk');assert.equal(h.p.persistentData.getInt('fantasia_str'),0)
})
test('gifts consume held item only, enforce range/cooldown, record threshold crossings',()=>{
 const h=harness();h.p.hand=item('minecraft:amethyst_shard',4)
 h.p.near='noah';h.run('fantasia_npc','adeline gift');assert.equal(h.p.hand.count,4)
 h.p.near='adeline';h.p.hand=item('minecraft:air',0);h.run('fantasia_npc','adeline gift')
 assert.equal(h.p.persistentData.getInt('fantasia_affection_adeline'),0)
 h.p.hand=item('minecraft:amethyst_shard',4);h.p.persistentData.putInt('fantasia_affection_adeline',78)
 h.run('fantasia_npc','adeline gift');assert.equal(h.p.hand.count,3)
 assert.equal(h.p.persistentData.getInt('fantasia_affection_adeline'),83)
 assert.ok(h.p.advancements.has('fantasia_research:bond/adeline'))
 assert.equal(h.p.scores.fa_b_adeline,83)
 h.run('fantasia_npc','adeline gift');assert.equal(h.p.hand.count,3)
 h.clock.time+=600;h.run('fantasia_npc','adeline gift');assert.equal(h.p.hand.count,2)
 assert.ok(!h.log.some(x=>x.startsWith('clear ')))
})
test('story dialogue reads actual scoreboard result despite void runCommandSilent',()=>{
 const h=harness();h.p.near='adeline';h.p.scores.fa_stage=7
 h.p.persistentData.putInt('fantasia_affection_adeline',80)
 h.run('fantasia_npc','adeline talk')
 assert.ok(h.p.messages.some(x=>x.includes('당신의 자리를')))
})
test('spell gate blocks unresearched casts and map destruction; explosion entity damage retained',()=>{
 const h=harness();const event={getEntity:()=>h.p,getSpellId:()=> 'irons_spellbooks:firebolt',setCanceled:v=>{event.cancelled=v}}
 const handler=h.native['io.redspace.ironsspellbooks.api.events.SpellPreCastEvent'][0]
 handler(event);assert.equal(event.cancelled,true)
 h.p.advancements.add('fantasia_research:fire_tier_1');event.cancelled=false;handler(event);assert.equal(event.cancelled,false)
 event.getSpellId=()=> 'irons_spellbooks:touch_dig';h.p.advancements.add('fantasia_research:nature_tier_3');h.p.advancements.add('fantasia_research:map_breaking_magic')
 handler(event);assert.equal(event.cancelled,true)
 let cleared=false;const explosion={getLevel:()=>h.p.level(),getAffectedBlocks:()=>({clear:()=>{cleared=true}})}
 h.native['net.neoforged.neoforge.event.level.ExplosionEvent$Detonate'][0](explosion);assert.ok(cleared)
})
test('research book requires nearby NPC, earned research, correct item and free slot',()=>{
 const h=harness();h.complete();h.p.near='noah'
 h.run('fantasia_magic','book');assert.equal(h.p.inventory.length,1);h.p.hand=h.p.inventory[0]
 h.run('fantasia_magic','book');assert.equal(h.p.inventory.length,1)
 h.p.advancements.add('fantasia_research:fire_tier_1')
 h.run('fantasia_magic','learn firebolt');assert.deepEqual(h.p.hand.container.spells,['irons_spellbooks:firebolt'])
 h.run('fantasia_magic','learn firebolt');assert.equal(h.p.hand.container.spells.length,1)
 h.run('fantasia_magic','learn blizzard');assert.equal(h.p.hand.container.spells.length,1)
 h.p.near='adeline';h.run('fantasia_magic','learn fireball');assert.equal(h.p.hand.container.spells.length,1)
})
test('scripts also boot without optional Iron/FTB mods and with optional safety core',()=>{
 for(const mods of [['kubejs'],['kubejs','irons_spellbooks','fantasia_core']]){
  const h=harness(mods);h.complete();h.run('fantasia_magic','')
  assert.ok(h.p.advancements.has('fantasia_research:exam/complete'))
  if(mods.includes('fantasia_core'))assert.equal(Object.keys(h.native).length,0)
 }
})

// This verifies scope isolation in Node; it does not emulate Rhino's evaluator.
test('magic Java bindings do not redeclare existing global names',()=>{
 const h=harness(['kubejs','irons_spellbooks'],
  'const FaResourceLocation=1; const FaSpellRegistry=2; const FaSpellContainer=3; const FANTASIA_SPELL_GATES=4;')
 assert.equal(typeof h.commands.fantasia_magic,'function')
 assert.equal(vm.runInContext('FaResourceLocation',h.scope),1)
 assert.equal(vm.runInContext('typeof faHasResearch',h.scope),'undefined')
})
