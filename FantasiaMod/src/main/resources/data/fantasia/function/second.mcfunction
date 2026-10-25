scoreboard players remove @a[scores={fa_heal=1..}] fa_heal 1
scoreboard players remove @a[scores={fa_supplies=1..}] fa_supplies 1
execute as @a[tag=fa_joined] at @s unless score @s fa_deaths = @s fa_prevdeath run function fantasia:recover
execute as @a[tag=fa_joined] at @s if dimension fantasia:campaign if entity @s[y=-64,dy=108] run function fantasia:recover
execute as @a[scores={fa_timer=1..}] run scoreboard players remove @s fa_timer 1
execute as @a[scores={fa_storm=1..2,fa_timer=0}] run function fantasia:puzzle/storm_timeout
execute in fantasia:campaign if score #tutorial fa_world matches 1 run function fantasia:encounter/tutorial/tick
execute in fantasia:campaign if score #mine fa_world matches 1 run function fantasia:encounter/mine/tick
execute in fantasia:campaign if score #canal fa_world matches 1 run function fantasia:encounter/canal/tick
execute in fantasia:campaign if score #forest fa_world matches 1 run function fantasia:encounter/forest/tick
execute in fantasia:campaign if score #storm fa_world matches 1 run function fantasia:encounter/storm/tick
execute in fantasia:campaign if score #defense fa_world matches 1 run function fantasia:encounter/defense/tick
execute in fantasia:campaign if score #north fa_world matches 1 run function fantasia:encounter/north/tick
execute in fantasia:campaign if score #east fa_world matches 1 run function fantasia:encounter/east/tick
execute in fantasia:campaign if score #south fa_world matches 1 run function fantasia:encounter/south/tick
execute in fantasia:campaign if score #castle fa_world matches 1 run function fantasia:encounter/castle/tick
execute as @a[scores={fa_stage=1,fa_mine=5,fa_canal=5,fa_forest=5,fa_storm=5}] run function fantasia:milestone/regions
execute as @a[scores={fa_stage=4,fa_north=5,fa_east=5,fa_south=5}] run function fantasia:milestone/fronts
