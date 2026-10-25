kill @e[tag=fa_enemy_castle]
scoreboard players set #castle fa_world 1
scoreboard players set #kills_castle fa_world 0
scoreboard players set #time_castle fa_world 0
scoreboard players set #wave_castle fa_world 1
execute as @a[distance=..12,tag=!fa_fighting,scores={fa_stage=5}] run tag @s add fa_in_castle
tag @a[tag=fa_in_castle] add fa_fighting
execute as @a[tag=fa_in_castle] in fantasia:campaign run tp @s 320 65 169
execute as @a[tag=fa_in_castle] run effect give @s minecraft:resistance 5 2 true
execute as @a[tag=fa_in_castle] run tellraw @s {"text":"도전 시작! 아레나에서 적을 모두 쓰러뜨리세요. 사망·이탈 시 보상이 지급되지 않으며, 전원 이탈 시 도전이 초기화됩니다.","color":"yellow"}
function fantasia:encounter/castle/spawn
scoreboard players set #seal_west fa_world 0
scoreboard players set #seal_east fa_world 0
bossbar set fantasia:belkarion players @a[tag=fa_in_castle]
bossbar set fantasia:belkarion value 3
bossbar set fantasia:belkarion visible true
