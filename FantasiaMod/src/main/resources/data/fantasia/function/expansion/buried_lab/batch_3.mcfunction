execute in fantasia:campaign run fill 1360 64 1312 1392 64 1344 minecraft:polished_deepslate
execute in fantasia:campaign run fill 1360 65 1312 1392 69 1312 minecraft:polished_deepslate
execute in fantasia:campaign run fill 1360 65 1344 1392 69 1344 minecraft:polished_deepslate
execute in fantasia:campaign run fill 1360 65 1312 1360 69 1344 minecraft:polished_deepslate
execute in fantasia:campaign run fill 1392 65 1312 1392 69 1344 minecraft:polished_deepslate
execute in fantasia:campaign run fill 1364 65 1316 1364 70 1316 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1364 71 1316 minecraft:sea_lantern
execute in fantasia:campaign run fill 1364 65 1340 1364 70 1340 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1364 71 1340 minecraft:sea_lantern
execute in fantasia:campaign run fill 1388 65 1316 1388 70 1316 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1388 71 1316 minecraft:sea_lantern
execute in fantasia:campaign run fill 1388 65 1340 1388 70 1340 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1388 71 1340 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1369 64 1328 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1376 64 1328 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1383 64 1328 minecraft:sea_lantern
execute in fantasia:campaign run fill 1366 65 1321 1366 67 1335 minecraft:bookshelf
execute in fantasia:campaign run fill 1386 65 1321 1386 67 1335 minecraft:bookshelf
execute in fantasia:campaign run setblock 1376 65 1321 minecraft:lectern
execute in fantasia:campaign run fill 1296 65 1278 1296 68 1282 minecraft:air
execute in fantasia:campaign run fill 1312 65 1278 1312 68 1282 minecraft:air
execute in fantasia:campaign run fill 1278 65 1296 1282 68 1296 minecraft:air
execute in fantasia:campaign run fill 1278 65 1312 1282 68 1312 minecraft:air
execute in fantasia:campaign run fill 1344 65 1278 1344 68 1282 minecraft:air
execute in fantasia:campaign run fill 1360 65 1278 1360 68 1282 minecraft:air
execute in fantasia:campaign run fill 1326 65 1296 1330 68 1296 minecraft:air
execute in fantasia:campaign run fill 1326 65 1312 1330 68 1312 minecraft:air
execute in fantasia:campaign run fill 1374 65 1296 1378 68 1296 minecraft:air
execute in fantasia:campaign run fill 1374 65 1312 1378 68 1312 minecraft:air
execute in fantasia:campaign run fill 1296 65 1326 1296 68 1330 minecraft:air
execute in fantasia:campaign run fill 1312 65 1326 1312 68 1330 minecraft:air
execute in fantasia:campaign run fill 1344 65 1326 1344 68 1330 minecraft:air
execute in fantasia:campaign run fill 1360 65 1326 1360 68 1330 minecraft:air
execute in fantasia:campaign run summon minecraft:interaction 1280 65 1280 {Tags:["fa_exp_station","fa_exp_buried_lab_0"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1280 68 1280 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"폐쇄된 승강기\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1328 65 1280 {Tags:["fa_exp_station","fa_exp_buried_lab_1"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1328 68 1280 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"자동 경비대\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1376 65 1280 {Tags:["fa_exp_station","fa_exp_buried_lab_2"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1376 68 1280 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"연맹의 암호\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1280 65 1328 {Tags:["fa_exp_station","fa_exp_buried_lab_3"],width:2.0f,height:2.5f,response:1b}
schedule function fantasia:expansion/buried_lab/batch_4 1t replace
