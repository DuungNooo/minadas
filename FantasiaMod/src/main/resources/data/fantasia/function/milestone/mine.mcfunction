scoreboard players set @s fa_mine 5
advancement grant @s only fantasia_research:campaign/mine
tag @s remove fa_in_mine
tag @s remove fa_fighting
tellraw @s {"text":"화염핵 회수와 광부 구출 완료! 아카데미에서 다음 목적지를 선택하세요.","color":"green"}
give @s minecraft:golden_apple 2
experience add @s 5 levels
advancement grant @s only fantasia_research:course/field/nether_entry
advancement grant @s only fantasia_research:course/field/blaze_combat
advancement grant @s only fantasia_research:course/field/blaze_sample
advancement grant @s only fantasia_research:course/dungeon/ignited_revenant
