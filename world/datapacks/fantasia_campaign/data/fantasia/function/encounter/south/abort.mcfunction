execute as @a[tag=fa_in_south] run tellraw @s {"text":"도전이 초기화되었습니다. NPC에게 다시 요청할 수 있습니다.","color":"yellow"}
tag @a[tag=fa_in_south] remove fa_fighting
tag @a remove fa_in_south
kill @e[tag=fa_enemy_south]
scoreboard players set #south fa_world 0
