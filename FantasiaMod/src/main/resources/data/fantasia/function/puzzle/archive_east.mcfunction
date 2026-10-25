execute unless score @s fa_stage matches 3 run return 0
execute unless score @s fa_archive matches 1 run return 0
scoreboard players set @s fa_archive 2
tellraw @s {"text":"세대에 걸친 마력 추출로 봉인핵이 손상되었다. 교단은 균열을 넓히고 있다.","color":"white"}
