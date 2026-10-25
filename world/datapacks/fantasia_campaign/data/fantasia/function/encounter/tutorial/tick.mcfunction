scoreboard players add #time_tutorial fa_world 1
execute as @a[tag=fa_in_tutorial] at @s unless dimension fantasia:campaign run function fantasia:encounter/tutorial/leave
execute positioned 0 65 22 as @a[tag=fa_in_tutorial,distance=40..] run function fantasia:encounter/tutorial/leave
execute unless entity @a[tag=fa_in_tutorial] run function fantasia:encounter/tutorial/abort
execute if score #time_tutorial fa_world matches 600.. run function fantasia:encounter/tutorial/abort
execute if score #tutorial fa_world matches 1 if score #kills_tutorial fa_world >= #need_tutorial fa_world run function fantasia:encounter/tutorial/win
