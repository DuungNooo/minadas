advancement revoke @s only fantasia:kill/east
execute if dimension fantasia:campaign if entity @s[tag=fa_in_east] if score #east fa_world matches 1 run scoreboard players add #kills_east fa_world 1
