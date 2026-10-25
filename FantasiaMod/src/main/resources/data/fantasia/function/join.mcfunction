execute unless score #ready fa_world matches 1 run return 0
execute if entity @s[tag=fa_joined] run return 0
tag @s add fa_joined
scoreboard players add @s fa_stage 0
scoreboard players add @s fa_gear 0
scoreboard players add @s fa_heal 0
scoreboard players add @s fa_supplies 0
scoreboard players add @s fa_prevdeath 0
scoreboard players add @s fa_ok 0
scoreboard players add @s fa_timer 0
scoreboard players add @s fa_archive 0
scoreboard players add @s fa_ending 0
scoreboard players add @s fa_mine 0
scoreboard players add @s fa_canal 0
scoreboard players add @s fa_forest 0
scoreboard players add @s fa_storm 0
scoreboard players add @s fa_north 0
scoreboard players add @s fa_east 0
scoreboard players add @s fa_south 0
scoreboard players add @s fa_deaths 0
scoreboard players operation @s fa_prevdeath = @s fa_deaths
scoreboard players set @s fa_action 0
execute in fantasia:campaign run tp @s 0 65 -8 0 0
execute in fantasia:campaign run spawnpoint @s 0 65 -8
gamemode adventure @s
effect give @s minecraft:resistance 10 4 true
tellraw @s {"text":"Fantasia: 균열의 왕 — 아델린을 우클릭해 이야기를 시작하세요. 아델린과 대화하면 입학 검사 화면이 열립니다.","color":"gold"}
tellraw @s {"text":"NPC 우클릭 → 버튼으로 이동/진행. 장비는 카일에게 수령, 회복은 세라핀에게 요청하세요.","color":"white"}
