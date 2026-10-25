scoreboard players set @s fa_north 5
advancement grant @s only fantasia_research:campaign/north
tag @s remove fa_in_north
tag @s remove fa_fighting
tellraw @s {"text":"북부 전선 확보! 아카데미에서 다음 목적지를 선택하세요.","color":"green"}
advancement grant @s only fantasia_research:void_tier_1
advancement grant @s only fantasia_research:void_tier_2
give @s minecraft:golden_apple 2
experience add @s 5 levels
