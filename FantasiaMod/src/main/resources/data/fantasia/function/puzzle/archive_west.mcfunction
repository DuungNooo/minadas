execute unless score @s fa_stage matches 3 run return 0
execute unless score @s fa_archive matches 0 run return 0
scoreboard players set @s fa_archive 1
tellraw @s {"text":"연맹은 마왕을 봉인했지만 그의 마력을 아카데미로 흘려보냈다.","color":"white"}
