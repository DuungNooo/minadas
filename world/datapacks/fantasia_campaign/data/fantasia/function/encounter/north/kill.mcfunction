advancement revoke @s only fantasia:kill/north
execute if dimension fantasia:campaign if entity @s[tag=fa_in_north] if score #north fa_world matches 1 run scoreboard players add #kills_north fa_world 1
