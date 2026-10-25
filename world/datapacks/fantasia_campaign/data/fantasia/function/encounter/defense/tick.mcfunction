scoreboard players add #time_defense fa_world 1
execute as @a[tag=fa_in_defense] at @s unless dimension fantasia:campaign run function fantasia:encounter/defense/leave
execute positioned -160 65 165 as @a[tag=fa_in_defense,distance=40..] run function fantasia:encounter/defense/leave
execute unless entity @a[tag=fa_in_defense] run function fantasia:encounter/defense/abort
execute if score #time_defense fa_world matches 600.. run function fantasia:encounter/defense/abort
execute if score #defense fa_world matches 1 if score #kills_defense fa_world >= #need_defense fa_world run function fantasia:encounter/defense/win
