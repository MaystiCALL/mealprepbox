# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: MealPrepBox
def update_recipe(recipe_id: str, **kwargs) -> dict:
    """Update fields of an existing recipe; returns the merged record."""
    db.setdefault("recipes", {})[recipe_id].update(kwargs)
    return db["recipes"][recipe_id]

def update_batch(batch_id: str, **kwargs) -> dict:
    """Update fields of an existing batch; returns the merged record."""
    db.setdefault("batches", {})[batch_id].update(kwargs)
    return db["batches"][batch_id]

def update_container(container_id: str, **kwargs) -> dict:
    """Update fields of an existing container; returns the merged record."""
    db.setdefault("containers", {})[container_id].update(kwargs)
    return db["containers"][container_id]

def update_freezer_item(item_id: str, **kwargs) -> dict:
    """Update fields of an existing freezer item; returns the merged record."""
    db.setdefault("freezer", {})[item_id].update(kwargs)
    return db["freezer"][item_id]

def update_reheat_note(note_id: str, **kwargs) -> dict:
    """Update fields of an existing reheating note; returns the merged record."""
    db.setdefault("reheat_notes", {})[note_id].update(kwargs)
    return db["reheat_notes"][note_id]
