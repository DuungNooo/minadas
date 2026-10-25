execute unless entity @s[tag=fa_in_castle] run return 0
execute unless score #castle fa_world matches 1 run return 0
execute unless score #wave_castle fa_world matches 2 run return 0
scoreboard players set #seal_west fa_world 1
tellraw @s {"text":"서쪽 봉인석 안정화.","color":"green"}
execute if score #seal_west fa_world matches 1 if score #seal_east fa_world matches 1 run function fantasia:encounter/castle/final
