scoreboard players set @s fa_ok 1
scoreboard players set @s fa_stage 7
scoreboard players set @s fa_ending 2
advancement grant @s only fantasia_research:campaign/ending
title @s times 20 100 30
title @s title {"text":"마력 소멸","color":"gold"}
title @s subtitle {"text":"Fantasia: 균열의 왕 · 캠페인 완료","color":"white"}
tellraw @s {"text":"당신은 균열 너머의 힘을 완전히 끊었다. 아카데미의 화려한 마력등은 꺼졌지만, 사람들은 처음으로 두려움 없는 밤을 맞았다.","color":"white"}
tellraw @s {"text":"캠페인 완료. NPC 인연과 마법 연구를 계속하거나 아카데미를 자유롭게 탐험하세요.","color":"green"}
