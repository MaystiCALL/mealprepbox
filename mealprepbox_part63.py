# === Stage 63: Add relationships between records where useful ===
# Project: MealPrepBox
class Meal:
    def __init__(self, name):
        self.name = name
        self.batches = []
        self.reheat_instructions = ""

    def add_batch(self, batch):
        self.batches.append(batch)

    def get_total_portions(self):
        return sum(batch.portions for batch in self.batches)

    def get_total_freezer_days(self):
        return sum(batch.freezer_days for batch in self.batches)


class Batch:
    def __init__(self, meal, portions, freezer_days, container_ids=None):
        self.meal = meal
        self.portions = portions
        self.freezer_days = freezer_days
        self.containers = container_ids or []

    def add_container(self, container):
        if container not in self.containers:
            self.containers.append(container)


class Container:
    def __init__(self, size_ml, batch=None, is_frozen=False):
        self.size_ml = size_ml
        self.batch = batch
        self.is_frozen = is_frozen

    def set_batch(self, batch):
        self.batch = batch


class FreezerInventory:
    def __init__(self):
        self.items = []

    def add(self, batch):
        self.items.append(batch)

    def total_freezer_portions(self):
        return sum(batch.portions for batch in self.items if batch.freezer_days > 0)

    def items_expiring_soon(self, days):
        return [item for item in self.items if item.freezer_days <= days]

    def clear_expired(self, days):
        self.items = [item for item in self.items if item.freezer_days > days]


def build_sample_data():
    chicken = Meal("Grilled Chicken")
    rice = Meal("Cooked Rice")

    chicken_batch = Batch(chicken, portions=6, freezer_days=4)
    rice_batch = Batch(rice, portions=6, freezer_days=5)
    chicken_batch.add_container(Container(500))
    rice_batch.add_container(Container(300))

    chicken.add_batch(chicken_batch)
    rice.add_batch(rice_batch)

    freezer = FreezerInventory()
    freezer.add(chicken_batch)
    freezer.add(rice_batch)

    return chicken, rice, freezer
