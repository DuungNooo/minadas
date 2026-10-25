advancement revoke @s only fantasia:npc/edric
tellraw @s {"text":"에드릭 · 수도 방어","color":"gold"}
tellraw @s {"text":"방어선 안에서 세 차례의 습격을 막아 주세요. 전원이 이탈하거나 쓰러지면 다시 시작할 수 있습니다.","color":"white"}
tellraw @s [{"text":"[ 방어전 시작 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 30"}}]
tellraw @s [{"text":"[ 현재 목표 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 2"}},{"text":"[ 아카데미 귀환 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 1"}}]
execute if entity @s[tag=fa_modded] run tellraw @s [{"text":"[ 대화 ] ","color":"yellow","clickEvent":{"action":"run_command","value":"/fantasia_npc edric talk"}},{"text":"[ 선물 ] ","color":"light_purple","clickEvent":{"action":"run_command","value":"/fantasia_npc edric gift"}},{"text":"[ 내 정보 ]","color":"white","clickEvent":{"action":"run_command","value":"/fantasia_stats"}}]
