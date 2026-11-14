# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: MealPrepBox
def test_update_missing_id_returns_none():
    box = MealPrepBox()
    assert box.update_recipe("nope", "new name") is None


def test_update_recipe_missing_field():
    box = MealPrepBox()
    box.add_recipe("Oats", servings=4, reheating="microwave 90s")
    assert box.update_recipe("Oats", servings=0) is None


def test_update_recipe_invalid_servings():
    box = MealPrepBox()
    box.add_recipe("Oats", servings=4, reheating="microwave 90s")
    assert box.update_recipe("Oats", servings=-1) is None


def test_delete_missing_recipe_returns_none():
    box = MealPrepBox()
    assert box.delete_recipe("ghost") is None


def test_delete_existing_recipe_removes_it():
    box = MealPrepBox()
    box.add_recipe("Oats", servings=4, reheating="microwave 90s")
    assert box.delete_recipe("Oats") is True
    assert "Oats" not in box.recipes


def test_delete_nonexistent_batch_returns_none():
    box = MealPrepBox()
    assert box.delete_batch("BATCH_999") is None


def test_delete_existing_batch_returns_true():
    box = MealPrepBox()
    box.add_recipe("Oats", servings=4, reheating="microwave 90s")
    batch_id = box.create_batch("Oats")
    assert box.delete_batch(batch_id) is True
    assert batch_id not in box.batches
