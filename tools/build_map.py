#!/usr/bin/env python3
"""Generate Fantasia's deterministic 1.21.1 map. Standard library only.

Only writes the map subtree and dimension/manifest owned by this generator.
Every world-edit command explicitly selects fantasia:campaign. Area construction
loads one bounded chunk rectangle, waits for it, edits in small batches, unloads,
and advances to the next area. Re-entering map/build while building is a no-op.
"""
from __future__ import annotations
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'world/datapacks/fantasia_campaign'
OUT = PACK / 'data/fantasia/function/map'
DIM = 'fantasia:campaign'
BATCH_SIZE = 48
AREAS = [
    ('academy', '아르카나 아카데미', 0, 0),
    ('mine', '불타는 광산', 160, 0),
    ('canal', '얼어붙은 수로', 0, 160),
    ('forest', '침식된 숲', -160, 0),
    ('storm', '낙뢰 평원', 0, -160),
    ('archive', '봉인서고와 지하 연구소', 160, 160),
    ('capital', '왕도 방어선', -160, 160),
    ('north', '북부 빙결 전선', -160, -160),
    ('east', '동부 자연 전선', 160, -160),
    ('south', '남부 화염 전선', 320, 0),
    ('castle', '벨카리온의 마왕성', 320, 160),
]

class Map:
    def __init__(self, ident, title, cx, cz):
        self.id, self.title, self.cx, self.cz = ident, title, cx, cz
        self.commands = []
        self.blocks = {}  # Small sparse semantic model used to check reserved paths.
        self.b = 34 if ident == 'castle' else 30

    def xyz(self, x, y, z):
        return f'{x+self.cx} {y} {z+self.cz}'

    def fill(self, x1, y1, z1, x2, y2, z2, block):
        assert x1 <= x2 and y1 <= y2 and z1 <= z2
        assert (x2-x1+1)*(y2-y1+1)*(z2-z1+1) <= 32768
        assert -self.b <= x1 <= x2 <= self.b and -self.b <= z1 <= z2 <= self.b
        self.commands.append(f'fill {self.xyz(x1,y1,z1)} {self.xyz(x2,y2,z2)} minecraft:{block}')
        # Track the floor/headroom around reserved walking routes, not all voxels.
        for x,y,z in self.reserved_points:
            if x1 <= x <= x2 and y1 <= y <= y2 and z1 <= z <= z2:
                self.blocks[x,y,z] = block.split('[')[0]

    def block(self,x,y,z,block):
        self.fill(x,y,z,x,y,z,block)

    @property
    def reserved_points(self):
        if hasattr(self, '_reserved'): return self._reserved
        pts = {(0, -20), (0,-14), (-8,0),(8,0)}
        if self.id == 'academy':
            pts.update({(0,-8),(0,0),(6,0),(-6,0),(0,8)})
            pts.update((x,z) for x in range(-7,8) for z in range(15,30) if x*x+(z-22)**2<=49)
        arena_z, radius = (15,15) if self.id == 'castle' else (5,10)
        pts.update((x,z) for x in range(-radius,radius+1) for z in range(arena_z-radius,arena_z+radius+1) if x*x+(z-arena_z)**2 <= radius**2)
        pts.update((x,z) for x in range(-1,2) for z in range(-20,arena_z+1))
        pts.update((x,z) for x in range(-8,9) for z in range(-1,2))
        self._reserved={(x,y,z) for x,z in pts for y in [64,65,66,67]}
        return self._reserved

    def foundation(self, floor, edge):
        b=self.b
        for x in range(-b,b+1,8):
            self.fill(x,60,-b,min(x+7,b),103,b,'air')
        self.fill(-b+3,60,-b+3,b-3,61,b-3,'deepslate_tiles')
        self.fill(-b+1,62,-b+1,b-1,63,b-1,edge)
        self.fill(-b,64,-b,b,64,b,floor)
        for x1,z1,x2,z2 in [(-b,-b,b,-b),(-b,b,b,b),(-b,-b,-b,b),(b,-b,b,b)]:
            self.fill(x1,65,z1,x2,65,z2,edge+'_wall' if edge in ['stone_brick','polished_blackstone_brick'] else 'stone_brick_wall')
        # Illuminated edge corners and safe cross-avenues.
        for x in [-b+1,b-1]:
            for z in [-b+1,b-1]: self.lamp(x,z)
        self.fill(-3,64,-b+1,3,64,b-1,'polished_andesite')
        self.fill(-b+1,64,-3,b-1,64,3,'polished_andesite')
        for z in range(-b+3,b-2,8):
            self.block(-4,64,z,'sea_lantern'); self.block(4,64,z,'sea_lantern')
        for x in range(-b+3,b-2,8):
            self.block(x,64,-4,'sea_lantern'); self.block(x,64,4,'sea_lantern')

    def lamp(self,x,z,pole='dark_oak_fence',light='lantern'):
        self.fill(x,65,z,x,67,z,pole); self.block(x,68,z,light)

    def room(self,x1,z1,x2,z2,wall='stone_bricks',roof='dark_oak_planks',floor='spruce_planks',height=7):
        self.fill(x1,64,z1,x2,64,z2,floor)
        self.fill(x1,65,z1,x2,64+height,z2,wall)
        self.fill(x1+1,65,z1+1,x2-1,63+height,z2-1,'air')
        self.fill(x1-1,65+height,z1-1,x2+1,65+height,z2+1,roof)
        mx=(x1+x2)//2; mz=(z1+z2)//2
        # Two clear entrances, wide enough for player/mob navigation.
        self.fill(mx-1,65,z1,mx+1,67,z1,'air')
        self.fill(mx-1,65,z2,mx+1,67,z2,'air')
        for x in [x1,x2]: self.fill(x,67,mz-1,x,68,mz+1,'glass_pane')
        self.block(mx,64,mz,'sea_lantern')
        self.block(mx,63+height,mz,'lantern[hanging=true]')

    def arch(self,x,z,block='quartz_pillar',axis='x',width=4,height=6):
        if axis=='x':
            for dx in [-width,width]: self.fill(x+dx,65,z,x+dx,65+height,z,block)
            self.fill(x-width,65+height,z,x+width,65+height,z,block)
        else:
            for dz in [-width,width]: self.fill(x,65,z+dz,x,65+height,z+dz,block)
            self.fill(x,65+height,z-width,x,65+height,z+width,block)

    def tree(self,x,z,log='oak_log',leaves='oak_leaves',height=5):
        self.fill(x-2,66+height,z-2,x+2,67+height,z+2,leaves+'[persistent=true]')
        self.fill(x-1,68+height,z-1,x+1,68+height,z+1,leaves+'[persistent=true]')
        self.fill(x,65,z,x,65+height,z,log)

    def tower(self,x,z,block='stone_bricks',height=13):
        self.fill(x-3,65,z-3,x+3,64+height,z+3,block)
        self.fill(x-2,65,z-2,x+2,63+height,z+2,'air')
        self.fill(x-4,64+height,z-4,x+4,64+height,z+4,block)
        for dx,dz in [(-4,-4),(-4,4),(4,-4),(4,4)]: self.block(x+dx,65+height,z+dz,block)
        self.fill(x-1,65,z-3,x+1,67,z-3,'air')
        self.fill(x-1,65,z+3,x+1,67,z+3,'air')
        self.fill(x-3,69,z-1,x-3,71,z+1,'glass_pane')
        self.fill(x+3,69,z-1,x+3,71,z+1,'glass_pane')
        self.block(x,64,z,'sea_lantern')

    def sign(self,x,z,text):
        # Text display is encoded in a normal sign; no extra entities/dependencies.
        component=json.dumps({'text':text,'color':'dark_purple'},ensure_ascii=False,separators=(',',':'))
        self.commands.append(f'setblock {self.xyz(x,65,z)} minecraft:oak_sign[rotation=0]{{front_text:{{messages:[\'{component}\',\'{{"text":""}}\',\'{{"text":""}}\',\'{{"text":"Fantasia"}}\']}},is_waxed:1b}}')

    def ring(self,cx,cz,r,block):
        for x in range(cx-r,cx+r+1):
            for z in range(cz-r,cz+r+1):
                d=(x-cx)**2+(z-cz)**2
                if (r-1)**2 <= d <= r*r: self.block(x,64,z,block)

    def validate(self):
        for (x,y,z),block in self.blocks.items():
            if y==64: assert block != 'air', (self.id,'missing floor',x,z)
            else: assert block=='air', (self.id,'blocked reserved route',x,y,z,block)
        assert len(self.blocks)==len(self.reserved_points), self.id


def build(m):
    ident=m.id
    floor={'academy':'smooth_quartz','mine':'polished_basalt','canal':'snow_block','forest':'grass_block','storm':'mossy_stone_bricks','archive':'chiseled_stone_bricks','capital':'stone_bricks','north':'snow_block','east':'moss_block','south':'nether_bricks','castle':'polished_blackstone_bricks'}[ident]
    m.foundation(floor, 'stone_bricks')
    if ident=='academy':
        for x in [-21,21]:
            m.tower(x,21,'quartz_bricks',15)
            m.room(x-7,-27,x+7,-12,'quartz_bricks','deepslate_tile_slab','polished_diorite',8)
        m.arch(0,-24,'quartz_pillar',height=8)
        m.ring(0,22,7,'yellow_glazed_terracotta')
        # Open training court, rune circle, planted courtyards, library desks.
        m.ring(0,5,10,'purple_glazed_terracotta')
        for x in [-24,-18,18,24]:
            m.block(x,65,-24,'bookshelf'); m.block(x,66,-24,'bookshelf')
            m.block(x,65,-14,'lectern[facing=south]')
        m.block(-21,65,-20,'enchanting_table')
        m.block(21,65,-20,'brewing_stand')
        m.block(23,65,-20,'water_cauldron[level=3]')
        for x in [17,21,25]:
            m.block(x,65,14,'hay_block')
            m.block(x,66,14,'target')
        m.sign(-17,-16,'마법부여 실습실')
        m.sign(17,-16,'연금 실습실')
        m.sign(17,10,'표적의 중심을 조준하세요')
        for x in [-25,25]:
            for z in [-8,8]: m.tree(x,z,'cherry_log','cherry_leaves',4)
        for x in [-11,11]:
            m.lamp(x,-12,'quartz_pillar'); m.lamp(x,18,'quartz_pillar')
        m.sign(5,-19,'아르카나 아카데미')
    elif ident=='mine':
        # Pillared mine galleries at the sides, glowing glass-covered lava vents.
        for x in [-22,22]:
            m.room(x-6,-27,x+6,-11,'deepslate_bricks','deepslate_tiles','cobbled_deepslate',7)
            for z in [-23,-17]:
                m.fill(x-4,65,z,x-4,70,z,'stripped_spruce_log')
                m.fill(x+4,65,z,x+4,70,z,'stripped_spruce_log')
                m.fill(x-4,70,z,x+4,70,z,'spruce_planks')
            m.fill(x-2,64,-25,x+2,64,-13,'rail[shape=north_south]')
        for x in [-23,23]:
            m.fill(x-4,64,8,x+4,64,20,'magma_block')
            m.fill(x-3,65,9,x+3,65,19,'orange_stained_glass')
            m.fill(x-2,66,12,x+2,71,16,'basalt')
            m.block(x,72,14,'glowstone')
        m.ring(0,5,10,'gilded_blackstone')
        m.arch(0,-25,'polished_basalt',height=7)
        m.sign(5,-20,'불타는 광산')
    elif ident=='canal':
        for x in [-18,18]:
            m.fill(x-3,64,-27,x+3,64,27,'packed_ice')
            m.fill(x-2,64,-26,x+2,64,26,'water')
            m.fill(x-3,64,-3,x+3,64,3,'dark_oak_planks')
            m.fill(x-3,65,-4,x+3,65,-4,'dark_oak_fence')
            m.fill(x-3,65,4,x+3,65,4,'dark_oak_fence')
        for x in [-24,24]:
            m.tower(x,-21,'packed_ice',11)
            m.fill(x-2,65,21,x+2,70,25,'blue_ice')
            m.block(x,71,23,'sea_lantern')
        m.arch(0,-24,'packed_ice',height=7)
        m.ring(0,5,10,'cyan_glazed_terracotta')
        m.sign(5,-20,'얼어붙은 수로')
    elif ident=='forest':
        for x,z,h in [(-24,-22,7),(23,-22,6),(-23,21,8),(23,22,7),(-25,-6,5),(25,-7,5),(-24,8,6),(24,7,6)]:
            m.tree(x,z,height=h)
        m.room(-26,-25,-13,-13,'mossy_stone_bricks','moss_block','mossy_cobblestone',5)
        m.fill(17,64,-24,25,64,-16,'water')
        m.fill(18,65,-23,24,65,-17,'lily_pad')
        for x,z in [(-17,19),(19,18),(-19,-8),(17,-9)]:
            m.block(x,65,z,'red_mushroom'); m.block(x+1,65,z,'brown_mushroom')
            m.block(x,64,z-1,'shroomlight')
        m.arch(0,-25,'mossy_stone_bricks',height=6)
        m.ring(0,5,10,'mossy_cobblestone')
        m.sign(5,-20,'침식된 숲')
    elif ident=='storm':
        for x,z in [(-23,-22),(23,-22),(-23,22),(23,22)]:
            m.tower(x,z,'cut_copper',10)
            m.fill(x,75,z,x,78,z,'lightning_rod[facing=up]')
            m.block(x,74,z,'copper_bulb[lit=true]')
        for x in [-19,19]:
            m.fill(x-3,65,-8,x+3,65,-6,'waxed_oxidized_cut_copper_slab')
            m.fill(x-3,65,7,x+3,65,9,'waxed_oxidized_cut_copper_slab')
        m.arch(0,-25,'waxed_cut_copper',height=7)
        m.ring(0,5,10,'yellow_glazed_terracotta')
        m.sign(5,-20,'낙뢰 평원')
    elif ident=='archive':
        for x in [-21,21]:
            m.room(x-7,-27,x+7,26,'deepslate_bricks','dark_prismarine','polished_diorite',10)
            # Side doors open directly onto the central investigation corridor.
            inner=x+7 if x<0 else x-7
            m.fill(inner,65,-2,inner,68,2,'air')
            for z in range(-23,24,6):
                m.fill(x-5,65,z,x-3,68,z,'bookshelf')
                m.fill(x+3,65,z,x+5,68,z,'bookshelf')
                m.block(x,64,z,'sea_lantern')
            m.block(x,65,-18,'enchanting_table')
            m.block(x,65,18,'brewing_stand')
            m.block(x,65,21,'cauldron')
        m.arch(0,-25,'chiseled_deepslate',height=8)
        m.ring(0,5,10,'purple_glazed_terracotta')
        m.sign(5,-20,'봉인서고 · 연구소')
    elif ident=='capital':
        for x in [-22,22]:
            for z in [-20,21]:
                m.room(x-6,z-7,x+6,z+7,'bricks','dark_oak_planks','spruce_planks',7)
                m.block(x-3,65,z,'barrel'); m.block(x+3,65,z,'crafting_table')
            m.lamp(x,-8); m.lamp(x,8)
        m.arch(0,-25,'stone_bricks',height=10,width=5)
        m.arch(0,25,'stone_bricks',height=8,width=5)
        for x in [-11,11]:
            m.fill(x,65,-12,x,66,-7,'oak_fence')
        m.ring(0,5,10,'red_glazed_terracotta')
        m.sign(6,-20,'왕도 · 시민 대피소')
    elif ident=='north':
        for x in [-22,22]:
            m.room(x-6,-27,x+6,-12,'packed_ice','blue_ice','snow_block',6)
            for z in [18,24]:
                m.fill(x-3,65,z-2,x+3,68,z+2,'packed_ice')
                m.fill(x-1,69,z-1,x+1,73,z+1,'blue_ice')
                m.block(x,74,z,'sea_lantern')
        m.arch(0,-25,'blue_ice',height=8)
        m.ring(0,5,10,'light_blue_glazed_terracotta')
        m.sign(5,-20,'북부 빙결 전선')
    elif ident=='east':
        for x,z in [(-23,-23),(23,-23),(-23,22),(23,22),(-24,-7),(24,-7),(-24,8),(24,8)]:
            m.tree(x,z,'dark_oak_log','dark_oak_leaves',7)
        m.room(-27,-26,-14,-14,'mud_bricks','moss_block','packed_mud',6)
        m.room(14,-26,27,-14,'mud_bricks','moss_block','packed_mud',6)
        for x in [-19,19]:
            for z in [17,23]: m.block(x,65,z,'flowering_azalea')
        m.arch(0,-25,'mossy_cobblestone',height=7)
        m.ring(0,5,10,'green_glazed_terracotta')
        m.sign(5,-20,'동부 자연 전선')
    elif ident=='south':
        for x in [-23,23]:
            for z in [-22,22]:
                m.tower(x,z,'red_nether_bricks',10)
                m.fill(x-2,75,z-2,x+2,75,z+2,'shroomlight')
                m.fill(x-3,76,z-3,x+3,76,z+3,'red_stained_glass')
        for x in [-21,21]:
            m.fill(x-3,64,-9,x+3,64,9,'magma_block')
            m.fill(x-2,65,-8,x+2,65,8,'red_stained_glass')
        m.arch(0,-25,'red_nether_bricks',height=8)
        m.ring(0,5,10,'orange_glazed_terracotta')
        m.sign(5,-20,'남부 화염 전선')
    elif ident=='castle':
        for x in [-29,29]:
            for z in [-29,29]: m.tower(x,z,'polished_blackstone_bricks',20)
        for x in [-25,25]:
            m.fill(x,65,-25,x,78,25,'polished_blackstone_bricks')
            for z in range(-24,25,4): m.block(x,79,z,'chiseled_polished_blackstone')
        m.fill(-25,65,32,25,78,32,'polished_blackstone_bricks')
        m.fill(-25,65,-25,-6,76,-25,'polished_blackstone_bricks')
        m.fill(6,65,-25,25,76,-25,'polished_blackstone_bricks')
        m.arch(0,-25,'chiseled_polished_blackstone',height=13,width=5)
        m.fill(-3,64,-24,3,64,8,'red_nether_bricks')
        m.ring(0,15,15,'crying_obsidian')
        m.ring(0,15,11,'gilded_blackstone')
        for x in [-20,20]:
            for z in [-18,-6,8,22]: m.lamp(x,z,'polished_blackstone_wall','soul_lantern')
        m.fill(-3,65,31,3,69,31,'chiseled_polished_blackstone')
        m.block(0,70,31,'redstone_block')
        m.sign(6,-20,'벨카리온의 마왕성')
    m.validate()


def write_func(name, commands):
    p=OUT/(name+'.mcfunction'); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text('# Generated by tools/build_map.py. Do not hand edit.\n'+'\n'.join(commands)+'\n',encoding='utf-8')


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    # Remove only generator-owned function files; campaign functions live elsewhere.
    for old in OUT.rglob('*.mcfunction'): old.unlink()
    dimension={'type':'minecraft:overworld','generator':{'type':'minecraft:flat','settings':{'biome':'minecraft:plains','features':False,'lakes':False,'layers':[{'height':1,'block':'minecraft:air'}],'structure_overrides':[]}}}
    dp=PACK/'data/fantasia/dimension/campaign.json'; dp.parent.mkdir(parents=True,exist_ok=True)
    dp.write_text(json.dumps(dimension,ensure_ascii=False,indent=2)+'\n')
    maps=[]
    for area in AREAS:
        m=Map(*area); build(m); maps.append(m)
    write_func('build',[
        'scoreboard objectives add fa_world dummy',
        'execute if score #ready fa_world matches 1 run return 0',
        'execute if score #building fa_world matches 1 run return 0',
        'scoreboard players set #building fa_world 1',
        'scoreboard players set #ready fa_world 0',
        'function fantasia:map/academy/load',
    ])
    for i,m in enumerate(maps):
        bounds=f'{m.cx-m.b} {m.cz-m.b} {m.cx+m.b} {m.cz+m.b}'
        write_func(f'{m.id}/load',[
            f'execute in {DIM} run forceload add {bounds}',
            f'schedule function fantasia:map/{m.id}/wait 10t replace',
        ])
        chunks=[(x,z) for x in range((m.cx-m.b)//16,(m.cx+m.b)//16+1) for z in range((m.cz-m.b)//16,(m.cz+m.b)//16+1)]
        wait=['scoreboard players set #chunks fa_world 0']
        wait += [f'execute in {DIM} if loaded {x*16} 64 {z*16} run scoreboard players add #chunks fa_world 1' for x,z in chunks]
        wait += [f'execute unless score #chunks fa_world matches {len(chunks)} run schedule function fantasia:map/{m.id}/wait 10t replace',
                 f'execute if score #chunks fa_world matches {len(chunks)} run function fantasia:map/{m.id}/000']
        write_func(f'{m.id}/wait',wait)
        batches=[m.commands[j:j+BATCH_SIZE] for j in range(0,len(m.commands),BATCH_SIZE)]
        for bi,batch in enumerate(batches):
            commands=[f'execute in {DIM} run {cmd}' for cmd in batch]
            if bi+1<len(batches): commands += [f'schedule function fantasia:map/{m.id}/{bi+1:03} 1t replace']
            else:
                commands += [f'execute in {DIM} run forceload remove {bounds}']
                if i+1<len(maps): commands += [f'function fantasia:map/{maps[i+1].id}/load']
                else: commands += ['function fantasia:map/complete']
            write_func(f'{m.id}/{bi:03}',commands)
    write_func('complete',[
        'scoreboard players set #building fa_world 0',
        'scoreboard players set #ready fa_world 1',
        'tellraw @a {"text":"[Fantasia] 아카데미와 10개 지역이 준비되었습니다.","color":"gold"}',
    ])
    manifest={'minecraft':'1.21.1','dimension':DIM,'ground_y':64,'build_function':'fantasia:map/build','ready_score':'#ready fa_world = 1','areas':[]}
    for m in maps:
        manifest['areas'].append({'id':m.id,'name':m.title,'center':[m.cx,65,m.cz], 'arrival':[m.cx,65,m.cz-20], 'npc':[m.cx,65,m.cz-14], 'stations':[[m.cx-8,65,m.cz],[m.cx+8,65,m.cz]], 'arena_center':[m.cx,65,m.cz+(15 if m.id=='castle' else 5)],'arena_radius':15 if m.id=='castle' else 10,'bounds':[m.cx-m.b,m.cz-m.b,m.cx+m.b,m.cz+m.b],'commands':len(m.commands)})
    (ROOT/'fantasia_content/MAP_LAYOUT.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'areas':len(maps),'world_edit_commands':sum(len(m.commands) for m in maps),'functions':len(list(OUT.rglob('*.mcfunction'))),'validated':'reserved floors, headroom, bounds, fill volumes'},indent=2))

if __name__=='__main__': main()
