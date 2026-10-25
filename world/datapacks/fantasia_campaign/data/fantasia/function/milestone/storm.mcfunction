scoreboard players set @s fa_storm 5
advancement grant @s only fantasia_research:campaign/storm
tag @s remove fa_in_storm
tag @s remove fa_fighting
tellraw @s {"text":"낙뢰 평원 안정화 완료! 아카데미에서 다음 목적지를 선택하세요.","color":"green"}
advancement grant @s only fantasia_research:lightning_tier_1
advancement grant @s only fantasia_research:lightning_tier_2
give @s minecraft:golden_apple 2
experience add @s 5 levels
