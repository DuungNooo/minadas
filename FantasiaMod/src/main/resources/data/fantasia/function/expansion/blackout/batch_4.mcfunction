execute in fantasia:campaign run summon minecraft:text_display 1024 68 1072 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"문 너머의 조교\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1072 65 1072 {Tags:["fa_exp_station","fa_exp_blackout_4"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1072 68 1072 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"봉인실의 침입자\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1120 65 1072 {Tags:["fa_exp_station","fa_exp_blackout_5"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1120 68 1072 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"첫 번째 균열\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run forceload remove 1008 1008 1136 1088
function fantasia:expansion/mine_depths/start
