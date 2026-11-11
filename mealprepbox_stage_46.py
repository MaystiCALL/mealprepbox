# === Stage 46: Add a schema version field and migration helper ===
# Project: MealPrepBox
SCHEMA_VERSION = 2


def migrate_schema(db):
    """Bump schema version and ensure migration markers exist."""
    if "schema_version" not in db:
        db["schema_version"] = SCHEMA_VERSION
    else:
        db["schema_version"] = max(db["schema_version"], SCHEMA_VERSION)
    if "migrations" not in db:
        db["migrations"] = []
    if SCHEMA_VERSION not in db["migrations"]:
        db["migrations"].append(SCHEMA_VERSION)
