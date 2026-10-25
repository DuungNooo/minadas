tag @s remove fa_fighting
tag @s remove fa_in_tutorial
tag @s remove fa_in_mine
tag @s remove fa_in_canal
tag @s remove fa_in_forest
tag @s remove fa_in_storm
tag @s remove fa_in_defense
tag @s remove fa_in_north
tag @s remove fa_in_east
tag @s remove fa_in_south
tag @s remove fa_in_castle
scoreboard players set @s fa_stage 0
scoreboard players set @s fa_gear 0
scoreboard players set @s fa_heal 0
scoreboard players set @s fa_supplies 0
scoreboard players set @s fa_ok 0
scoreboard players set @s fa_timer 0
scoreboard players set @s fa_archive 0
scoreboard players set @s fa_ending 0
scoreboard players set @s fa_mine 0
scoreboard players set @s fa_canal 0
scoreboard players set @s fa_forest 0
scoreboard players set @s fa_storm 0
scoreboard players set @s fa_north 0
scoreboard players set @s fa_east 0
scoreboard players set @s fa_south 0
scoreboard players operation @s fa_prevdeath = @s fa_deaths
advancement revoke @s only fantasia_research:campaign/intro
advancement revoke @s only fantasia_research:campaign/mine
advancement revoke @s only fantasia_research:campaign/canal
advancement revoke @s only fantasia_research:campaign/forest
advancement revoke @s only fantasia_research:campaign/storm
advancement revoke @s only fantasia_research:campaign/regions
advancement revoke @s only fantasia_research:campaign/defense
advancement revoke @s only fantasia_research:campaign/truth
advancement revoke @s only fantasia_research:campaign/north
advancement revoke @s only fantasia_research:campaign/east
advancement revoke @s only fantasia_research:campaign/south
advancement revoke @s only fantasia_research:campaign/fronts
advancement revoke @s only fantasia_research:campaign/castle
advancement revoke @s only fantasia_research:campaign/ending
tag @s remove fa_joined
function fantasia:join
tellraw @s {"text":"개인 캠페인 진행만 초기화했습니다. 맵과 다른 플레이어 진행은 유지됩니다.","color":"gold"}
