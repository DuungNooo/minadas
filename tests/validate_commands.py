"""Parse every shipped vanilla command using the 1.21.1 command tree.

This is a static compatibility check, NOT a running Minecraft server.
Fixtures are extracted Minecraft data from misode/mcmeta tag 1.21.1-summary.
"""
from pathlib import Path
import json
import re
import sys

from mecha import Mecha, CommandSpec, CommandTree, AstBlock, AstCommand
from mecha.parse import get_parsers

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / 'tests/fixtures'


def validate():
    parser = Mecha(spec=CommandSpec(
        tree=CommandTree.load_from(FIXTURES / 'minecraft_1.21.1_commands.json',
                                   version='1.21', patch_only=True),
        parsers=get_parsers('1.21'),
    ))
    blocks = json.loads((FIXTURES / 'minecraft_1.21.1_blocks.json').read_text())
    registries = json.loads((FIXTURES / 'minecraft_1.21.1_registries.json').read_text())
    files = sorted((ROOT / 'world/datapacks').rglob('*.mcfunction'))
    functions = {}
    advancements = set()
    for path in files:
        parts = path.relative_to(ROOT / 'world/datapacks').parts
        functions[f'{parts[2]}:{"/".join(parts[4:])[:-11]}'] = path
    for path in (ROOT / 'world/datapacks').glob('*/data/*/advancement/**/*.json'):
        parts = path.relative_to(ROOT / 'world/datapacks').parts
        advancements.add(f'{parts[2]}:{"/".join(parts[4:])[:-5]}')
    failures = []
    count = 0
    for path in files:
        source = path.read_text(encoding='utf-8')
        try:
            tree = parser.parse(source)
        except Exception as exc:
            failures.append(f'{path.relative_to(ROOT)}: parse: {exc}')
            continue
        count += len(tree.commands)
        for node in tree.walk():
            if isinstance(node, AstBlock):
                block = node.identifier
                if block.namespace not in (None, 'minecraft') or block.is_tag:
                    continue
                if block.path not in blocks:
                    failures.append(f'{path.name}: unknown block {block.path}')
                    continue
                allowed = blocks[block.path][0]
                for state in node.block_states:
                    if state.key.value not in allowed or state.value.value not in allowed[state.key.value]:
                        failures.append(f'{path.name}: invalid {block.path}[{state.key.value}={state.value.value}]')
            if isinstance(node, AstCommand) and node.identifier.startswith('summon:'):
                entity = node.arguments[0]
                if entity.namespace in (None, 'minecraft') and entity.path not in registries['entity_type']:
                    failures.append(f'{path.name}: unknown entity {entity.path}')
            if isinstance(node, AstCommand) and node.identifier.startswith('fill:'):
                first, last = node.arguments[:2]
                a, b = [first.x, first.y, first.z], [last.x, last.y, last.z]
                if all(x.type == 'absolute' for x in a+b):
                    volume = 1
                    for x, y in zip(a, b): volume *= abs(x.value-y.value)+1
                    if volume > 32768:
                        failures.append(f'{path.name}: fill volume {volume} > default 32768')
        for line in source.splitlines():
            if line.lstrip().startswith('#'): continue
            for match in re.finditer(r'\bfunction (fantasia(?:_research)?:[a-z0-9_./-]+)', line):
                if match[1] not in functions:
                    failures.append(f'{path.name}: missing function {match[1]}')
            for match in re.finditer(r'\badvancement (?:grant|revoke) \S+ only (fantasia(?:_research)?:[a-z0-9_./-]+)', line):
                if match[1] not in advancements:
                    failures.append(f'{path.name}: missing advancement {match[1]}')
    for path in (ROOT / 'world/datapacks').glob('*/data/minecraft/tags/function/*.json'):
        for entry in json.loads(path.read_text())['values']:
            name = entry if isinstance(entry, str) else entry['id']
            if name not in functions:
                failures.append(f'{path.name}: missing tagged function {name}')
    for path in (ROOT / 'world/datapacks').rglob('*.json'):
        json.loads(path.read_text(encoding='utf-8'))
    print(f'Parsed {count} commands in {len(files)} functions against Minecraft 1.21.1 command tree.')
    print('Checked vanilla blocks/states/entities, fill bounds, function and advancement references.')
    if failures:
        for error in failures: print(error, file=sys.stderr)
        raise SystemExit(1)
    print('PASS (static command validation; live server execution is separate).')


if __name__ == '__main__':
    validate()
