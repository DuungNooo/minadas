advancement revoke @s only fantasia:kill/south
execute if dimension fantasia:campaign if entity @s[tag=fa_in_south] if score #south fa_world matches 1 run scoreboard players add #kills_south fa_world 1
