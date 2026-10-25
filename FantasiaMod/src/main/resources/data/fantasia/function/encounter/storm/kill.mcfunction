advancement revoke @s only fantasia:kill/storm
execute if dimension fantasia:campaign if entity @s[tag=fa_in_storm] if score #storm fa_world matches 1 run scoreboard players add #kills_storm fa_world 1
