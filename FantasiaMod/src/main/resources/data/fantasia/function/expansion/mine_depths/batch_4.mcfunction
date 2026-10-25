execute in fantasia:campaign run summon minecraft:text_display 1280 68 1072 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"갇힌 광부들\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1328 65 1072 {Tags:["fa_exp_station","fa_exp_mine_depths_4"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1328 68 1072 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"불씨를 먹는 수호자\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1376 65 1072 {Tags:["fa_exp_station","fa_exp_mine_depths_5"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1376 68 1072 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"교수의 표본함\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run forceload remove 1264 1008 1392 1088
function fantasia:expansion/canal_rescue/start
