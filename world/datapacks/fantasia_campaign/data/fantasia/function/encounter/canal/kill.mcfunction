advancement revoke @s only fantasia:kill/canal
execute if dimension fantasia:campaign if entity @s[tag=fa_in_canal] if score #canal fa_world matches 1 run scoreboard players add #kills_canal fa_world 1
