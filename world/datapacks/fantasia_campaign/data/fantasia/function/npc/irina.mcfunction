advancement revoke @s only fantasia:npc/irina
tellraw @s {"text":"이리나 · 불타는 광산","color":"gold"}
tellraw @s {"text":"광산의 마물들을 쓰러뜨린 다음 서쪽 광부를 구하고 동쪽 화염핵을 회수하세요.","color":"white"}
tellraw @s [{"text":"[ 실전 도전 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 20"}}]
tellraw @s [{"text":"[ 현재 목표 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 2"}},{"text":"[ 아카데미 귀환 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 1"}}]
execute if entity @s[tag=fa_modded] run tellraw @s [{"text":"[ 대화 ] ","color":"yellow","clickEvent":{"action":"run_command","value":"/fantasia_npc irina talk"}},{"text":"[ 선물 ] ","color":"light_purple","clickEvent":{"action":"run_command","value":"/fantasia_npc irina gift"}},{"text":"[ 내 정보 ]","color":"white","clickEvent":{"action":"run_command","value":"/fantasia_stats"}}]
