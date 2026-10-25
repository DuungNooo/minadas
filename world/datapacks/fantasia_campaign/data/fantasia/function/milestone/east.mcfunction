scoreboard players set @s fa_east 5
advancement grant @s only fantasia_research:campaign/east
tag @s remove fa_in_east
tag @s remove fa_fighting
tellraw @s {"text":"동부 전선 확보! 아카데미에서 다음 목적지를 선택하세요.","color":"green"}
advancement grant @s only fantasia_research:holy_tier_1
advancement grant @s only fantasia_research:holy_tier_2
give @s minecraft:golden_apple 2
experience add @s 5 levels
