scoreboard players set @s fa_ok 1
scoreboard players set @s fa_stage 7
scoreboard players set @s fa_ending 1
advancement grant @s only fantasia_research:campaign/ending
title @s times 20 100 30
title @s title {"text":"봉인 재구축","color":"gold"}
title @s subtitle {"text":"Fantasia: 균열의 왕 · 캠페인 완료","color":"white"}
tellraw @s {"text":"네 마력핵과 세 공명석이 새로운 봉인이 되었다. 아카데미는 더 이상 마왕의 힘을 빌리지 않고, 학생들은 스스로의 마법을 연구한다.","color":"white"}
tellraw @s {"text":"캠페인 완료. NPC 인연과 마법 연구를 계속하거나 아카데미를 자유롭게 탐험하세요.","color":"green"}
