scoreboard players set @s fa_ok 1
scoreboard players set @s fa_stage 7
scoreboard players set @s fa_ending 4
advancement grant @s only fantasia_research:campaign/ending
title @s times 20 100 30
title @s title {"text":"진실 공개","color":"gold"}
title @s subtitle {"text":"Fantasia: 균열의 왕 · 캠페인 완료","color":"white"}
tellraw @s {"text":"교수의 편지와 실험 기록을 세상에 공개했다. 옛 영웅들의 그림자까지 마주한 아카데미는, 힘을 얻는 법보다 힘을 책임지는 법을 가르치기 시작했다.","color":"white"}
tellraw @s {"text":"캠페인 완료. NPC 인연과 마법 연구를 계속하거나 아카데미를 자유롭게 탐험하세요.","color":"green"}
