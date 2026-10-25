advancement revoke @s only fantasia:npc/seraphine
tellraw @s {"text":"세라핀 · 치료","color":"gold"}
tellraw @s {"text":"쓰러져도 조사 기록은 사라지지 않아요. 여기서 치료와 식량을 받아 가세요.","color":"white"}
tellraw @s [{"text":"[ 치료와 식량 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 13"}}]
tellraw @s [{"text":"[ 현재 목표 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 2"}},{"text":"[ 아카데미 귀환 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 1"}}]
execute if entity @s[tag=fa_modded] run tellraw @s [{"text":"[ 대화 ] ","color":"yellow","clickEvent":{"action":"run_command","value":"/fantasia_npc seraphine talk"}},{"text":"[ 선물 ] ","color":"light_purple","clickEvent":{"action":"run_command","value":"/fantasia_npc seraphine gift"}},{"text":"[ 내 정보 ]","color":"white","clickEvent":{"action":"run_command","value":"/fantasia_stats"}}]
