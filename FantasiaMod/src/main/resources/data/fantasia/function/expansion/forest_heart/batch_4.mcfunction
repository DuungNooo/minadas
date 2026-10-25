execute in fantasia:campaign run summon minecraft:text_display 1792 68 1072 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"숲지기의 길\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1840 65 1072 {Tags:["fa_exp_station","fa_exp_forest_heart_4"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1840 68 1072 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"검은 뿌리\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1888 65 1072 {Tags:["fa_exp_station","fa_exp_forest_heart_5"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1888 68 1072 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"숨겨진 배관\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run forceload remove 1776 1008 1904 1088
function fantasia:expansion/storm_signal/start
