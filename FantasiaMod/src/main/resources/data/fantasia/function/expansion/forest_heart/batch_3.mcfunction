execute in fantasia:campaign run fill 1872 64 1056 1904 64 1088 minecraft:mossy_stone_bricks
execute in fantasia:campaign run fill 1872 65 1056 1904 69 1056 minecraft:mossy_stone_bricks
execute in fantasia:campaign run fill 1872 65 1088 1904 69 1088 minecraft:mossy_stone_bricks
execute in fantasia:campaign run fill 1872 65 1056 1872 69 1088 minecraft:mossy_stone_bricks
execute in fantasia:campaign run fill 1904 65 1056 1904 69 1088 minecraft:mossy_stone_bricks
execute in fantasia:campaign run fill 1876 65 1060 1876 70 1060 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1876 71 1060 minecraft:sea_lantern
execute in fantasia:campaign run fill 1876 65 1084 1876 70 1084 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1876 71 1084 minecraft:sea_lantern
execute in fantasia:campaign run fill 1900 65 1060 1900 70 1060 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1900 71 1060 minecraft:sea_lantern
execute in fantasia:campaign run fill 1900 65 1084 1900 70 1084 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1900 71 1084 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1881 64 1072 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1888 64 1072 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1895 64 1072 minecraft:sea_lantern
execute in fantasia:campaign run fill 1878 65 1065 1878 67 1079 minecraft:bookshelf
execute in fantasia:campaign run fill 1898 65 1065 1898 67 1079 minecraft:bookshelf
execute in fantasia:campaign run setblock 1888 65 1065 minecraft:lectern
execute in fantasia:campaign run fill 1808 65 1022 1808 68 1026 minecraft:air
execute in fantasia:campaign run fill 1824 65 1022 1824 68 1026 minecraft:air
execute in fantasia:campaign run fill 1790 65 1040 1794 68 1040 minecraft:air
execute in fantasia:campaign run fill 1790 65 1056 1794 68 1056 minecraft:air
execute in fantasia:campaign run fill 1856 65 1022 1856 68 1026 minecraft:air
execute in fantasia:campaign run fill 1872 65 1022 1872 68 1026 minecraft:air
execute in fantasia:campaign run fill 1838 65 1040 1842 68 1040 minecraft:air
execute in fantasia:campaign run fill 1838 65 1056 1842 68 1056 minecraft:air
execute in fantasia:campaign run fill 1886 65 1040 1890 68 1040 minecraft:air
execute in fantasia:campaign run fill 1886 65 1056 1890 68 1056 minecraft:air
execute in fantasia:campaign run fill 1808 65 1070 1808 68 1074 minecraft:air
execute in fantasia:campaign run fill 1824 65 1070 1824 68 1074 minecraft:air
execute in fantasia:campaign run fill 1856 65 1070 1856 68 1074 minecraft:air
execute in fantasia:campaign run fill 1872 65 1070 1872 68 1074 minecraft:air
execute in fantasia:campaign run summon minecraft:interaction 1792 65 1024 {Tags:["fa_exp_station","fa_exp_forest_heart_0"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1792 68 1024 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"독성 잎의 표본\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1840 65 1024 {Tags:["fa_exp_station","fa_exp_forest_heart_1"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1840 68 1024 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"흉터 난 정원\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1888 65 1024 {Tags:["fa_exp_station","fa_exp_forest_heart_2"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1888 68 1024 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"순환의 세 돌\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1792 65 1072 {Tags:["fa_exp_station","fa_exp_forest_heart_3"],width:2.0f,height:2.5f,response:1b}
schedule function fantasia:expansion/forest_heart/batch_4 1t replace
