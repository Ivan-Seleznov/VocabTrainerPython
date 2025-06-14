import json
from pathlib import Path

SETTINGS_FILE = Path("settings.json")

class SettingsManager:
    def __init__(self, file=SETTINGS_FILE):
        self.file = file
        self.data = {
            "cards_per_day": 10,
            "learn_threshold": 5
        }
        self.load()

    def load(self):
        if self.file.exists():
            with open(self.file, "r", encoding="utf-8") as f:
                self.data.update(json.load(f))

    def save(self):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def get_cards_per_day(self) -> int:
        return self.data.get("cards_per_day", 10)

    def set_cards_per_day(self, n: int):
        self.data["cards_per_day"] = n
        self.save()

    def get_learn_threshold(self) -> int:
        return self.data.get("learn_threshold", 5)

    def set_learn_threshold(self, t: int):
        self.data["learn_threshold"] = t
        self.save()
