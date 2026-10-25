execute in fantasia:campaign run fill 1104 64 1568 1136 64 1600 minecraft:polished_andesite
execute in fantasia:campaign run fill 1104 65 1568 1136 69 1568 minecraft:packed_ice
execute in fantasia:campaign run fill 1104 65 1600 1136 69 1600 minecraft:packed_ice
execute in fantasia:campaign run fill 1104 65 1568 1104 69 1600 minecraft:packed_ice
execute in fantasia:campaign run fill 1136 65 1568 1136 69 1600 minecraft:packed_ice
execute in fantasia:campaign run fill 1108 65 1572 1108 70 1572 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1108 71 1572 minecraft:sea_lantern
execute in fantasia:campaign run fill 1108 65 1596 1108 70 1596 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1108 71 1596 minecraft:sea_lantern
execute in fantasia:campaign run fill 1132 65 1572 1132 70 1572 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1132 71 1572 minecraft:sea_lantern
execute in fantasia:campaign run fill 1132 65 1596 1132 70 1596 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1132 71 1596 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1113 64 1584 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1120 64 1584 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1127 64 1584 minecraft:sea_lantern
execute in fantasia:campaign run fill 1110 65 1577 1110 67 1591 minecraft:bookshelf
execute in fantasia:campaign run fill 1130 65 1577 1130 67 1591 minecraft:bookshelf
execute in fantasia:campaign run setblock 1120 65 1577 minecraft:lectern
execute in fantasia:campaign run fill 1040 65 1534 1040 68 1538 minecraft:air
execute in fantasia:campaign run fill 1056 65 1534 1056 68 1538 minecraft:air
execute in fantasia:campaign run fill 1022 65 1552 1026 68 1552 minecraft:air
execute in fantasia:campaign run fill 1022 65 1568 1026 68 1568 minecraft:air
execute in fantasia:campaign run fill 1088 65 1534 1088 68 1538 minecraft:air
execute in fantasia:campaign run fill 1104 65 1534 1104 68 1538 minecraft:air
execute in fantasia:campaign run fill 1070 65 1552 1074 68 1552 minecraft:air
execute in fantasia:campaign run fill 1070 65 1568 1074 68 1568 minecraft:air
execute in fantasia:campaign run fill 1118 65 1552 1122 68 1552 minecraft:air
execute in fantasia:campaign run fill 1118 65 1568 1122 68 1568 minecraft:air
execute in fantasia:campaign run fill 1040 65 1582 1040 68 1586 minecraft:air
execute in fantasia:campaign run fill 1056 65 1582 1056 68 1586 minecraft:air
execute in fantasia:campaign run fill 1088 65 1582 1088 68 1586 minecraft:air
execute in fantasia:campaign run fill 1104 65 1582 1104 68 1586 minecraft:air
execute in fantasia:campaign run summon minecraft:interaction 1024 65 1536 {Tags:["fa_exp_station","fa_exp_north_watch_0"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1024 68 1536 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"멈춘 관측소\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1072 65 1536 {Tags:["fa_exp_station","fa_exp_north_watch_1"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1072 68 1536 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"얼음 속의 균열\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1120 65 1536 {Tags:["fa_exp_station","fa_exp_north_watch_2"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1120 68 1536 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"등대의 빛\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1024 65 1584 {Tags:["fa_exp_station","fa_exp_north_watch_3"],width:2.0f,height:2.5f,response:1b}
schedule function fantasia:expansion/north_watch/batch_4 1t replace
