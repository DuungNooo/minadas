"""Cross-file contracts only; this does not replace a real NeoForge build."""
from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / "OPTIONAL_FantasiaCore_source/src/main/java/kr/fantasia/core/FantasiaCore.java").read_text()
MAPPING = re.findall(r'Map.entry\("([^"]+)", new ResearchGate\("([^"]+)"', SOURCE)
ADVANCEMENTS = ROOT / "world/datapacks/fantasia_all_spells/data/fantasia_research/advancement"


class CoreContractTests(unittest.TestCase):
    def test_all_original_spells_have_unique_gate(self):
        self.assertEqual(len(MAPPING), 111)
        self.assertEqual(len({spell for spell, _ in MAPPING}), 111)

    def test_every_gate_resolves_to_an_actual_research_advancement(self):
        gates = {gate for _, gate in MAPPING}
        self.assertEqual(len(gates), 27)
        for gate in gates:
            with self.subTest(gate=gate):
                data = json.loads((ADVANCEMENTS / (gate + ".json")).read_text())
                self.assertIn("criteria", data)

    def test_no_duplicate_command_or_ephemeral_profile_system(self):
        for removed in ("RegisterCommandsEvent", "PLAYER_DATA", "PlayerProfile", "Commands.literal"):
            self.assertNotIn(removed, SOURCE)

    def test_direct_block_breaking_gate_exists(self):
        data = json.loads((ADVANCEMENTS / "map_breaking_magic.json").read_text())
        self.assertIn("criteria", data)
        self.assertIn('"irons_spellbooks:spectral_hammer"', SOURCE)
        self.assertIn('"irons_spellbooks:touch_dig"', SOURCE)


if __name__ == "__main__":
    unittest.main()
