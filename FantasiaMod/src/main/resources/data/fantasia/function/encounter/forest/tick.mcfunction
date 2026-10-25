scoreboard players add #time_forest fa_world 1
execute as @a[tag=fa_in_forest] at @s unless dimension fantasia:campaign run function fantasia:encounter/forest/leave
execute positioned -160 65 5 as @a[tag=fa_in_forest,distance=40..] run function fantasia:encounter/forest/leave
execute unless entity @a[tag=fa_in_forest] run function fantasia:encounter/forest/abort
execute if score #time_forest fa_world matches 600.. run function fantasia:encounter/forest/abort
execute if score #forest fa_world matches 1 if score #kills_forest fa_world >= #need_forest fa_world run function fantasia:encounter/forest/win
