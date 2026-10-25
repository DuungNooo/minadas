execute in fantasia:campaign run summon minecraft:text_display 1280 68 1328 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"기억의 증인\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1328 65 1328 {Tags:["fa_exp_station","fa_exp_buried_lab_4"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1328 68 1328 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"추출 장치\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1376 65 1328 {Tags:["fa_exp_station","fa_exp_buried_lab_5"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1376 68 1328 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"연맹의 대가\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run forceload remove 1264 1264 1392 1344
function fantasia:expansion/cult_hideout/start
