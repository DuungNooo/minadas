scoreboard players set #actor_chunks fa_world 0
execute in fantasia:campaign if loaded -176 65 0 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded -160 65 -176 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded -160 65 -16 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded -160 65 0 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded -160 65 144 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded -16 65 -160 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded -16 65 0 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded -16 65 160 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded 0 65 -176 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded 0 65 -160 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded 0 65 0 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded 0 65 144 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded 0 65 160 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded 144 65 0 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded 144 65 160 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded 160 65 -176 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded 160 65 -16 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded 160 65 0 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded 160 65 144 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded 160 65 160 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded 304 65 160 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded 320 65 -16 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded 320 65 128 run scoreboard players add #actor_chunks fa_world 1
execute in fantasia:campaign if loaded 320 65 160 run scoreboard players add #actor_chunks fa_world 1
execute unless score #actor_chunks fa_world matches 24 run schedule function fantasia:npc/wait 10t replace
execute if score #actor_chunks fa_world matches 24 in fantasia:campaign run function fantasia:npc/spawn
