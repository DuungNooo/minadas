execute in fantasia:campaign run summon minecraft:text_display 1024 68 1328 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"연구자의 귀환\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1072 65 1328 {Tags:["fa_exp_station","fa_exp_storm_signal_4"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1072 68 1328 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"폭풍의 전령\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1120 65 1328 {Tags:["fa_exp_station","fa_exp_storm_signal_5"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1120 68 1328 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"마지막 발신자\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run forceload remove 1008 1264 1136 1344
function fantasia:expansion/buried_lab/start
