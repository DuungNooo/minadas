execute in fantasia:campaign run fill 1616 64 1056 1648 64 1088 minecraft:prismarine_bricks
execute in fantasia:campaign run fill 1616 65 1056 1648 69 1056 minecraft:prismarine_bricks
execute in fantasia:campaign run fill 1616 65 1088 1648 69 1088 minecraft:prismarine_bricks
execute in fantasia:campaign run fill 1616 65 1056 1616 69 1088 minecraft:prismarine_bricks
execute in fantasia:campaign run fill 1648 65 1056 1648 69 1088 minecraft:prismarine_bricks
execute in fantasia:campaign run fill 1620 65 1060 1620 70 1060 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1620 71 1060 minecraft:sea_lantern
execute in fantasia:campaign run fill 1620 65 1084 1620 70 1084 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1620 71 1084 minecraft:sea_lantern
execute in fantasia:campaign run fill 1644 65 1060 1644 70 1060 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1644 71 1060 minecraft:sea_lantern
execute in fantasia:campaign run fill 1644 65 1084 1644 70 1084 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1644 71 1084 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1625 64 1072 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1632 64 1072 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1639 64 1072 minecraft:sea_lantern
execute in fantasia:campaign run fill 1622 65 1065 1622 67 1079 minecraft:bookshelf
execute in fantasia:campaign run fill 1642 65 1065 1642 67 1079 minecraft:bookshelf
execute in fantasia:campaign run setblock 1632 65 1065 minecraft:lectern
execute in fantasia:campaign run fill 1552 65 1022 1552 68 1026 minecraft:air
execute in fantasia:campaign run fill 1568 65 1022 1568 68 1026 minecraft:air
execute in fantasia:campaign run fill 1534 65 1040 1538 68 1040 minecraft:air
execute in fantasia:campaign run fill 1534 65 1056 1538 68 1056 minecraft:air
execute in fantasia:campaign run fill 1600 65 1022 1600 68 1026 minecraft:air
execute in fantasia:campaign run fill 1616 65 1022 1616 68 1026 minecraft:air
execute in fantasia:campaign run fill 1582 65 1040 1586 68 1040 minecraft:air
execute in fantasia:campaign run fill 1582 65 1056 1586 68 1056 minecraft:air
execute in fantasia:campaign run fill 1630 65 1040 1634 68 1040 minecraft:air
execute in fantasia:campaign run fill 1630 65 1056 1634 68 1056 minecraft:air
execute in fantasia:campaign run fill 1552 65 1070 1552 68 1074 minecraft:air
execute in fantasia:campaign run fill 1568 65 1070 1568 68 1074 minecraft:air
execute in fantasia:campaign run fill 1600 65 1070 1600 68 1074 minecraft:air
execute in fantasia:campaign run fill 1616 65 1070 1616 68 1074 minecraft:air
execute in fantasia:campaign run summon minecraft:interaction 1536 65 1024 {Tags:["fa_exp_station","fa_exp_canal_rescue_0"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1536 68 1024 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"수문 관리인의 일지\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1584 65 1024 {Tags:["fa_exp_station","fa_exp_canal_rescue_1"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1584 68 1024 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"동결된 경비실\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1632 65 1024 {Tags:["fa_exp_station","fa_exp_canal_rescue_2"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1632 68 1024 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"역류 장치\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1536 65 1072 {Tags:["fa_exp_station","fa_exp_canal_rescue_3"],width:2.0f,height:2.5f,response:1b}
schedule function fantasia:expansion/canal_rescue/batch_4 1t replace
