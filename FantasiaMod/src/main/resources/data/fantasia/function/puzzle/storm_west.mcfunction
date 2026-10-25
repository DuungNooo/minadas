execute unless score @s fa_stage matches 1 run return 0
execute unless score @s fa_storm matches 0 run return 0
scoreboard players set @s fa_storm 1
scoreboard players set @s fa_timer 20
tellraw @s {"text":"20초 안에 동쪽 장치 → 중앙 집전기 순서로 가동하세요.","color":"yellow"}
