kill @e[tag=fa_npc]
kill @e[tag=fa_station]
kill @e[tag=fa_label]
gamerule keepInventory true
gamerule mobGriefing false
gamerule doFireTick false
gamerule doMobSpawning false
difficulty normal
team add fa_npcs
team modify fa_npcs collisionRule never
summon minecraft:villager 0 65 0 {Tags:["fa_npc","fa_npc_adeline"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomName:"{\"text\":\"아델린 · 안내\",\"color\":\"gold\"}",CustomNameVisible:1b,VillagerData:{type:"minecraft:plains",profession:"minecraft:librarian",level:5},Offers:{Recipes:[]}}
summon minecraft:villager 6 65 0 {Tags:["fa_npc","fa_npc_kyle"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomName:"{\"text\":\"카일 · 훈련과 보급\",\"color\":\"gold\"}",CustomNameVisible:1b,VillagerData:{type:"minecraft:plains",profession:"minecraft:librarian",level:5},Offers:{Recipes:[]}}
summon minecraft:villager -6 65 0 {Tags:["fa_npc","fa_npc_seraphine"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomName:"{\"text\":\"세라핀 · 치료\",\"color\":\"gold\"}",CustomNameVisible:1b,VillagerData:{type:"minecraft:plains",profession:"minecraft:librarian",level:5},Offers:{Recipes:[]}}
summon minecraft:villager 0 65 8 {Tags:["fa_npc","fa_npc_noah"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomName:"{\"text\":\"노아 · 연구\",\"color\":\"gold\"}",CustomNameVisible:1b,VillagerData:{type:"minecraft:plains",profession:"minecraft:librarian",level:5},Offers:{Recipes:[]}}
summon minecraft:villager 160 65 -14 {Tags:["fa_npc","fa_npc_irina"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomName:"{\"text\":\"이리나 · 불타는 광산\",\"color\":\"gold\"}",CustomNameVisible:1b,VillagerData:{type:"minecraft:plains",profession:"minecraft:librarian",level:5},Offers:{Recipes:[]}}
summon minecraft:villager 0 65 146 {Tags:["fa_npc","fa_npc_riana"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomName:"{\"text\":\"리아나 · 얼어붙은 수로\",\"color\":\"gold\"}",CustomNameVisible:1b,VillagerData:{type:"minecraft:plains",profession:"minecraft:librarian",level:5},Offers:{Recipes:[]}}
summon minecraft:villager -160 65 -14 {Tags:["fa_npc","fa_npc_rowen"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomName:"{\"text\":\"로웬 · 침식된 숲\",\"color\":\"gold\"}",CustomNameVisible:1b,VillagerData:{type:"minecraft:plains",profession:"minecraft:librarian",level:5},Offers:{Recipes:[]}}
summon minecraft:villager 0 65 -174 {Tags:["fa_npc","fa_npc_theo"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomName:"{\"text\":\"테오 · 낙뢰 평원\",\"color\":\"gold\"}",CustomNameVisible:1b,VillagerData:{type:"minecraft:plains",profession:"minecraft:librarian",level:5},Offers:{Recipes:[]}}
summon minecraft:villager 160 65 146 {Tags:["fa_npc","fa_npc_rachel"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomName:"{\"text\":\"라헬 · 봉인서고\",\"color\":\"gold\"}",CustomNameVisible:1b,VillagerData:{type:"minecraft:plains",profession:"minecraft:librarian",level:5},Offers:{Recipes:[]}}
summon minecraft:villager -160 65 146 {Tags:["fa_npc","fa_npc_edric"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomName:"{\"text\":\"에드릭 · 수도 방어\",\"color\":\"gold\"}",CustomNameVisible:1b,VillagerData:{type:"minecraft:plains",profession:"minecraft:librarian",level:5},Offers:{Recipes:[]}}
summon minecraft:villager -160 65 -174 {Tags:["fa_npc","fa_npc_elena"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomName:"{\"text\":\"엘레나 · 북부 전선\",\"color\":\"gold\"}",CustomNameVisible:1b,VillagerData:{type:"minecraft:plains",profession:"minecraft:librarian",level:5},Offers:{Recipes:[]}}
summon minecraft:villager 160 65 -174 {Tags:["fa_npc","fa_npc_claude"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomName:"{\"text\":\"클라우드 · 동부 전선\",\"color\":\"gold\"}",CustomNameVisible:1b,VillagerData:{type:"minecraft:plains",profession:"minecraft:librarian",level:5},Offers:{Recipes:[]}}
summon minecraft:villager 320 65 -14 {Tags:["fa_npc","fa_npc_bernard"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomName:"{\"text\":\"베른하르트 · 남부 전선\",\"color\":\"gold\"}",CustomNameVisible:1b,VillagerData:{type:"minecraft:plains",profession:"minecraft:librarian",level:5},Offers:{Recipes:[]}}
summon minecraft:villager 320 65 140 {Tags:["fa_npc","fa_npc_headmaster"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomName:"{\"text\":\"헤론 · 마왕성\",\"color\":\"gold\"}",CustomNameVisible:1b,VillagerData:{type:"minecraft:plains",profession:"minecraft:librarian",level:5},Offers:{Recipes:[]}}
summon minecraft:interaction 152 65 0 {Tags:["fa_station","fa_station_miner"],width:1.8f,height:2.0f,response:1b}
summon minecraft:text_display 152 67.2 0 {Tags:["fa_label"],billboard:"center",alignment:"center",background:1073741824,text:"{\"text\":\"구조를 기다리는 광부\",\"color\":\"aqua\"}"}
summon minecraft:interaction 168 65 0 {Tags:["fa_station","fa_station_fire_core"],width:1.8f,height:2.0f,response:1b}
summon minecraft:text_display 168 67.2 0 {Tags:["fa_label"],billboard:"center",alignment:"center",background:1073741824,text:"{\"text\":\"화염 마력핵\",\"color\":\"aqua\"}"}
summon minecraft:interaction -8 65 160 {Tags:["fa_station","fa_station_canal_west"],width:1.8f,height:2.0f,response:1b}
summon minecraft:text_display -8 67.2 160 {Tags:["fa_label"],billboard:"center",alignment:"center",background:1073741824,text:"{\"text\":\"서쪽 · 수문\",\"color\":\"aqua\"}"}
summon minecraft:interaction 8 65 160 {Tags:["fa_station","fa_station_canal_east"],width:1.8f,height:2.0f,response:1b}
summon minecraft:text_display 8 67.2 160 {Tags:["fa_label"],billboard:"center",alignment:"center",background:1073741824,text:"{\"text\":\"동쪽 · 수문\",\"color\":\"aqua\"}"}
summon minecraft:interaction 0 65 155 {Tags:["fa_station","fa_station_canal_center"],width:1.8f,height:2.0f,response:1b}
summon minecraft:text_display 0 67.2 155 {Tags:["fa_label"],billboard:"center",alignment:"center",background:1073741824,text:"{\"text\":\"중앙 · 수문\",\"color\":\"aqua\"}"}
summon minecraft:interaction -168 65 0 {Tags:["fa_station","fa_station_forest_west"],width:1.8f,height:2.0f,response:1b}
summon minecraft:text_display -168 67.2 0 {Tags:["fa_label"],billboard:"center",alignment:"center",background:1073741824,text:"{\"text\":\"서쪽 · 정화석\",\"color\":\"aqua\"}"}
summon minecraft:interaction -152 65 0 {Tags:["fa_station","fa_station_forest_east"],width:1.8f,height:2.0f,response:1b}
summon minecraft:text_display -152 67.2 0 {Tags:["fa_label"],billboard:"center",alignment:"center",background:1073741824,text:"{\"text\":\"동쪽 · 정화석\",\"color\":\"aqua\"}"}
summon minecraft:interaction -160 65 -5 {Tags:["fa_station","fa_station_forest_center"],width:1.8f,height:2.0f,response:1b}
summon minecraft:text_display -160 67.2 -5 {Tags:["fa_label"],billboard:"center",alignment:"center",background:1073741824,text:"{\"text\":\"중앙 · 정화석\",\"color\":\"aqua\"}"}
summon minecraft:interaction -8 65 -160 {Tags:["fa_station","fa_station_storm_west"],width:1.8f,height:2.0f,response:1b}
summon minecraft:text_display -8 67.2 -160 {Tags:["fa_label"],billboard:"center",alignment:"center",background:1073741824,text:"{\"text\":\"서쪽 · 집전기\",\"color\":\"aqua\"}"}
summon minecraft:interaction 8 65 -160 {Tags:["fa_station","fa_station_storm_east"],width:1.8f,height:2.0f,response:1b}
summon minecraft:text_display 8 67.2 -160 {Tags:["fa_label"],billboard:"center",alignment:"center",background:1073741824,text:"{\"text\":\"동쪽 · 집전기\",\"color\":\"aqua\"}"}
summon minecraft:interaction 0 65 -165 {Tags:["fa_station","fa_station_storm_center"],width:1.8f,height:2.0f,response:1b}
summon minecraft:text_display 0 67.2 -165 {Tags:["fa_label"],billboard:"center",alignment:"center",background:1073741824,text:"{\"text\":\"중앙 · 집전기\",\"color\":\"aqua\"}"}
summon minecraft:interaction 152 65 160 {Tags:["fa_station","fa_station_archive_west"],width:1.8f,height:2.0f,response:1b}
summon minecraft:text_display 152 67.2 160 {Tags:["fa_label"],billboard:"center",alignment:"center",background:1073741824,text:"{\"text\":\"옛 연맹의 기록\",\"color\":\"aqua\"}"}
summon minecraft:interaction 168 65 160 {Tags:["fa_station","fa_station_archive_east"],width:1.8f,height:2.0f,response:1b}
summon minecraft:text_display 168 67.2 160 {Tags:["fa_label"],billboard:"center",alignment:"center",background:1073741824,text:"{\"text\":\"마력 실험 기록\",\"color\":\"aqua\"}"}
summon minecraft:interaction 160 65 155 {Tags:["fa_station","fa_station_archive_center"],width:1.8f,height:2.0f,response:1b}
summon minecraft:text_display 160 67.2 155 {Tags:["fa_label"],billboard:"center",alignment:"center",background:1073741824,text:"{\"text\":\"베른하르트의 편지\",\"color\":\"aqua\"}"}
summon minecraft:interaction 310 65 175 {Tags:["fa_station","fa_station_seal_west"],width:1.8f,height:2.0f,response:1b}
summon minecraft:text_display 310 67.2 175 {Tags:["fa_label"],billboard:"center",alignment:"center",background:1073741824,text:"{\"text\":\"서쪽 봉인석 · 붕괴 단계에 가동\",\"color\":\"aqua\"}"}
summon minecraft:interaction 330 65 175 {Tags:["fa_station","fa_station_seal_east"],width:1.8f,height:2.0f,response:1b}
summon minecraft:text_display 330 67.2 175 {Tags:["fa_label"],billboard:"center",alignment:"center",background:1073741824,text:"{\"text\":\"동쪽 봉인석 · 붕괴 단계에 가동\",\"color\":\"aqua\"}"}
team join fa_npcs @e[tag=fa_npc]
forceload remove -176 0
forceload remove -160 -176
forceload remove -160 -16
forceload remove -160 0
forceload remove -160 144
forceload remove -16 -160
forceload remove -16 0
forceload remove -16 160
forceload remove 0 -176
forceload remove 0 -160
forceload remove 0 0
forceload remove 0 144
forceload remove 0 160
forceload remove 144 0
forceload remove 144 160
forceload remove 160 -176
forceload remove 160 -16
forceload remove 160 0
forceload remove 160 144
forceload remove 160 160
forceload remove 304 160
forceload remove 320 -16
forceload remove 320 128
forceload remove 320 160
scoreboard players set #npcs fa_world 1
