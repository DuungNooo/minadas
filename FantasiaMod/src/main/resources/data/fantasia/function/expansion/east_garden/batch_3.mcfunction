execute in fantasia:campaign run fill 1360 64 1568 1392 64 1600 minecraft:mossy_stone_bricks
execute in fantasia:campaign run fill 1360 65 1568 1392 69 1568 minecraft:mossy_stone_bricks
execute in fantasia:campaign run fill 1360 65 1600 1392 69 1600 minecraft:mossy_stone_bricks
execute in fantasia:campaign run fill 1360 65 1568 1360 69 1600 minecraft:mossy_stone_bricks
execute in fantasia:campaign run fill 1392 65 1568 1392 69 1600 minecraft:mossy_stone_bricks
execute in fantasia:campaign run fill 1364 65 1572 1364 70 1572 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1364 71 1572 minecraft:sea_lantern
execute in fantasia:campaign run fill 1364 65 1596 1364 70 1596 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1364 71 1596 minecraft:sea_lantern
execute in fantasia:campaign run fill 1388 65 1572 1388 70 1572 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1388 71 1572 minecraft:sea_lantern
execute in fantasia:campaign run fill 1388 65 1596 1388 70 1596 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1388 71 1596 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1369 64 1584 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1376 64 1584 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1383 64 1584 minecraft:sea_lantern
execute in fantasia:campaign run fill 1366 65 1577 1366 67 1591 minecraft:bookshelf
execute in fantasia:campaign run fill 1386 65 1577 1386 67 1591 minecraft:bookshelf
execute in fantasia:campaign run setblock 1376 65 1577 minecraft:lectern
execute in fantasia:campaign run fill 1296 65 1534 1296 68 1538 minecraft:air
execute in fantasia:campaign run fill 1312 65 1534 1312 68 1538 minecraft:air
execute in fantasia:campaign run fill 1278 65 1552 1282 68 1552 minecraft:air
execute in fantasia:campaign run fill 1278 65 1568 1282 68 1568 minecraft:air
execute in fantasia:campaign run fill 1344 65 1534 1344 68 1538 minecraft:air
execute in fantasia:campaign run fill 1360 65 1534 1360 68 1538 minecraft:air
execute in fantasia:campaign run fill 1326 65 1552 1330 68 1552 minecraft:air
execute in fantasia:campaign run fill 1326 65 1568 1330 68 1568 minecraft:air
execute in fantasia:campaign run fill 1374 65 1552 1378 68 1552 minecraft:air
execute in fantasia:campaign run fill 1374 65 1568 1378 68 1568 minecraft:air
execute in fantasia:campaign run fill 1296 65 1582 1296 68 1586 minecraft:air
execute in fantasia:campaign run fill 1312 65 1582 1312 68 1586 minecraft:air
execute in fantasia:campaign run fill 1344 65 1582 1344 68 1586 minecraft:air
execute in fantasia:campaign run fill 1360 65 1582 1360 68 1586 minecraft:air
execute in fantasia:campaign run summon minecraft:interaction 1280 65 1536 {Tags:["fa_exp_station","fa_exp_east_garden_0"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1280 68 1536 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"독 안개의 끝\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1328 65 1536 {Tags:["fa_exp_station","fa_exp_east_garden_1"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1328 68 1536 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"정찰대의 흔적\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1376 65 1536 {Tags:["fa_exp_station","fa_exp_east_garden_2"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1376 68 1536 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"정화수 순환\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1280 65 1584 {Tags:["fa_exp_station","fa_exp_east_garden_3"],width:2.0f,height:2.5f,response:1b}
schedule function fantasia:expansion/east_garden/batch_4 1t replace
