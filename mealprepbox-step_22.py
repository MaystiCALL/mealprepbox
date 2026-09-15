# === Stage 22: Add favorite records and quick favorite listing ===
# Project: MealPrepBox
class Favorite:
    """A single favorite recipe entry."""
    def __init__(self, name: str, meal_type: str, prep_time: int, is_vegan: bool = False):
        self.name = name
        self.meal_type = meal_type
        self.prep_time = prep_time
        self.is_vegan = is_vegan

    def summary(self) -> str:
        flag = " [V]" if self.is_vegan else ""
        return f"{self.name} ({self.meal_type}, {self.prep_time} min){flag}"

    def __repr__(self):
        return self.summary()


class FavoriteBook:
    """In-memory collection of favorite recipes."""
    def __init__(self):
        self._favorites: list[Favorite] = []

    def add(self, name: str, meal_type: str, prep_time: int, is_vegan: bool = False) -> Favorite:
        fav = Favorite(name, meal_type, prep_time, is_vegan)
        self._favorites.append(fav)
        return fav

    def list_all(self) -> list[str]:
        return [f.summary() for f in self._favorites]

    def __len__(self):
        return len(self._favorites)
