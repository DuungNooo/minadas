advancement revoke @s only fantasia:npc/rachel
tellraw @s {"text":"라헬 · 봉인서고","color":"gold"}
tellraw @s {"text":"서쪽 옛 기록, 동쪽 실험 기록, 중앙 교수의 편지를 읽으세요. 그 후 저에게 보고하면 봉인의 진실을 알려드리겠습니다.","color":"white"}
tellraw @s [{"text":"[ 조사 보고 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 31"}}]
tellraw @s [{"text":"[ 현재 목표 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 2"}},{"text":"[ 아카데미 귀환 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 1"}}]
execute if entity @s[tag=fa_modded] run tellraw @s [{"text":"[ 대화 ] ","color":"yellow","clickEvent":{"action":"run_command","value":"/fantasia_npc rachel talk"}},{"text":"[ 선물 ] ","color":"light_purple","clickEvent":{"action":"run_command","value":"/fantasia_npc rachel gift"}},{"text":"[ 내 정보 ]","color":"white","clickEvent":{"action":"run_command","value":"/fantasia_stats"}}]
