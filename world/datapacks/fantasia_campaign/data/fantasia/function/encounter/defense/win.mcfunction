execute if score #wave_defense fa_world matches 3 run function fantasia:encounter/defense/finish
execute if score #defense fa_world matches 1 if score #wave_defense fa_world matches 1..2 run function fantasia:encounter/defense/next
