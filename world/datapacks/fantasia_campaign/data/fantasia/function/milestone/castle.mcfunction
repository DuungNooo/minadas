scoreboard players set @s fa_stage 6
advancement grant @s only fantasia_research:campaign/castle
advancement grant @s only fantasia_research:course/graduation/capstone
advancement grant @s only fantasia_research:course/advanced/end_crystal
give @s minecraft:end_crystal
tag @s remove fa_in_castle
tag @s remove fa_fighting
tellraw @s {"text":"벨카리온의 폭주가 멈췄다. 마지막 선택은 당신에게 달렸다. 입구의 헤론에게 돌아가 결말을 선택하세요.","color":"gold"}
