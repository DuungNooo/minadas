tellraw @s {"text":"══ Fantasia · 현재 목표 ══","color":"gold"}
execute if score @s fa_stage matches 0 run tellraw @s {"text":"입학 검사 완료 → 카일에게 장비 수령 → 기초 훈련 통과","color":"white"}
execute if score @s fa_stage matches 1 run tellraw @s {"text":"네 지역을 조사하세요. 광산/수로/숲/평원은 원하는 순서로 진행합니다.","color":"white"}
execute if score @s fa_stage matches 2 run tellraw @s {"text":"수도 방어전에서 세 차례의 습격을 막으세요.","color":"white"}
execute if score @s fa_stage matches 3 run tellraw @s {"text":"봉인서고의 세 기록을 읽고 라헬에게 보고하세요.","color":"white"}
execute if score @s fa_stage matches 4 run tellraw @s {"text":"북부·동부·남부 전선의 공명석을 확보하세요.","color":"white"}
execute if score @s fa_stage matches 5 run tellraw @s {"text":"마왕성에서 벨카리온의 세 전투 단계를 돌파하세요.","color":"white"}
execute if score @s fa_stage matches 6 run tellraw @s {"text":"헤론에게 돌아가 결말을 선택하세요.","color":"white"}
execute if score @s fa_stage matches 7 run tellraw @s {"text":"캠페인 완료. 자유 연구와 인연 활동을 계속할 수 있습니다.","color":"white"}
execute if score @s fa_mine matches 5 run tellraw @s {"text":"광산 ✓","color":"green"}
execute if score @s fa_canal matches 5 run tellraw @s {"text":"수로 ✓","color":"green"}
execute if score @s fa_forest matches 5 run tellraw @s {"text":"숲 ✓","color":"green"}
execute if score @s fa_storm matches 5 run tellraw @s {"text":"평원 ✓","color":"green"}
execute if score @s fa_north matches 5 run tellraw @s {"text":"북부 ✓","color":"green"}
execute if score @s fa_east matches 5 run tellraw @s {"text":"동부 ✓","color":"green"}
execute if score @s fa_south matches 5 run tellraw @s {"text":"남부 ✓","color":"green"}
