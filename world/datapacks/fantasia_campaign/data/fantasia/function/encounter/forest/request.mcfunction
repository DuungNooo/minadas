scoreboard players set @s fa_ok 1
execute if score #forest fa_world matches 1 run tellraw @s {"text":"이미 전투가 진행 중입니다. 이 도전이 끝나거나 전원이 귀환한 뒤 다시 요청하세요.","color":"yellow"}
execute unless score #forest fa_world matches 1 run function fantasia:encounter/forest/start
