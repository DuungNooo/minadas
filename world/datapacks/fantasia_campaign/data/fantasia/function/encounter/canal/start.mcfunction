kill @e[tag=fa_enemy_canal]
scoreboard players set #canal fa_world 1
scoreboard players set #kills_canal fa_world 0
scoreboard players set #time_canal fa_world 0
scoreboard players set #wave_canal fa_world 1
execute as @a[distance=..12,tag=!fa_fighting,scores={fa_stage=1,fa_canal=3}] run tag @s add fa_in_canal
tag @a[tag=fa_in_canal] add fa_fighting
execute as @a[tag=fa_in_canal] in fantasia:campaign run tp @s 0 65 159
execute as @a[tag=fa_in_canal] run effect give @s minecraft:resistance 5 2 true
execute as @a[tag=fa_in_canal] run tellraw @s {"text":"도전 시작! 아레나에서 적을 모두 쓰러뜨리세요. 사망·이탈 시 보상이 지급되지 않으며, 전원 이탈 시 도전이 초기화됩니다.","color":"yellow"}
function fantasia:encounter/canal/spawn
