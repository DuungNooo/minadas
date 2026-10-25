scoreboard players set @s fa_ok 1
scoreboard players set @s fa_supplies 180
give @s minecraft:lapis_lazuli 16
give @s minecraft:book 3
give @s minecraft:blaze_powder 8
give @s minecraft:nether_wart 8
give @s minecraft:sugar 8
give @s minecraft:potion[minecraft:potion_contents={potion:"minecraft:water"}] 3
experience add @s 5 levels
tellraw @s {"text":"북서쪽 마법부여실: 청금석과 경험치로 책을 마법부여하세요. 북동쪽 연금실: 물병 → 네더 사마귀 → 설탕 순서로 양조하세요. 동쪽 표적은 활로 중심을 맞히세요.","color":"white"}
