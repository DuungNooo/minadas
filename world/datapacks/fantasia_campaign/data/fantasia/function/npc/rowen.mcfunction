advancement revoke @s only fantasia:npc/rowen
tellraw @s {"text":"로웬 · 침식된 숲","color":"gold"}
tellraw @s {"text":"서쪽 뿌리 → 중앙 정화석 → 동쪽 꽃 순서로 정화한 뒤 숲의 마물을 물리치세요.","color":"white"}
tellraw @s [{"text":"[ 실전 도전 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 22"}}]
tellraw @s [{"text":"[ 현재 목표 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 2"}},{"text":"[ 아카데미 귀환 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 1"}}]
execute if entity @s[tag=fa_modded] run tellraw @s [{"text":"[ 대화 ] ","color":"yellow","clickEvent":{"action":"run_command","value":"/fantasia_npc rowen talk"}},{"text":"[ 선물 ] ","color":"light_purple","clickEvent":{"action":"run_command","value":"/fantasia_npc rowen gift"}},{"text":"[ 내 정보 ]","color":"white","clickEvent":{"action":"run_command","value":"/fantasia_stats"}}]
