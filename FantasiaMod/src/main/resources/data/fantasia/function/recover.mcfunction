tag @s remove fa_fighting
tag @s remove fa_in_tutorial
tag @s remove fa_in_mine
tag @s remove fa_in_canal
tag @s remove fa_in_forest
tag @s remove fa_in_storm
tag @s remove fa_in_defense
tag @s remove fa_in_north
tag @s remove fa_in_east
tag @s remove fa_in_south
tag @s remove fa_in_castle
scoreboard players operation @s fa_prevdeath = @s fa_deaths
execute in fantasia:campaign run tp @s 0 65 -8
effect give @s minecraft:regeneration 6 2 true
effect give @s minecraft:resistance 10 4 true
tellraw @s {"text":"아카데미로 구조되었습니다. 이미 완료한 조사 기록은 유지됩니다. 다시 NPC에게 도전을 요청할 수 있습니다.","color":"yellow"}
