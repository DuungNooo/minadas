scoreboard players add #time_storm fa_world 1
execute as @a[tag=fa_in_storm] at @s unless dimension fantasia:campaign run function fantasia:encounter/storm/leave
execute positioned 0 65 -155 as @a[tag=fa_in_storm,distance=40..] run function fantasia:encounter/storm/leave
execute unless entity @a[tag=fa_in_storm] run function fantasia:encounter/storm/abort
execute if score #time_storm fa_world matches 600.. run function fantasia:encounter/storm/abort
execute if score #storm fa_world matches 1 if score #kills_storm fa_world >= #need_storm fa_world run function fantasia:encounter/storm/win
