#!/usr/bin/env python3
"""Unit tests for source-aware infobox extraction and conservative comparison."""
import unittest

from extract_infobox_claims import iter_infoboxes, linked_entities
from evaluate_infobox_claims import evaluate_claims


class InfoboxParserTests(unittest.TestCase):
    def test_nested_templates_and_wikilink_pipes_do_not_split_parameters(self):
        source = "{{Infobox X|date=2020-2021|nested={{small|label=a=b|x=y}}|name=[[A|Alpha]]}}"
        parsed = list(iter_infoboxes(source))
        self.assertEqual(len(parsed), 1)
        _, _, name, params = parsed[0]
        self.assertEqual(name, "Infobox X")
        self.assertEqual([p["parameter_name"] for p in params], ["date", "nested", "name"])
        self.assertEqual(params[1]["raw_value"], "{{small|label=a=b|x=y}}")
        self.assertEqual(params[2]["raw_value"], "[[A|Alpha]]")

    def test_nested_parameter_syntax_and_comments(self):
        source = "{{Infobox X|value={{{fallback|{{small|x=y}}}}}|real=yes<!-- |fake=x -->}}"
        parsed = list(iter_infoboxes(source))
        self.assertEqual(len(parsed), 1)
        self.assertEqual([p["parameter_name"] for p in parsed[0][3]], ["value", "real"])

    def test_linked_entity_offsets_are_absolute(self):
        links = linked_entities("before [[Entity|label]] after", 100)
        self.assertEqual(links[0]["target"], "Entity")
        self.assertEqual(links[0]["display"], "label")
        self.assertEqual(links[0]["char_start"], 107)
        self.assertEqual(links[0]["char_end"], 123)

    def test_comparison_requires_same_subject_instance_and_field(self):
        base = {
            "page_id": "1", "title": "Subject", "template_instance_id": "T1",
            "normalized_parameter_name": "date", "parameter_name": "date",
            "template_name": "Infobox X", "provenance": {"locator": "chars 1-5"},
        }
        claims = [
            {**base, "claim_id": "a", "raw_parameter_value": "2020-2021"},
            {**base, "claim_id": "b", "raw_parameter_value": "2022-2023"},
            {**base, "claim_id": "c", "raw_parameter_value": " 2020-2021 "},
            {**base, "claim_id": "d", "page_id": "2", "raw_parameter_value": "1990-1991"},
            {**base, "claim_id": "e", "normalized_parameter_name": "combatant1", "raw_parameter_value": "2105-2111"},
        ]
        result = evaluate_claims(claims)
        self.assertEqual(result["candidate_count"], 1)
        self.assertEqual(result["candidate_conflicts"][0]["subject_page_id"], "1")
        self.assertEqual(result["candidate_conflicts"][0]["status"], "candidate_conflict_requires_source_review")


if __name__ == "__main__":
    unittest.main()
