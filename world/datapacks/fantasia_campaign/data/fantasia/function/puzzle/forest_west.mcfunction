execute unless score @s fa_stage matches 1 run return 0
execute unless score @s fa_forest matches 0 run return 0
scoreboard players set @s fa_forest 1
tellraw @s {"text":"장치 1/3 가동. 다음 장치로 이동하세요.","color":"green"}
