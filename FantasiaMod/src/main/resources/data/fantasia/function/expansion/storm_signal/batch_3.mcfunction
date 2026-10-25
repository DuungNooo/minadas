execute in fantasia:campaign run fill 1104 64 1312 1136 64 1344 minecraft:cut_copper
execute in fantasia:campaign run fill 1104 65 1312 1136 69 1312 minecraft:cut_copper
execute in fantasia:campaign run fill 1104 65 1344 1136 69 1344 minecraft:cut_copper
execute in fantasia:campaign run fill 1104 65 1312 1104 69 1344 minecraft:cut_copper
execute in fantasia:campaign run fill 1136 65 1312 1136 69 1344 minecraft:cut_copper
execute in fantasia:campaign run fill 1108 65 1316 1108 70 1316 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1108 71 1316 minecraft:sea_lantern
execute in fantasia:campaign run fill 1108 65 1340 1108 70 1340 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1108 71 1340 minecraft:sea_lantern
execute in fantasia:campaign run fill 1132 65 1316 1132 70 1316 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1132 71 1316 minecraft:sea_lantern
execute in fantasia:campaign run fill 1132 65 1340 1132 70 1340 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1132 71 1340 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1113 64 1328 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1120 64 1328 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1127 64 1328 minecraft:sea_lantern
execute in fantasia:campaign run fill 1110 65 1321 1110 67 1335 minecraft:bookshelf
execute in fantasia:campaign run fill 1130 65 1321 1130 67 1335 minecraft:bookshelf
execute in fantasia:campaign run setblock 1120 65 1321 minecraft:lectern
execute in fantasia:campaign run fill 1040 65 1278 1040 68 1282 minecraft:air
execute in fantasia:campaign run fill 1056 65 1278 1056 68 1282 minecraft:air
execute in fantasia:campaign run fill 1022 65 1296 1026 68 1296 minecraft:air
execute in fantasia:campaign run fill 1022 65 1312 1026 68 1312 minecraft:air
execute in fantasia:campaign run fill 1088 65 1278 1088 68 1282 minecraft:air
execute in fantasia:campaign run fill 1104 65 1278 1104 68 1282 minecraft:air
execute in fantasia:campaign run fill 1070 65 1296 1074 68 1296 minecraft:air
execute in fantasia:campaign run fill 1070 65 1312 1074 68 1312 minecraft:air
execute in fantasia:campaign run fill 1118 65 1296 1122 68 1296 minecraft:air
execute in fantasia:campaign run fill 1118 65 1312 1122 68 1312 minecraft:air
execute in fantasia:campaign run fill 1040 65 1326 1040 68 1330 minecraft:air
execute in fantasia:campaign run fill 1056 65 1326 1056 68 1330 minecraft:air
execute in fantasia:campaign run fill 1088 65 1326 1088 68 1330 minecraft:air
execute in fantasia:campaign run fill 1104 65 1326 1104 68 1330 minecraft:air
execute in fantasia:campaign run summon minecraft:interaction 1024 65 1280 {Tags:["fa_exp_station","fa_exp_storm_signal_0"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1024 68 1280 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"끊어진 중계선\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1072 65 1280 {Tags:["fa_exp_station","fa_exp_storm_signal_1"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1072 68 1280 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"움직이는 전장\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1120 65 1280 {Tags:["fa_exp_station","fa_exp_storm_signal_2"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1120 68 1280 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"세 개의 피뢰침\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1024 65 1328 {Tags:["fa_exp_station","fa_exp_storm_signal_3"],width:2.0f,height:2.5f,response:1b}
schedule function fantasia:expansion/storm_signal/batch_4 1t replace
