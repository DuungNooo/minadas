advancement revoke @s only fantasia:kill/mine
execute if dimension fantasia:campaign if entity @s[tag=fa_in_mine] if score #mine fa_world matches 1 run scoreboard players add #kills_mine fa_world 1
