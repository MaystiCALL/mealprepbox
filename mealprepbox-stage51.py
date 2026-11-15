# === Stage 51: Add unit tests for search and filter behavior ===
# Project: MealPrepBox
def test_search_by_name():
    assert search("chicken") == ["Chicken Curry Bowl", "Chicken Salad"]
    assert search("veggie") == ["Veggie Stir Fry"]
    assert search("beef") == []


def test_search_case_insensitive():
    assert search("CHICKEN") == ["Chicken Curry Bowl", "Chicken Salad"]


def test_search_partial_match():
    assert "Chicken Curry Bowl" in search("curry")


def test_filter_by_category():
    assert filter_by_category("Dairy") == ["Greek Yogurt Parfait"]


def test_filter_by_tags():
    assert filter_by_tags("high_protein") == ["Chicken Curry Bowl", "Greek Yogurt Parfait"]


def test_filter_empty_results():
    assert filter_by_category("Beverage") == []
    assert filter_by_tags("vegetarian") == []


def test_search_no_duplicates():
    assert len(search("chicken")) == 2
