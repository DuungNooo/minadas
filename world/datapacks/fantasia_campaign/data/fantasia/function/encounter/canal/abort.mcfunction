execute as @a[tag=fa_in_canal] run tellraw @s {"text":"도전이 초기화되었습니다. NPC에게 다시 요청할 수 있습니다.","color":"yellow"}
tag @a[tag=fa_in_canal] remove fa_fighting
tag @a remove fa_in_canal
kill @e[tag=fa_enemy_canal]
scoreboard players set #canal fa_world 0
