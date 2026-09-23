# === Stage 35: Add active user switching and user-specific records ===
# Project: MealPrepBox
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.records = []

    def add_record(self, record):
        self.records.append(record)
        return record
