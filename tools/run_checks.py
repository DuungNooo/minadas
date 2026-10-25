#!/usr/bin/env python3
"""Run the bounded verification suite and preserve each command's exit status."""
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
COMMANDS=[
 [sys.executable,'tools/build_map.py'],
 [sys.executable,'tools/build_campaign.py'],
 [sys.executable,'tests/validate_commands.py'],
 [sys.executable,'tests/campaign_runtime_test.py'],
 [sys.executable,'tests/data_test.py'],
 [sys.executable,'tests/core_contract_test.py'],
 [sys.executable,'tests/installer_test.py'],
 ['node','--test','tests/runtime_test.js'],
 [sys.executable,'tools/build_world_template.py'],
]

if __name__=='__main__':
    for command in COMMANDS:
        print('\nRUN: '+' '.join(command),flush=True)
        subprocess.run(command,cwd=ROOT,check=True)
    print('\nAll automated checks passed. Live Minecraft/NeoForge execution was not performed.')
