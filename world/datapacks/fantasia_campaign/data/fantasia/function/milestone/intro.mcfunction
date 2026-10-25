scoreboard players set @s fa_stage 1
advancement grant @s only fantasia_research:campaign/intro
advancement grant @s only fantasia_research:course/foundation/combat
tag @s remove fa_in_tutorial
tag @s remove fa_fighting
tellraw @s {"text":"견습 마도사 임명. 이제 아델린에게 돌아가 네 지역을 원하는 순서로 조사하세요.","color":"green"}
