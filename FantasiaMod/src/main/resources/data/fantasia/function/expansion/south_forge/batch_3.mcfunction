execute in fantasia:campaign run fill 1616 64 1568 1648 64 1600 minecraft:nether_bricks
execute in fantasia:campaign run fill 1616 65 1568 1648 69 1568 minecraft:nether_bricks
execute in fantasia:campaign run fill 1616 65 1600 1648 69 1600 minecraft:nether_bricks
execute in fantasia:campaign run fill 1616 65 1568 1616 69 1600 minecraft:nether_bricks
execute in fantasia:campaign run fill 1648 65 1568 1648 69 1600 minecraft:nether_bricks
execute in fantasia:campaign run fill 1620 65 1572 1620 70 1572 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1620 71 1572 minecraft:sea_lantern
execute in fantasia:campaign run fill 1620 65 1596 1620 70 1596 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1620 71 1596 minecraft:sea_lantern
execute in fantasia:campaign run fill 1644 65 1572 1644 70 1572 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1644 71 1572 minecraft:sea_lantern
execute in fantasia:campaign run fill 1644 65 1596 1644 70 1596 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1644 71 1596 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1625 64 1584 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1632 64 1584 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1639 64 1584 minecraft:sea_lantern
execute in fantasia:campaign run fill 1622 65 1577 1622 67 1591 minecraft:bookshelf
execute in fantasia:campaign run fill 1642 65 1577 1642 67 1591 minecraft:bookshelf
execute in fantasia:campaign run setblock 1632 65 1577 minecraft:lectern
execute in fantasia:campaign run fill 1552 65 1534 1552 68 1538 minecraft:air
execute in fantasia:campaign run fill 1568 65 1534 1568 68 1538 minecraft:air
execute in fantasia:campaign run fill 1534 65 1552 1538 68 1552 minecraft:air
execute in fantasia:campaign run fill 1534 65 1568 1538 68 1568 minecraft:air
execute in fantasia:campaign run fill 1600 65 1534 1600 68 1538 minecraft:air
execute in fantasia:campaign run fill 1616 65 1534 1616 68 1538 minecraft:air
execute in fantasia:campaign run fill 1582 65 1552 1586 68 1552 minecraft:air
execute in fantasia:campaign run fill 1582 65 1568 1586 68 1568 minecraft:air
execute in fantasia:campaign run fill 1630 65 1552 1634 68 1552 minecraft:air
execute in fantasia:campaign run fill 1630 65 1568 1634 68 1568 minecraft:air
execute in fantasia:campaign run fill 1552 65 1582 1552 68 1586 minecraft:air
execute in fantasia:campaign run fill 1568 65 1582 1568 68 1586 minecraft:air
execute in fantasia:campaign run fill 1600 65 1582 1600 68 1586 minecraft:air
execute in fantasia:campaign run fill 1616 65 1582 1616 68 1586 minecraft:air
execute in fantasia:campaign run summon minecraft:interaction 1536 65 1536 {Tags:["fa_exp_station","fa_exp_south_forge_0"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1536 68 1536 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"비어 있는 병기고\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1584 65 1536 {Tags:["fa_exp_station","fa_exp_south_forge_1"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1584 68 1536 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"붉은 제련로\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1632 65 1536 {Tags:["fa_exp_station","fa_exp_south_forge_2"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1632 68 1536 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"열 교환 장치\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1536 65 1584 {Tags:["fa_exp_station","fa_exp_south_forge_3"],width:2.0f,height:2.5f,response:1b}
schedule function fantasia:expansion/south_forge/batch_4 1t replace
