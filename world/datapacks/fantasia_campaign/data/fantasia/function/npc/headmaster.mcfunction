advancement revoke @s only fantasia:npc/headmaster
tellraw @s {"text":"헤론 · 마왕성","color":"gold"}
tellraw @s {"text":"벨카리온은 세 단계로 싸운다. 첫 육체를 쓰러뜨리고 서쪽과 동쪽 봉인석을 작동한 다음 폭주한 왕과 호위병을 쓰러뜨려라.","color":"white"}
tellraw @s [{"text":"[ 왕좌의 문 열기 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 50"}}]
execute if score @s fa_stage matches 6.. run function fantasia:ending/menu
tellraw @s [{"text":"[ 현재 목표 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 2"}},{"text":"[ 아카데미 귀환 ] ","color":"aqua","bold":true,"clickEvent":{"action":"run_command","value":"/trigger fa_action set 1"}}]
execute if entity @s[tag=fa_modded] run tellraw @s [{"text":"[ 대화 ] ","color":"yellow","clickEvent":{"action":"run_command","value":"/fantasia_npc headmaster talk"}},{"text":"[ 선물 ] ","color":"light_purple","clickEvent":{"action":"run_command","value":"/fantasia_npc headmaster gift"}},{"text":"[ 내 정보 ]","color":"white","clickEvent":{"action":"run_command","value":"/fantasia_stats"}}]
