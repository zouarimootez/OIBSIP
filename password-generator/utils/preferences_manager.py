import json
import os

class PreferencesManager:
    def __init__(self):
        self.preferences_file = "preferences.json"

    def load_preferences(self):
        """Load user preferences from a file."""
        if os.path.exists(self.preferences_file):
            with open(self.preferences_file, "r") as file:
                return json.load(file)
        return {}

    def save_preferences(self, preferences):
        """Save user preferences to a file."""
        with open(self.preferences_file, "w") as file:
            json.dump(preferences, file)