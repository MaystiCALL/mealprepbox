# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: MealPrepBox
import operator

SORT_KEYS = {
    "title": ("title", operator.attrgetter("title")),
    "date": ("date", operator.attrgetter("date")),
    "priority": ("priority", operator.attrgetter("priority")),
    "last_updated": ("last_updated", operator.attrgetter("last_updated")),
}

def sort_meals(meals, sort_by="date"):
    """Return a new sorted list of Meal objects by the given field.

    Args:
        meals: list of Meal instances (or dicts with the same keys).
        sort_by: one of 'title', 'date', 'priority', 'last_updated'.

    Returns:
        A new list sorted in ascending order by the chosen field.
    """
    key_func = operator.attrgetter(sort_by) if sort_by in SORT_KEYS else None

    def _sort_key(item):
        if isinstance(item, dict):
            return item.get(sort_by, "")
        return key_func(item) if key_func else item.get(sort_by, "")

    return sorted(meals, key=_sort_key)
