# === Stage 57: Add structured result objects for command handlers ===
# Project: MealPrepBox
class BatchResult:
    def __init__(self, message, batch_id=None):
        self.message = message
        self.batch_id = batch_id

    def to_dict(self):
        return {"message": self.message, "batch_id": self.batch_id}

    def __repr__(self):
        return f"BatchResult(message={self.message!r}, batch_id={self.batch_id!r})"


class ContainerResult:
    def __init__(self, message, container_id=None):
        self.message = message
        self.container_id = container_id

    def to_dict(self):
        return {"message": self.message, "container_id": self.container_id}

    def __repr__(self):
        return f"ContainerResult(message={self.message!r}, container_id={self.container_id!r})"


class FreezerResult:
    def __init__(self, message, items=None):
        self.message = message
        self.items = items

    def to_dict(self):
        return {"message": self.message, "items": self.items}

    def __repr__(self):
        return f"FreezerResult(message={self.message!r}, items={self.items!r})"


class ReheatResult:
    def __init__(self, message, food=None, temperature=None, time_minutes=None):
        self.message = message
        self.food = food
        self.temperature = temperature
        self.time_minutes = time_minutes

    def to_dict(self):
        return {
            "message": self.message,
            "food": self.food,
            "temperature": self.temperature,
            "time_minutes": self.time_minutes,
        }

    def __repr__(self):
        return (
            f"ReheatResult(message={self.message!r}, food={self.food!r}, "
            f"temperature={self.temperature!r}, time_minutes={self.time_minutes!r})"
        )
