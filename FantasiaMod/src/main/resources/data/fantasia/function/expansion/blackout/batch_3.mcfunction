execute in fantasia:campaign run fill 1104 64 1056 1136 64 1088 minecraft:stone_bricks
execute in fantasia:campaign run fill 1104 65 1056 1136 69 1056 minecraft:stone_bricks
execute in fantasia:campaign run fill 1104 65 1088 1136 69 1088 minecraft:stone_bricks
execute in fantasia:campaign run fill 1104 65 1056 1104 69 1088 minecraft:stone_bricks
execute in fantasia:campaign run fill 1136 65 1056 1136 69 1088 minecraft:stone_bricks
execute in fantasia:campaign run fill 1108 65 1060 1108 70 1060 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1108 71 1060 minecraft:sea_lantern
execute in fantasia:campaign run fill 1108 65 1084 1108 70 1084 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1108 71 1084 minecraft:sea_lantern
execute in fantasia:campaign run fill 1132 65 1060 1132 70 1060 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1132 71 1060 minecraft:sea_lantern
execute in fantasia:campaign run fill 1132 65 1084 1132 70 1084 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1132 71 1084 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1113 64 1072 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1120 64 1072 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1127 64 1072 minecraft:sea_lantern
execute in fantasia:campaign run fill 1110 65 1065 1110 67 1079 minecraft:bookshelf
execute in fantasia:campaign run fill 1130 65 1065 1130 67 1079 minecraft:bookshelf
execute in fantasia:campaign run setblock 1120 65 1065 minecraft:lectern
execute in fantasia:campaign run fill 1040 65 1022 1040 68 1026 minecraft:air
execute in fantasia:campaign run fill 1056 65 1022 1056 68 1026 minecraft:air
execute in fantasia:campaign run fill 1022 65 1040 1026 68 1040 minecraft:air
execute in fantasia:campaign run fill 1022 65 1056 1026 68 1056 minecraft:air
execute in fantasia:campaign run fill 1088 65 1022 1088 68 1026 minecraft:air
execute in fantasia:campaign run fill 1104 65 1022 1104 68 1026 minecraft:air
execute in fantasia:campaign run fill 1070 65 1040 1074 68 1040 minecraft:air
execute in fantasia:campaign run fill 1070 65 1056 1074 68 1056 minecraft:air
execute in fantasia:campaign run fill 1118 65 1040 1122 68 1040 minecraft:air
execute in fantasia:campaign run fill 1118 65 1056 1122 68 1056 minecraft:air
execute in fantasia:campaign run fill 1040 65 1070 1040 68 1074 minecraft:air
execute in fantasia:campaign run fill 1056 65 1070 1056 68 1074 minecraft:air
execute in fantasia:campaign run fill 1088 65 1070 1088 68 1074 minecraft:air
execute in fantasia:campaign run fill 1104 65 1070 1104 68 1074 minecraft:air
execute in fantasia:campaign run summon minecraft:interaction 1024 65 1024 {Tags:["fa_exp_station","fa_exp_blackout_0"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1024 68 1024 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"꺼진 동쪽 회랑\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1072 65 1024 {Tags:["fa_exp_station","fa_exp_blackout_1"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1072 68 1024 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"남겨진 훈련장\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1120 65 1024 {Tags:["fa_exp_station","fa_exp_blackout_2"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1120 68 1024 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"지하의 세 공명기\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1024 65 1072 {Tags:["fa_exp_station","fa_exp_blackout_3"],width:2.0f,height:2.5f,response:1b}
schedule function fantasia:expansion/blackout/batch_4 1t replace
