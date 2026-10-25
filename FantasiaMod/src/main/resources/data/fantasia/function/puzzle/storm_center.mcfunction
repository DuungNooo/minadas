execute unless score @s fa_stage matches 1 run return 0
execute unless score @s fa_storm matches 2 run return 0
scoreboard players set @s fa_storm 3
tellraw @s {"text":"장치 3/3 가동. 안내 NPC에게 실전 도전을 요청하세요.","color":"green"}
