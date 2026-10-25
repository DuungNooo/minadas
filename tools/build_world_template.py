"""Write a fresh Minecraft 1.21.1 world header; map is built on first launch.

Never copies player data or existing region files. Requires nbtlib.
"""
from pathlib import Path
import nbtlib as n

ROOT=Path(__file__).resolve().parents[1]

def tag(value):
    if isinstance(value,bool):return n.Byte(int(value))
    if isinstance(value,int):return n.Int(value)
    if isinstance(value,str):return n.String(value)
    if isinstance(value,list):return n.List[n.String]([n.String(v) for v in value])
    return n.Compound({k:tag(v) for k,v in value.items()})

def main():
    import json
    campaign=json.loads((ROOT/'world/datapacks/fantasia_campaign/data/fantasia/dimension/campaign.json').read_text())
    # NBT numeric layers must be lists of compounds, not JSON strings.
    def convert(v):
        if isinstance(v,list):
            if not v:return n.List[n.String]()
            items=[convert(x) for x in v]
            return n.List[type(items[0])](items)
        if isinstance(v,dict):return n.Compound({k:convert(x) for k,x in v.items()})
        return tag(v)
    dims={
      'minecraft:overworld':{'type':'minecraft:overworld','generator':{'type':'minecraft:flat','settings':{'biome':'minecraft:plains','features':False,'lakes':False,'layers':[{'height':1,'block':'minecraft:bedrock'},{'height':2,'block':'minecraft:dirt'},{'height':1,'block':'minecraft:grass_block'}],'structure_overrides':[]}}},
      'minecraft:the_nether':{'type':'minecraft:the_nether','generator':{'type':'minecraft:noise','settings':'minecraft:nether','biome_source':{'type':'minecraft:multi_noise','preset':'minecraft:nether'}}},
      'minecraft:the_end':{'type':'minecraft:the_end','generator':{'type':'minecraft:noise','settings':'minecraft:end','biome_source':{'type':'minecraft:the_end'}}},
      'fantasia:campaign':campaign}
    data=convert({'DataVersion':3955,'version':19133,'Version':{'Id':3955,'Name':'1.21.1','Series':'main','Snapshot':False},'LevelName':'Fantasia - 균열의 왕 1.1.0','GameType':2,'hardcore':False,'allowCommands':False,'initialized':True,'Difficulty':2,'DifficultyLocked':False,'SpawnX':0,'SpawnY':-60,'SpawnZ':0,'DataPacks':{'Enabled':['vanilla','file/fantasia_all_spells','file/fantasia_campaign'],'Disabled':[]},'enabled_features':['minecraft:vanilla'],'GameRules':{'keepInventory':'true','mobGriefing':'false','doFireTick':'false','doMobSpawning':'false'},'WorldGenSettings':{'generate_features':False,'bonus_chest':False,'dimensions':dims}})
    data['Difficulty']=n.Byte(2)
    data['WorldGenSettings']['seed']=n.Long(1849246584)
    data['Time']=n.Long(0);data['DayTime']=n.Long(6000);data['LastPlayed']=n.Long(0)
    data['SpawnAngle']=n.Float(0)
    path=ROOT/'world/level.dat'
    n.File({'':n.Compound({'Data':data})}).save(path,gzipped=True)
    loaded=n.load(path)
    assert int(loaded['']['Data']['DataVersion'])==3955
    assert str(loaded['']['Data']['LevelName']).startswith('Fantasia')
    print('Created fresh world header; terrain and map require first launch:',path)

if __name__=='__main__':main()
