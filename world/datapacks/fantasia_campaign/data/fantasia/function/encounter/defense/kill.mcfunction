advancement revoke @s only fantasia:kill/defense
execute if dimension fantasia:campaign if entity @s[tag=fa_in_defense] if score #defense fa_world matches 1 run scoreboard players add #kills_defense fa_world 1
