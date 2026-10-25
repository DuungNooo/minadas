advancement revoke @s only fantasia:kill/castle
execute if dimension fantasia:campaign if entity @s[tag=fa_in_castle] if score #castle fa_world matches 1 run scoreboard players add #kills_castle fa_world 1
