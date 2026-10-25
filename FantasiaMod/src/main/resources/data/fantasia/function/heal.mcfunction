scoreboard players set @s fa_ok 1
scoreboard players set @s fa_heal 30
effect give @s minecraft:instant_health 1 5 true
effect give @s minecraft:saturation 1 3 true
give @s minecraft:cooked_beef 16
give @s minecraft:arrow 32
tellraw @s {"text":"회복 완료. 다음 보급은 30초 뒤에 받을 수 있습니다.","color":"green"}
