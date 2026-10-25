execute in fantasia:campaign run summon minecraft:text_display 1536 68 1328 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"베른하르트 구출\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1584 65 1328 {Tags:["fa_exp_station","fa_exp_cult_hideout_4"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1584 68 1328 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"교단의 집행자\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1632 65 1328 {Tags:["fa_exp_station","fa_exp_cult_hideout_5"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1632 68 1328 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"다른 봉인법\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run forceload remove 1520 1264 1648 1344
function fantasia:expansion/capital_refuge/start
