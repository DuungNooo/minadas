advancement revoke @s only fantasia:npc/claude
tellraw @s {"text":"클라우드 · 동부 전선","color":"gold"}
tellraw @s {"text":"전선의 정예군을 격퇴하고 봉인 장치를 확보해 주세요. 세 전선이 모두 안정되어야 왕좌로 가는 길이 열립니다.","color":"white"}
tellraw @s [{"text":"[ 전선 전투 시작 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 41"}}]
tellraw @s [{"text":"[ 현재 목표 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 2"}},{"text":"[ 아카데미 귀환 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 1"}}]
execute if entity @s[tag=fa_modded] run tellraw @s [{"text":"[ 대화 ] ","color":"yellow","clickEvent":{"action":"run_command","value":"/fantasia_npc claude talk"}},{"text":"[ 선물 ] ","color":"light_purple","clickEvent":{"action":"run_command","value":"/fantasia_npc claude gift"}},{"text":"[ 내 정보 ]","color":"white","clickEvent":{"action":"run_command","value":"/fantasia_stats"}}]
