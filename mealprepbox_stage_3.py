# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: MealPrepBox
def _validate_identifier(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")
    return value.strip()

def _validate_positive_int(value, name):
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value

def _validate_short_text(value, name, max_len=50):
    if not isinstance(value, str) or len(value.strip()) == 0:
        raise ValueError(f"{name} must be a non-empty short text")
    if len(value.strip()) > max_len:
        raise ValueError(f"{name} exceeds max length of {max_len}")
    return value.strip()

def validate_batch(batch):
    if not isinstance(batch, dict):
        raise TypeError("batch must be a dict")
    required = {"id", "name", "prep_date", "quantity", "ingredients", "reheat_notes"}
    missing = required - set(batch.keys())
    if missing:
        raise ValueError(f"batch is missing required fields: {missing}")
    _validate_identifier(batch["id"], "batch.id")
    _validate_short_text(batch["name"], "batch.name", max_len=80)
    _validate_positive_int(batch["quantity"], "batch.quantity")
    _validate_short_text(batch["prep_date"], "batch.prep_date")
    if not isinstance(batch["ingredients"], list) or len(batch["ingredients"]) == 0:
        raise ValueError("batch.ingredients must be a non-empty list")
    if not isinstance(batch["reheat_notes"], str):
        raise ValueError("batch.reheat_notes must be a string")
    return batch
