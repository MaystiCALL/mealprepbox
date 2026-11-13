# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: MealPrepBox
def test_create_batch():
    batch = create_batch("Chicken", 4)
    assert batch.name == "Chicken"
    assert batch.count == 4

def test_create_container():
    container = create_container("Bento")
    assert container.name == "Bento"

def test_create_freezer_item():
    item = create_freezer_item("Chicken", 3)
    assert item.name == "Chicken"
    assert item.count == 3

def test_add_reheat_note():
    note = add_reheat_note("Chicken", "Microwave 3 minutes")
    assert note.meal == "Chicken"
    assert note.instructions == "Microwave 3 minutes"

def test_validate_batch_name():
    assert validate_batch_name("Chicken") is True
    assert validate_batch_name("") is False

def test_validate_container_name():
    assert validate_container_name("Bento") is True
    assert validate_container_name("  ") is False

def test_validate_freezer_count():
    assert validate_freezer_count(3) is True
    assert validate_freezer_count(-1) is False
    assert validate_freezer_count(0) is False

def test_validate_reheat_instructions():
    assert validate_reheat_instructions("Microwave 3 minutes") is True
    assert validate_reheat_instructions("") is False
