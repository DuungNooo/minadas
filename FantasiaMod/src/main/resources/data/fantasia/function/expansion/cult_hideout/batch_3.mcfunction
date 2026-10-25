execute in fantasia:campaign run fill 1616 64 1312 1648 64 1344 minecraft:polished_blackstone_bricks
execute in fantasia:campaign run fill 1616 65 1312 1648 69 1312 minecraft:polished_blackstone_bricks
execute in fantasia:campaign run fill 1616 65 1344 1648 69 1344 minecraft:polished_blackstone_bricks
execute in fantasia:campaign run fill 1616 65 1312 1616 69 1344 minecraft:polished_blackstone_bricks
execute in fantasia:campaign run fill 1648 65 1312 1648 69 1344 minecraft:polished_blackstone_bricks
execute in fantasia:campaign run fill 1620 65 1316 1620 70 1316 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1620 71 1316 minecraft:sea_lantern
execute in fantasia:campaign run fill 1620 65 1340 1620 70 1340 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1620 71 1340 minecraft:sea_lantern
execute in fantasia:campaign run fill 1644 65 1316 1644 70 1316 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1644 71 1316 minecraft:sea_lantern
execute in fantasia:campaign run fill 1644 65 1340 1644 70 1340 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1644 71 1340 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1625 64 1328 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1632 64 1328 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1639 64 1328 minecraft:sea_lantern
execute in fantasia:campaign run fill 1622 65 1321 1622 67 1335 minecraft:bookshelf
execute in fantasia:campaign run fill 1642 65 1321 1642 67 1335 minecraft:bookshelf
execute in fantasia:campaign run setblock 1632 65 1321 minecraft:lectern
execute in fantasia:campaign run fill 1552 65 1278 1552 68 1282 minecraft:air
execute in fantasia:campaign run fill 1568 65 1278 1568 68 1282 minecraft:air
execute in fantasia:campaign run fill 1534 65 1296 1538 68 1296 minecraft:air
execute in fantasia:campaign run fill 1534 65 1312 1538 68 1312 minecraft:air
execute in fantasia:campaign run fill 1600 65 1278 1600 68 1282 minecraft:air
execute in fantasia:campaign run fill 1616 65 1278 1616 68 1282 minecraft:air
execute in fantasia:campaign run fill 1582 65 1296 1586 68 1296 minecraft:air
execute in fantasia:campaign run fill 1582 65 1312 1586 68 1312 minecraft:air
execute in fantasia:campaign run fill 1630 65 1296 1634 68 1296 minecraft:air
execute in fantasia:campaign run fill 1630 65 1312 1634 68 1312 minecraft:air
execute in fantasia:campaign run fill 1552 65 1326 1552 68 1330 minecraft:air
execute in fantasia:campaign run fill 1568 65 1326 1568 68 1330 minecraft:air
execute in fantasia:campaign run fill 1600 65 1326 1600 68 1330 minecraft:air
execute in fantasia:campaign run fill 1616 65 1326 1616 68 1330 minecraft:air
execute in fantasia:campaign run summon minecraft:interaction 1536 65 1280 {Tags:["fa_exp_station","fa_exp_cult_hideout_0"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1536 68 1280 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"밀수꾼의 통로\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1584 65 1280 {Tags:["fa_exp_station","fa_exp_cult_hideout_1"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1584 68 1280 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"인장 없는 경비\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1632 65 1280 {Tags:["fa_exp_station","fa_exp_cult_hideout_2"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1632 68 1280 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"감옥의 잠금장치\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1536 65 1328 {Tags:["fa_exp_station","fa_exp_cult_hideout_3"],width:2.0f,height:2.5f,response:1b}
schedule function fantasia:expansion/cult_hideout/batch_4 1t replace
