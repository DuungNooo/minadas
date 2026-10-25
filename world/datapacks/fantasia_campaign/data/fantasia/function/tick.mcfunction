execute if score #ready fa_world matches 1 unless score #npcs fa_world matches 1..2 run function fantasia:resume
execute if score #ready fa_world matches 1 as @a[tag=!fa_joined] at @s run function fantasia:join
execute if score #ready fa_world matches 1 as @a[scores={fa_action=1..}] at @s run function fantasia:action
scoreboard players add #clock fa_world 1
execute if score #ready fa_world matches 1 if score #clock fa_world matches 20.. run function fantasia:second
execute if score #clock fa_world matches 20.. run scoreboard players set #clock fa_world 0
