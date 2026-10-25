execute in fantasia:campaign run summon minecraft:text_display 1536 68 1072 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"물속의 신호\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1584 65 1072 {Tags:["fa_exp_station","fa_exp_canal_rescue_4"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1584 68 1072 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"얼어붙은 펌프실\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1632 65 1072 {Tags:["fa_exp_station","fa_exp_canal_rescue_5"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1632 68 1072 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"누가 수문을 닫았는가\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run forceload remove 1520 1008 1648 1088
function fantasia:expansion/forest_heart/start
