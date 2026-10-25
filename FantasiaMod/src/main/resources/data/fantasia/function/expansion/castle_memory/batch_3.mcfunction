execute in fantasia:campaign run fill 1872 64 1568 1904 64 1600 minecraft:polished_blackstone_bricks
execute in fantasia:campaign run fill 1872 65 1568 1904 69 1568 minecraft:polished_blackstone_bricks
execute in fantasia:campaign run fill 1872 65 1600 1904 69 1600 minecraft:polished_blackstone_bricks
execute in fantasia:campaign run fill 1872 65 1568 1872 69 1600 minecraft:polished_blackstone_bricks
execute in fantasia:campaign run fill 1904 65 1568 1904 69 1600 minecraft:polished_blackstone_bricks
execute in fantasia:campaign run fill 1876 65 1572 1876 70 1572 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1876 71 1572 minecraft:sea_lantern
execute in fantasia:campaign run fill 1876 65 1596 1876 70 1596 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1876 71 1596 minecraft:sea_lantern
execute in fantasia:campaign run fill 1900 65 1572 1900 70 1572 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1900 71 1572 minecraft:sea_lantern
execute in fantasia:campaign run fill 1900 65 1596 1900 70 1596 minecraft:chiseled_stone_bricks
execute in fantasia:campaign run setblock 1900 71 1596 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1881 64 1584 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1888 64 1584 minecraft:sea_lantern
execute in fantasia:campaign run setblock 1895 64 1584 minecraft:sea_lantern
execute in fantasia:campaign run fill 1878 65 1577 1878 67 1591 minecraft:bookshelf
execute in fantasia:campaign run fill 1898 65 1577 1898 67 1591 minecraft:bookshelf
execute in fantasia:campaign run setblock 1888 65 1577 minecraft:lectern
execute in fantasia:campaign run fill 1808 65 1534 1808 68 1538 minecraft:air
execute in fantasia:campaign run fill 1824 65 1534 1824 68 1538 minecraft:air
execute in fantasia:campaign run fill 1790 65 1552 1794 68 1552 minecraft:air
execute in fantasia:campaign run fill 1790 65 1568 1794 68 1568 minecraft:air
execute in fantasia:campaign run fill 1856 65 1534 1856 68 1538 minecraft:air
execute in fantasia:campaign run fill 1872 65 1534 1872 68 1538 minecraft:air
execute in fantasia:campaign run fill 1838 65 1552 1842 68 1552 minecraft:air
execute in fantasia:campaign run fill 1838 65 1568 1842 68 1568 minecraft:air
execute in fantasia:campaign run fill 1886 65 1552 1890 68 1552 minecraft:air
execute in fantasia:campaign run fill 1886 65 1568 1890 68 1568 minecraft:air
execute in fantasia:campaign run fill 1808 65 1582 1808 68 1586 minecraft:air
execute in fantasia:campaign run fill 1824 65 1582 1824 68 1586 minecraft:air
execute in fantasia:campaign run fill 1856 65 1582 1856 68 1586 minecraft:air
execute in fantasia:campaign run fill 1872 65 1582 1872 68 1586 minecraft:air
execute in fantasia:campaign run summon minecraft:interaction 1792 65 1536 {Tags:["fa_exp_station","fa_exp_castle_memory_0"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1792 68 1536 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"칠흑 회랑\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1840 65 1536 {Tags:["fa_exp_station","fa_exp_castle_memory_1"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1840 68 1536 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"뒤틀린 연구실\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1888 65 1536 {Tags:["fa_exp_station","fa_exp_castle_memory_2"],width:2.0f,height:2.5f,response:1b}
execute in fantasia:campaign run summon minecraft:text_display 1888 68 1536 {Tags:["fa_exp_label"],billboard:"center",alignment:"center",text:"{\"text\": \"과거의 세 문\", \"color\": \"aqua\"}"}
execute in fantasia:campaign run summon minecraft:interaction 1792 65 1584 {Tags:["fa_exp_station","fa_exp_castle_memory_3"],width:2.0f,height:2.5f,response:1b}
schedule function fantasia:expansion/castle_memory/batch_4 1t replace
