scoreboard players set @s fa_south 5
advancement grant @s only fantasia_research:campaign/south
tag @s remove fa_in_south
tag @s remove fa_fighting
tellraw @s {"text":"남부 전선 확보! 아카데미에서 다음 목적지를 선택하세요.","color":"green"}
give @s minecraft:golden_apple 2
experience add @s 5 levels
