advancement revoke @s only fantasia:npc/theo
tellraw @s {"text":"테오 · 낙뢰 평원","color":"gold"}
tellraw @s {"text":"서쪽 장치를 켠 뒤 20초 안에 동쪽 장치와 중앙 집전기에 도착해 누르세요. 그다음 폭풍 경비대를 쓰러뜨리세요.","color":"white"}
tellraw @s [{"text":"[ 실전 도전 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 23"}}]
tellraw @s [{"text":"[ 현재 목표 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 2"}},{"text":"[ 아카데미 귀환 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 1"}}]
execute if entity @s[tag=fa_modded] run tellraw @s [{"text":"[ 대화 ] ","color":"yellow","clickEvent":{"action":"run_command","value":"/fantasia_npc theo talk"}},{"text":"[ 선물 ] ","color":"light_purple","clickEvent":{"action":"run_command","value":"/fantasia_npc theo gift"}},{"text":"[ 내 정보 ]","color":"white","clickEvent":{"action":"run_command","value":"/fantasia_stats"}}]
