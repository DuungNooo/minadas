scoreboard players add #time_north fa_world 1
execute as @a[tag=fa_in_north] at @s unless dimension fantasia:campaign run function fantasia:encounter/north/leave
execute positioned -160 65 -155 as @a[tag=fa_in_north,distance=40..] run function fantasia:encounter/north/leave
execute unless entity @a[tag=fa_in_north] run function fantasia:encounter/north/abort
execute if score #time_north fa_world matches 600.. run function fantasia:encounter/north/abort
execute if score #north fa_world matches 1 if score #kills_north fa_world >= #need_north fa_world run function fantasia:encounter/north/win
