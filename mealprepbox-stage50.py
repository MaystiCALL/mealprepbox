# === Stage 50: Add unit tests for import and export behavior ===
# Project: MealPrepBox
import json
import os
import unittest

import mealprepbox as mpx


class TestMealPrepBox(unittest.TestCase):
    def setUp(self):
        self.box = mpx.Box("Sample Week")

    def test_import_json_roundtrip(self):
        self.box.add_batch("Chicken Bowls", 4)
        payload = self.box.export()
        restored = mpx.Box.import_from(payload)
        self.assertEqual(restored.name, self.box.name)
        self.assertEqual(len(restored.batches), 1)
        self.assertEqual(restored.batches[0].name, "Chicken Bowls")

    def test_export_empty(self):
        payload = self.box.export()
        restored = mpx.Box.import_from(payload)
        self.assertEqual(restored.name, "Sample Week")
        self.assertEqual(len(restored.batches), 0)

    def test_freezer_roundtrip(self):
        self.box.add_freezer_item("Frozen Soup", 3)
        payload = self.box.export()
        restored = mpx.Box.import_from(payload)
        self.assertEqual(len(restored.freezer), 1)
        self.assertEqual(restored.freezer[0].name, "Frozen Soup")
        self.assertEqual(restored.freezer[0].quantity, 3)

    def test_reheat_notes_roundtrip(self):
        self.box.add_reheat_note("Chicken Bowls", "Microwave 3 min")
        payload = self.box.export()
        restored = mpx.Box.import_from(payload)
        self.assertEqual(len(restored.reheat_notes), 1)
        self.assertEqual(restored.reheat_notes[0].batch, "Chicken Bowls")
        self.assertEqual(restored.reheat_notes[0].note, "Microwave 3 min")

    def test_to_json_file_roundtrip(self):
        path = "test_export.json"
        try:
            self.box.add_batch("Tacos", 5)
            self.box.export_to_json(path)
            with open(path) as fh:
                data = json.load(fh)
            restored = mpx.Box.import_from_json(path)
            self.assertEqual(len(restored.batches), 1)
            self.assertEqual(restored.batches[0].name, "Tacos")
        finally:
            if os.path.exists(path):
                os.remove(path)


if __name__ == "__main__":
    unittest.main()
