scoreboard players set @s fa_canal 5
advancement grant @s only fantasia_research:campaign/canal
tag @s remove fa_in_canal
tag @s remove fa_fighting
tellraw @s {"text":"수로 복구 완료! 아카데미에서 다음 목적지를 선택하세요.","color":"green"}
give @s minecraft:golden_apple 2
experience add @s 5 levels
advancement grant @s only fantasia_research:course/dungeon/ender_golem
