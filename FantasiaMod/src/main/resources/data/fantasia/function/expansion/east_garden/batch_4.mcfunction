execute in fantasia:campaign run summon minecraft:text_display 1280 68 1584 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"약초사의 길\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1328 65 1584 {Tags:["fa_exp_station","fa_exp_east_garden_4"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1328 68 1584 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"시든 정원의 장군\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1376 65 1584 {Tags:["fa_exp_station","fa_exp_east_garden_5"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1376 68 1584 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"동부 공명석\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run forceload remove 1264 1520 1392 1600
function fantasia:expansion/south_forge/start
