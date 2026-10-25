advancement revoke @s only fantasia:kill/tutorial
execute if dimension fantasia:campaign if entity @s[tag=fa_in_tutorial] if score #tutorial fa_world matches 1 run scoreboard players add #kills_tutorial fa_world 1
