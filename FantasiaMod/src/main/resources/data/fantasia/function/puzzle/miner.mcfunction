execute unless score @s fa_stage matches 1 run return 0
execute unless score @s fa_mine matches 1 run return 0
scoreboard players set @s fa_mine 2
tellraw @s {"text":"광부를 구출했다. “교수님은 동쪽 화염핵에서 검은 표식을 보셨어요. 그 뒤로 사라지셨죠.”","color":"white"}
