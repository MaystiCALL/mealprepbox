# === Stage 18: Add an activity log with timestamps and action names ===
# Project: MealPrepBox
import datetime

class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action, details=""):
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "action": action,
            "details": details,
        }
        self.entries.append(entry)

    def get_log(self):
        return self.entries
