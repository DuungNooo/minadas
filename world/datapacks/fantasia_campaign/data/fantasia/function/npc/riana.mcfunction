advancement revoke @s only fantasia:npc/riana
tellraw @s {"text":"리아나 · 얼어붙은 수로","color":"gold"}
tellraw @s {"text":"수로 흐름은 동쪽 → 서쪽 → 중앙 순서입니다. 세 수문을 조절한 뒤 경비대를 쓰러뜨리세요.","color":"white"}
tellraw @s [{"text":"[ 실전 도전 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 21"}}]
tellraw @s [{"text":"[ 현재 목표 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 2"}},{"text":"[ 아카데미 귀환 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 1"}}]
execute if entity @s[tag=fa_modded] run tellraw @s [{"text":"[ 대화 ] ","color":"yellow","clickEvent":{"action":"run_command","value":"/fantasia_npc riana talk"}},{"text":"[ 선물 ] ","color":"light_purple","clickEvent":{"action":"run_command","value":"/fantasia_npc riana gift"}},{"text":"[ 내 정보 ]","color":"white","clickEvent":{"action":"run_command","value":"/fantasia_stats"}}]
