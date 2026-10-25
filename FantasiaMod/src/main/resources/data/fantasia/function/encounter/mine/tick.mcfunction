scoreboard players add #time_mine fa_world 1
execute as @a[tag=fa_in_mine] at @s unless dimension fantasia:campaign run function fantasia:encounter/mine/leave
execute positioned 160 65 5 as @a[tag=fa_in_mine,distance=40..] run function fantasia:encounter/mine/leave
execute unless entity @a[tag=fa_in_mine] run function fantasia:encounter/mine/abort
execute if score #time_mine fa_world matches 600.. run function fantasia:encounter/mine/abort
execute if score #mine fa_world matches 1 if score #kills_mine fa_world >= #need_mine fa_world run function fantasia:encounter/mine/win
