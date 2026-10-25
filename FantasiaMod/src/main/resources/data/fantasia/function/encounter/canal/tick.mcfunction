scoreboard players add #time_canal fa_world 1
execute as @a[tag=fa_in_canal] at @s unless dimension fantasia:campaign run function fantasia:encounter/canal/leave
execute positioned 0 65 165 as @a[tag=fa_in_canal,distance=40..] run function fantasia:encounter/canal/leave
execute unless entity @a[tag=fa_in_canal] run function fantasia:encounter/canal/abort
execute if score #time_canal fa_world matches 600.. run function fantasia:encounter/canal/abort
execute if score #canal fa_world matches 1 if score #kills_canal fa_world >= #need_canal fa_world run function fantasia:encounter/canal/win
