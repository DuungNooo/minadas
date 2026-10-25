advancement revoke @s only fantasia:npc/noah
tellraw @s {"text":"노아 · 연구","color":"gold"}
tellraw @s {"text":"네 지역 조사, 봉인의 진실, 세 전선을 통해 연구가 단계적으로 열립니다. 지역 봉인은 누구나 자신의 조사 기록을 완성해야 합니다.","color":"white"}
function fantasia:status
execute if entity @s[tag=fa_modded] run tellraw @s {"text":"[ 마법 연구·주문서 받기 ]","color":"aqua","clickEvent":{"action":"run_command","value":"/fantasia_magic"}}
tellraw @s [{"text":"[ 현재 목표 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 2"}},{"text":"[ 아카데미 귀환 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 1"}}]
execute if entity @s[tag=fa_modded] run tellraw @s [{"text":"[ 대화 ] ","color":"yellow","clickEvent":{"action":"run_command","value":"/fantasia_npc noah talk"}},{"text":"[ 선물 ] ","color":"light_purple","clickEvent":{"action":"run_command","value":"/fantasia_npc noah gift"}},{"text":"[ 내 정보 ]","color":"white","clickEvent":{"action":"run_command","value":"/fantasia_stats"}}]
