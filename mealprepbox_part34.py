# === Stage 34: Add support for multiple local user profiles ===
# Project: MealPrepBox
import json, os

class UserProfile:
    def __init__(self, name, preferences=None):
        self.name = name
        self.preferences = preferences or {}

    def to_dict(self):
        return {"name": self.name, "preferences": self.preferences}

    @classmethod
    def from_dict(cls, d):
        return cls(d["name"], d.get("preferences", {}))

class MultiProfileManager:
    def __init__(self, profiles_dir="profiles"):
        self.profiles_dir = profiles_dir
        self.profiles = []
        self._load_profiles()

    def _load_profiles(self):
        if os.path.isdir(self.profiles_dir):
            for f in os.listdir(self.profiles_dir):
                if f.endswith(".json"):
                    path = os.path.join(self.profiles_dir, f)
                    with open(path, "r") as fh:
                        self.profiles.append(UserProfile.from_dict(json.load(fh)))

    def add_profile(self, name, preferences=None):
        profile = UserProfile(name, preferences)
        self.profiles.append(profile)
        path = os.path.join(self.profiles_dir, f"{name}.json")
        with open(path, "w") as fh:
            json.dump(profile.to_dict(), fh, indent=2)

    def get_profile(self, name):
        for p in self.profiles:
            if p.name == name:
                return p
        return None

    def delete_profile(self, name):
        self.profiles = [p for p in self.profiles if p.name != name]
        path = os.path.join(self.profiles_dir, f"{name}.json")
        if os.path.exists(path):
            os.remove(path)
