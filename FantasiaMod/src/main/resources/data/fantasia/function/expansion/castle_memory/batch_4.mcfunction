execute in fantasia:campaign run summon minecraft:text_display 1792 68 1584 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"기록을 지키는 자\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1840 65 1584 {Tags:["fa_exp_station","fa_exp_castle_memory_4"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1840 68 1584 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"장군의 잔재\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1888 65 1584 {Tags:["fa_exp_station","fa_exp_castle_memory_5"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1888 68 1584 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"왕좌 앞의 기록\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run forceload remove 1776 1520 1904 1600
scoreboard players set #exp_ready fa_world 1
tellraw @a {"text":"추가 원정 지역 준비 완료. NPC의 원정 메뉴를 확인하세요.","color":"green"}
