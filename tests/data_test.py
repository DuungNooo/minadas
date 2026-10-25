"""Cross-resource checks for the actual shipped quest/progression content."""
from pathlib import Path
import json
import re
import unittest
import nbtlib

ROOT=Path(__file__).resolve().parents[1]
PACKS=ROOT/'world/datapacks'
ADV={}
for path in PACKS.glob('*/data/*/advancement/**/*.json'):
    parts=path.relative_to(PACKS).parts
    ADV[f'{parts[2]}:{"/".join(parts[4:])[:-5]}']=json.loads(path.read_text())

class ContentTests(unittest.TestCase):
    def test_advancement_parents_and_functions_exist(self):
        for name,data in ADV.items():
            if 'parent' in data:self.assertIn(data['parent'],ADV,name)
            function=data.get('rewards',{}).get('function')
            if function:
                ns,rel=function.split(':')
                self.assertTrue(list(PACKS.glob(f'*/data/{ns}/function/{rel}.mcfunction')),function)
            self.assertTrue(data.get('criteria'),name)
            for criterion in data['criteria'].values():
                self.assertTrue(criterion['trigger'].startswith('minecraft:'),name)

    def test_quest_files_are_real_snbt_and_ids_references_are_consistent(self):
        ids=set();quests={};tasks=[]
        qroot=ROOT/'config/ftbquests/quests'
        for path in qroot.rglob('*.snbt'):
            nbtlib.parse_nbt(path.read_text())
        for path in (qroot/'chapters').glob('*.snbt'):
            chapter=json.loads(path.read_text())
            for entry in [chapter]+chapter['quests']+[t for q in chapter['quests'] for t in q['tasks']]:
                self.assertRegex(entry['id'],r'^[0-9A-F]{16}$')
                self.assertNotIn(entry['id'],ids)
                ids.add(entry['id'])
            for quest in chapter['quests']:
                quests[quest['id']]=quest;tasks.extend(quest['tasks'])
        for task in tasks:
            self.assertEqual(task['type'],'advancement')
            self.assertIn(task['advancement'],ADV)
        def visit(q,parents):
            self.assertNotIn(q,parents,'Cyclic quest dependency')
            for dep in quests[q].get('dependencies',[]):
                self.assertIn(dep,quests);visit(dep,parents|{q})
        for q in quests:visit(q,set())
        self.assertEqual(len(quests),70)

    def test_native_spell_gates_match_the_optional_core_exactly(self):
        source=(ROOT/'OPTIONAL_FantasiaCore_source/src/main/java/kr/fantasia/core/FantasiaCore.java').read_text()
        native=(ROOT/'kubejs/server_scripts/fantasia_magic_runtime.js').read_text()
        java_map=dict(re.findall(r'Map.entry\("([^"]+)", new ResearchGate\("([^"]+)"',source))
        js_map=dict(re.findall(r'"(irons_spellbooks:[a-z_]+)": "([a-z0-9_]+)"',native))
        self.assertEqual(js_map,java_map)
        self.assertEqual(len(js_map),111)
        for gate in js_map.values():self.assertIn('fantasia_research:'+gate,ADV)

    def test_recipe_unlock_advancements_are_not_filtered(self):
        pack=json.loads((PACKS/'fantasia_all_spells/pack.mcmeta').read_text())
        for rule in pack.get('filter',{}).get('block',[]):
            self.assertIsNone(re.search(rule['path'],'advancement/recipes/building_blocks/oak_planks.json'))

if __name__=='__main__':unittest.main(verbosity=2)
