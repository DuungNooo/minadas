scoreboard players add #wave_defense fa_world 1
execute as @a[tag=fa_in_defense] run effect give @s minecraft:instant_health 1 1 true
execute as @a[tag=fa_in_defense] run tellraw @s {"text":"다음 습격이 밀려옵니다! 방어선을 지켜 주세요.","color":"red"}
function fantasia:encounter/defense/spawn
