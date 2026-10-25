scoreboard players set @s fa_ok 1
scoreboard players set @s fa_stage 7
scoreboard players set @s fa_ending 3
advancement grant @s only fantasia_research:campaign/ending
title @s times 20 100 30
title @s title {"text":"힘 통제","color":"gold"}
title @s subtitle {"text":"Fantasia: 균열의 왕 · 캠페인 완료","color":"white"}
tellraw @s {"text":"당신은 마왕의 힘을 공동 감시 아래 두었다. 연구에는 엄격한 한계가 생겼고, 사람들은 같은 잘못을 반복하지 않겠다고 맹세했다.","color":"white"}
tellraw @s {"text":"캠페인 완료. NPC 인연과 마법 연구를 계속하거나 아카데미를 자유롭게 탐험하세요.","color":"green"}
