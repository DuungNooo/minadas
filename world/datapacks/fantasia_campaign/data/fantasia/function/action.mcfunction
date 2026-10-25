scoreboard players set @s fa_ok 0
execute if score @s fa_action matches 1 if dimension fantasia:campaign if entity @e[tag=fa_npc,distance=..7,limit=1] run function fantasia:home
execute if score @s fa_action matches 2 run function fantasia:status
execute if score @s fa_action matches 2 run scoreboard players set @s fa_ok 1
execute if score @s fa_action matches 11 if dimension fantasia:campaign positioned 6 65 0 if entity @s[distance=..7] if score @s fa_gear matches 0 run function fantasia:gear
execute if score @s fa_action matches 12 if dimension fantasia:campaign positioned 6 65 0 if entity @s[distance=..7] if score @s fa_stage matches 0 if score @s fa_gear matches 1.. if entity @s[advancements={fantasia_research:exam/complete=true}] run function fantasia:encounter/tutorial/request
execute if score @s fa_action matches 13 if dimension fantasia:campaign positioned -6 65 0 if entity @s[distance=..7] if score @s fa_heal matches 0 run function fantasia:heal
execute if score @s fa_action matches 14 if dimension fantasia:campaign positioned 6 65 0 if entity @s[distance=..7] if score @s fa_supplies matches 0 if entity @s[advancements={fantasia_research:exam/complete=true}] run function fantasia:supplies
execute if score @s fa_action matches 20 if dimension fantasia:campaign positioned 160 65 -14 if entity @s[distance=..7] if score @s fa_stage matches 1 if score @s fa_mine matches 0 run function fantasia:encounter/mine/request
execute if score @s fa_action matches 21 if dimension fantasia:campaign positioned 0 65 146 if entity @s[distance=..7] if score @s fa_stage matches 1 if score @s fa_canal matches 3 run function fantasia:encounter/canal/request
execute if score @s fa_action matches 22 if dimension fantasia:campaign positioned -160 65 -14 if entity @s[distance=..7] if score @s fa_stage matches 1 if score @s fa_forest matches 3 run function fantasia:encounter/forest/request
execute if score @s fa_action matches 23 if dimension fantasia:campaign positioned 0 65 -174 if entity @s[distance=..7] if score @s fa_stage matches 1 if score @s fa_storm matches 3 run function fantasia:encounter/storm/request
execute if score @s fa_action matches 30 if dimension fantasia:campaign positioned -160 65 146 if entity @s[distance=..7] if score @s fa_stage matches 2 run function fantasia:encounter/defense/request
execute if score @s fa_action matches 31 if dimension fantasia:campaign positioned 160 65 146 if entity @s[distance=..7] if score @s fa_stage matches 3 if score @s fa_archive matches 3 run function fantasia:milestone/truth
execute if score @s fa_action matches 40 if dimension fantasia:campaign positioned -160 65 -174 if entity @s[distance=..7] if score @s fa_stage matches 4 if score @s fa_north matches 0 run function fantasia:encounter/north/request
execute if score @s fa_action matches 41 if dimension fantasia:campaign positioned 160 65 -174 if entity @s[distance=..7] if score @s fa_stage matches 4 if score @s fa_east matches 0 run function fantasia:encounter/east/request
execute if score @s fa_action matches 42 if dimension fantasia:campaign positioned 320 65 -14 if entity @s[distance=..7] if score @s fa_stage matches 4 if score @s fa_south matches 0 run function fantasia:encounter/south/request
execute if score @s fa_action matches 50 if dimension fantasia:campaign positioned 320 65 140 if entity @s[distance=..7] if score @s fa_stage matches 5 run function fantasia:encounter/castle/request
execute if score @s fa_action matches 101 if dimension fantasia:campaign positioned 0 65 0 if entity @s[distance=..7] if score @s fa_stage matches 1.. unless entity @s[tag=fa_fighting] run function fantasia:travel/mine
execute if score @s fa_action matches 102 if dimension fantasia:campaign positioned 0 65 0 if entity @s[distance=..7] if score @s fa_stage matches 1.. unless entity @s[tag=fa_fighting] run function fantasia:travel/canal
execute if score @s fa_action matches 103 if dimension fantasia:campaign positioned 0 65 0 if entity @s[distance=..7] if score @s fa_stage matches 1.. unless entity @s[tag=fa_fighting] run function fantasia:travel/forest
execute if score @s fa_action matches 104 if dimension fantasia:campaign positioned 0 65 0 if entity @s[distance=..7] if score @s fa_stage matches 1.. unless entity @s[tag=fa_fighting] run function fantasia:travel/storm
execute if score @s fa_action matches 105 if dimension fantasia:campaign positioned 0 65 0 if entity @s[distance=..7] if score @s fa_stage matches 2.. unless entity @s[tag=fa_fighting] run function fantasia:travel/capital
execute if score @s fa_action matches 106 if dimension fantasia:campaign positioned 0 65 0 if entity @s[distance=..7] if score @s fa_stage matches 3.. unless entity @s[tag=fa_fighting] run function fantasia:travel/archive
execute if score @s fa_action matches 107 if dimension fantasia:campaign positioned 0 65 0 if entity @s[distance=..7] if score @s fa_stage matches 4.. unless entity @s[tag=fa_fighting] run function fantasia:travel/north
execute if score @s fa_action matches 108 if dimension fantasia:campaign positioned 0 65 0 if entity @s[distance=..7] if score @s fa_stage matches 4.. unless entity @s[tag=fa_fighting] run function fantasia:travel/east
execute if score @s fa_action matches 109 if dimension fantasia:campaign positioned 0 65 0 if entity @s[distance=..7] if score @s fa_stage matches 4.. unless entity @s[tag=fa_fighting] run function fantasia:travel/south
execute if score @s fa_action matches 110 if dimension fantasia:campaign positioned 0 65 0 if entity @s[distance=..7] if score @s fa_stage matches 5.. unless entity @s[tag=fa_fighting] run function fantasia:travel/castle
execute if score @s fa_action matches 61 if dimension fantasia:campaign positioned 320 65 140 if entity @s[distance=..7] if score @s fa_stage matches 6 run function fantasia:ending/1
execute if score @s fa_action matches 62 if dimension fantasia:campaign positioned 320 65 140 if entity @s[distance=..7] if score @s fa_stage matches 6 run function fantasia:ending/2
execute if score @s fa_action matches 63 if dimension fantasia:campaign positioned 320 65 140 if entity @s[distance=..7] if score @s fa_stage matches 6 run function fantasia:ending/3
execute if score @s fa_action matches 64 if dimension fantasia:campaign positioned 320 65 140 if entity @s[distance=..7] if score @s fa_stage matches 6 run function fantasia:ending/4
execute if score @s fa_ok matches 0 run tellraw @s {"text":"지금은 사용할 수 없는 선택지입니다. 해당 NPC에게 가까이 가서 현재 조건과 목표를 확인하세요.","color":"yellow"}
scoreboard players set @s fa_action 0
scoreboard players enable @s fa_action
