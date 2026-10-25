scoreboard players add #time_castle fa_world 1
execute as @a[tag=fa_in_castle] at @s unless dimension fantasia:campaign run function fantasia:encounter/castle/leave
execute positioned 320 65 175 as @a[tag=fa_in_castle,distance=40..] run function fantasia:encounter/castle/leave
execute unless entity @a[tag=fa_in_castle] run function fantasia:encounter/castle/abort
execute if score #time_castle fa_world matches 600.. run function fantasia:encounter/castle/abort
execute if score #castle fa_world matches 1 if score #kills_castle fa_world >= #need_castle fa_world run function fantasia:encounter/castle/win
