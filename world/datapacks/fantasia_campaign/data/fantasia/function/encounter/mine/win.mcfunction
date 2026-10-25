scoreboard players set #mine fa_world 0
execute as @a[tag=fa_in_mine] run scoreboard players set @s fa_mine 1
execute as @a[tag=fa_in_mine] run tellraw @s {"text":"광산을 확보했습니다. 서쪽 광부를 구출한 뒤 동쪽 화염핵을 회수하세요.","color":"green"}
tag @a[tag=fa_in_mine] remove fa_fighting
tag @a remove fa_in_mine
