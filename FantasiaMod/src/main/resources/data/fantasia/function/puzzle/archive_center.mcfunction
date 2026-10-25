execute unless score @s fa_stage matches 3 run return 0
execute unless score @s fa_archive matches 2 run return 0
scoreboard players set @s fa_archive 3
tellraw @s {"text":"“마력을 추출하지 않아도 봉인은 재구축할 수 있다. 세 전선의 공명석을 모아 달라.” — 베른하르트","color":"white"}
