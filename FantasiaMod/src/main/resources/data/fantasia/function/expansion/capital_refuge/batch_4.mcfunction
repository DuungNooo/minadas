execute in fantasia:campaign run summon minecraft:text_display 1792 68 1328 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"마지막 피난민\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1840 65 1328 {Tags:["fa_exp_station","fa_exp_capital_refuge_4"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1840 68 1328 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"공성 지휘관\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1888 65 1328 {Tags:["fa_exp_station","fa_exp_capital_refuge_5"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1888 68 1328 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"지키는 이유\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run forceload remove 1776 1264 1904 1344
function fantasia:expansion/north_watch/start
