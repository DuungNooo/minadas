scoreboard objectives add fa_world dummy
scoreboard objectives add fa_action dummy
scoreboard objectives add fa_stage dummy
scoreboard objectives add fa_gear dummy
scoreboard objectives add fa_heal dummy
scoreboard objectives add fa_supplies dummy
scoreboard objectives add fa_deaths deathCount
scoreboard objectives add fa_prevdeath dummy
scoreboard objectives add fa_ok dummy
scoreboard objectives add fa_timer dummy
scoreboard objectives add fa_archive dummy
scoreboard objectives add fa_ending dummy
scoreboard objectives add fa_mine dummy
scoreboard objectives add fa_canal dummy
scoreboard objectives add fa_forest dummy
scoreboard objectives add fa_storm dummy
scoreboard objectives add fa_north dummy
scoreboard objectives add fa_east dummy
scoreboard objectives add fa_south dummy
scoreboard players set #clock fa_world 0
execute unless score #ready fa_world matches 1 run function fantasia:map/restart
execute if score #ready fa_world matches 1 run function fantasia:resume
bossbar add fantasia:belkarion {"text":"벨카리온","color":"dark_purple"}
bossbar set fantasia:belkarion color purple
bossbar set fantasia:belkarion max 3
bossbar set fantasia:belkarion visible false
execute unless score #exp_ready fa_world matches 1 run function fantasia:expansion/restart
