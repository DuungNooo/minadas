execute in fantasia:campaign run summon minecraft:text_display 1536 68 1584 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"실험체가 된 포로\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1584 65 1584 {Tags:["fa_exp_station","fa_exp_south_forge_4"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1584 68 1584 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"피의 장군\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1632 65 1584 {Tags:["fa_exp_station","fa_exp_south_forge_5"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1632 68 1584 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"남부 공명석\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run forceload remove 1520 1520 1648 1600
function fantasia:expansion/castle_memory/start
