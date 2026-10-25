execute in fantasia:campaign run fill 1872 64 1312 1904 64 1344 minecraft:stone_bricks
execute in fantasia:campaign run fill 1872 65 1312 1904 69 1312 minecraft:stone_bricks
execute in fantasia:campaign run fill 1872 65 1344 1904 69 1344 minecraft:stone_bricks
execute in fantasia:campaign run fill 1872 65 1312 1872 69 1344 minecraft:stone_bricks
execute in fantasia:campaign run fill 1904 65 1312 1904 69 1344 minecraft:stone_bricks
execute in fantasia:campaign run fill 1876 65 1316 1876 70 1316 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1876 71 1316 minecraft:sea_lantern
execute in fantasia:campaign run fill 1876 65 1340 1876 70 1340 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1876 71 1340 minecraft:sea_lantern
execute in fantasia:campaign run fill 1900 65 1316 1900 70 1316 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1900 71 1316 minecraft:sea_lantern
execute in fantasia:campaign run fill 1900 65 1340 1900 70 1340 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1900 71 1340 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1881 64 1328 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1888 64 1328 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1895 64 1328 minecraft:sea_lantern
execute in fantasia:campaign run fill 1878 65 1321 1878 67 1335 minecraft:bookshelf
execute in fantasia:campaign run fill 1898 65 1321 1898 67 1335 minecraft:bookshelf
execute in fantasia:campaign run setblock 1888 65 1321 minecraft:lectern
execute in fantasia:campaign run fill 1808 65 1278 1808 68 1282 minecraft:air
execute in fantasia:campaign run fill 1824 65 1278 1824 68 1282 minecraft:air
execute in fantasia:campaign run fill 1790 65 1296 1794 68 1296 minecraft:air
execute in fantasia:campaign run fill 1790 65 1312 1794 68 1312 minecraft:air
execute in fantasia:campaign run fill 1856 65 1278 1856 68 1282 minecraft:air
execute in fantasia:campaign run fill 1872 65 1278 1872 68 1282 minecraft:air
execute in fantasia:campaign run fill 1838 65 1296 1842 68 1296 minecraft:air
execute in fantasia:campaign run fill 1838 65 1312 1842 68 1312 minecraft:air
execute in fantasia:campaign run fill 1886 65 1296 1890 68 1296 minecraft:air
execute in fantasia:campaign run fill 1886 65 1312 1890 68 1312 minecraft:air
execute in fantasia:campaign run fill 1808 65 1326 1808 68 1330 minecraft:air
execute in fantasia:campaign run fill 1824 65 1326 1824 68 1330 minecraft:air
execute in fantasia:campaign run fill 1856 65 1326 1856 68 1330 minecraft:air
execute in fantasia:campaign run fill 1872 65 1326 1872 68 1330 minecraft:air
execute in fantasia:campaign run summon minecraft:interaction 1792 65 1280 {Tags:["fa_exp_station","fa_exp_capital_refuge_0"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1792 68 1280 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"버려진 광장\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1840 65 1280 {Tags:["fa_exp_station","fa_exp_capital_refuge_1"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1840 68 1280 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"치료소 앞의 전투\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1888 65 1280 {Tags:["fa_exp_station","fa_exp_capital_refuge_2"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1888 68 1280 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"성문 복구\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1792 65 1328 {Tags:["fa_exp_station","fa_exp_capital_refuge_3"],width:2.0f,height:2.5f,response:1b}
schedule function fantasia:expansion/capital_refuge/batch_4 1t replace
