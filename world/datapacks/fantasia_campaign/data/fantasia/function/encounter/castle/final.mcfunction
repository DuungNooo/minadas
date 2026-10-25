scoreboard players set #wave_castle fa_world 3
scoreboard players set #kills_castle fa_world 0
scoreboard players set #need_castle fa_world 3
bossbar set fantasia:belkarion value 1
summon minecraft:husk 320 65 180 {Tags:["fa_enemy","fa_enemy_castle"],PersistenceRequired:1b,Health:140.0f,Attributes:[{Name:"minecraft:generic.max_health",Base:140.0d},{Name:"minecraft:generic.movement_speed",Base:0.27d}],CustomName:'{"text":"벨카리온 · 최후의 폭주","color":"dark_red"}',CustomNameVisible:1b,HandItems:[{id:"minecraft:iron_axe",count:1},{}],ArmorItems:[{},{},{id:"minecraft:iron_chestplate",count:1},{id:"minecraft:iron_helmet",count:1}],HandDropChances:[0.0f,0.0f],ArmorDropChances:[0.0f,0.0f,0.0f,0.0f]}
summon minecraft:skeleton 314 65 176 {Tags:["fa_enemy","fa_enemy_castle"],PersistenceRequired:1b,HandItems:[{id:"minecraft:bow",count:1},{}],ArmorItems:[{},{},{},{id:"minecraft:iron_helmet",count:1}]}
summon minecraft:skeleton 326 65 176 {Tags:["fa_enemy","fa_enemy_castle"],PersistenceRequired:1b,HandItems:[{id:"minecraft:bow",count:1},{}],ArmorItems:[{},{},{},{id:"minecraft:iron_helmet",count:1}]}
execute as @a[tag=fa_in_castle] run tellraw @s {"text":"최후의 폭주! 왕과 두 호위병을 모두 쓰러뜨리세요.","color":"red"}
