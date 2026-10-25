execute in fantasia:campaign run summon minecraft:text_display 1024 68 1584 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"고립된 정찰대\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1072 65 1584 {Tags:["fa_exp_station","fa_exp_north_watch_4"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1072 68 1584 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"백야의 장군\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1120 65 1584 {Tags:["fa_exp_station","fa_exp_north_watch_5"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1120 68 1584 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"북부 공명석\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run forceload remove 1008 1520 1136 1600
function fantasia:expansion/east_garden/start
