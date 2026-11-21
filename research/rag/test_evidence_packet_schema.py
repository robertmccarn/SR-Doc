"""Contract tests for evidence-packet resolution status values."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent
SCHEMA_PATH = ROOT / "evidence-packet.schema.json"


class EvidencePacketSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        cls.allowed = set(
            cls.schema["properties"]["resolved_entities"]["items"]["properties"]["resolution_status"]["enum"]
        )

    def test_all_search_cli_resolution_statuses_are_allowed(self):
        emitted = {
            "exact",                 # exact page-ID lookup
            "exact_title",           # exact title-key lookup
            "redirect_target",       # resolved captured redirect
            "ambiguous_exact_title", # multiple exact title-key matches
        }
        self.assertTrue(emitted.issubset(self.allowed), emitted - self.allowed)

    def test_schema_keeps_unresolved_and_alias_states(self):
        self.assertIn("unresolved", self.allowed)
        self.assertIn("alias", self.allowed)
        self.assertIn("ambiguous", self.allowed)

    def test_schema_is_draft_2020_12(self):
        self.assertEqual(
            self.schema["$schema"],
            "https://json-schema.org/draft/2020-12/schema",
        )


if __name__ == "__main__":
    unittest.main()
