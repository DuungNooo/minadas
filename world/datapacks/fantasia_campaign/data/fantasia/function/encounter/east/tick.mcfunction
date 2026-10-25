scoreboard players add #time_east fa_world 1
execute as @a[tag=fa_in_east] at @s unless dimension fantasia:campaign run function fantasia:encounter/east/leave
execute positioned 160 65 -155 as @a[tag=fa_in_east,distance=40..] run function fantasia:encounter/east/leave
execute unless entity @a[tag=fa_in_east] run function fantasia:encounter/east/abort
execute if score #time_east fa_world matches 600.. run function fantasia:encounter/east/abort
execute if score #east fa_world matches 1 if score #kills_east fa_world >= #need_east fa_world run function fantasia:encounter/east/win
