# === Stage 58: Add bulk update behavior for selected records ===
# Project: MealPrepBox
def bulk_update(self, field, values):
    """Apply a single bulk update across every stored record."""
    for record in self.records:
        setattr(record, field, values)
    return len(self.records)


def bulk_set_freezer(self, status):
    """Mark selected freezer records with a new status in place."""
    return self.bulk_update("frozen", status)


def bulk_add_reheat_note(self, note, minutes=5):
    """Append a reheating instruction to every record that has one."""
    for record in self.records:
        if getattr(record, "reheat_note", None):
            record.reheat_note = record.reheat_note + "; " + note + " (" + str(minutes) + " min)"
    return len(self.records)
