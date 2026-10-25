execute in fantasia:campaign run fill 1360 64 1056 1392 64 1088 minecraft:deepslate_tiles
execute in fantasia:campaign run fill 1360 65 1056 1392 69 1056 minecraft:deepslate_tiles
execute in fantasia:campaign run fill 1360 65 1088 1392 69 1088 minecraft:deepslate_tiles
execute in fantasia:campaign run fill 1360 65 1056 1360 69 1088 minecraft:deepslate_tiles
execute in fantasia:campaign run fill 1392 65 1056 1392 69 1088 minecraft:deepslate_tiles
execute in fantasia:campaign run fill 1364 65 1060 1364 70 1060 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1364 71 1060 minecraft:sea_lantern
execute in fantasia:campaign run fill 1364 65 1084 1364 70 1084 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1364 71 1084 minecraft:sea_lantern
execute in fantasia:campaign run fill 1388 65 1060 1388 70 1060 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1388 71 1060 minecraft:sea_lantern
execute in fantasia:campaign run fill 1388 65 1084 1388 70 1084 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1388 71 1084 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1369 64 1072 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1376 64 1072 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1383 64 1072 minecraft:sea_lantern
execute in fantasia:campaign run fill 1366 65 1065 1366 67 1079 minecraft:bookshelf
execute in fantasia:campaign run fill 1386 65 1065 1386 67 1079 minecraft:bookshelf
execute in fantasia:campaign run setblock 1376 65 1065 minecraft:lectern
execute in fantasia:campaign run fill 1296 65 1022 1296 68 1026 minecraft:air
execute in fantasia:campaign run fill 1312 65 1022 1312 68 1026 minecraft:air
execute in fantasia:campaign run fill 1278 65 1040 1282 68 1040 minecraft:air
execute in fantasia:campaign run fill 1278 65 1056 1282 68 1056 minecraft:air
execute in fantasia:campaign run fill 1344 65 1022 1344 68 1026 minecraft:air
execute in fantasia:campaign run fill 1360 65 1022 1360 68 1026 minecraft:air
execute in fantasia:campaign run fill 1326 65 1040 1330 68 1040 minecraft:air
execute in fantasia:campaign run fill 1326 65 1056 1330 68 1056 minecraft:air
execute in fantasia:campaign run fill 1374 65 1040 1378 68 1040 minecraft:air
execute in fantasia:campaign run fill 1374 65 1056 1378 68 1056 minecraft:air
execute in fantasia:campaign run fill 1296 65 1070 1296 68 1074 minecraft:air
execute in fantasia:campaign run fill 1312 65 1070 1312 68 1074 minecraft:air
execute in fantasia:campaign run fill 1344 65 1070 1344 68 1074 minecraft:air
execute in fantasia:campaign run fill 1360 65 1070 1360 68 1074 minecraft:air
execute in fantasia:campaign run summon minecraft:interaction 1280 65 1024 {Tags:["fa_exp_station","fa_exp_mine_depths_0"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1280 68 1024 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"사라진 교대표\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1328 65 1024 {Tags:["fa_exp_station","fa_exp_mine_depths_1"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1328 68 1024 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"잿빛 운반로\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1376 65 1024 {Tags:["fa_exp_station","fa_exp_mine_depths_2"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1376 68 1024 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"압력 조절실\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1280 65 1072 {Tags:["fa_exp_station","fa_exp_mine_depths_3"],width:2.0f,height:2.5f,response:1b}
schedule function fantasia:expansion/mine_depths/batch_4 1t replace
