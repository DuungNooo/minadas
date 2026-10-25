scoreboard players set #wave_castle fa_world 2
scoreboard players set #kills_castle fa_world 0
scoreboard players set #need_castle fa_world 999
bossbar set fantasia:belkarion value 2
execute as @a[tag=fa_in_castle] run tellraw @s {"text":"봉인 붕괴! 서쪽과 동쪽 봉인석을 가까이서 우클릭해 안정화하세요.","color":"light_purple"}
execute as @a[tag=fa_in_castle] run effect give @s minecraft:regeneration 6 1 true
