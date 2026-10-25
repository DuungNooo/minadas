advancement revoke @s only fantasia:kill/forest
execute if dimension fantasia:campaign if entity @s[tag=fa_in_forest] if score #forest fa_world matches 1 run scoreboard players add #kills_forest fa_world 1
