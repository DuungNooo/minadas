scoreboard players add #time_south fa_world 1
execute as @a[tag=fa_in_south] at @s unless dimension fantasia:campaign run function fantasia:encounter/south/leave
execute positioned 320 65 5 as @a[tag=fa_in_south,distance=40..] run function fantasia:encounter/south/leave
execute unless entity @a[tag=fa_in_south] run function fantasia:encounter/south/abort
execute if score #time_south fa_world matches 600.. run function fantasia:encounter/south/abort
execute if score #south fa_world matches 1 if score #kills_south fa_world >= #need_south fa_world run function fantasia:encounter/south/win
