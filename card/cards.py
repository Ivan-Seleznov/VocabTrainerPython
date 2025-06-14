import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List

DATA_FILE = Path("cards.json")

class Card:
    def __init__(
        self,
        original: str,
        translation: str,
        next_review: str = None,
        interval_days: int = 1,
        repetitions: int = 0,
        is_learned: bool = False
    ):
        self.original = original
        self.translation = translation
        self.interval_days = interval_days
        self.repetitions = repetitions
        self.is_learned = is_learned
        # наступне відображення: зараз, якщо перше створення
        self.next_review = next_review or datetime.now().isoformat()

    def to_dict(self):
        return {
            "original": self.original,
            "translation": self.translation,
            "interval_days": self.interval_days,
            "next_review": self.next_review,
            "repetitions": self.repetitions,
            "is_learned": self.is_learned,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            original=data["original"],
            translation=data["translation"],
            interval_days=data.get("interval_days", 1),
            next_review=data.get("next_review"),
            repetitions=data.get("repetitions", 0),
            is_learned=data.get("is_learned", False),
        )

class CardManager:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.cards: List[Card] = []
        self.load_cards()

    def load_cards(self) -> None:
        if self.data_file.exists():
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.cards = [Card.from_dict(d) for d in data]
        else:
            self.cards = []

    def save_cards(self) -> None:
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self.cards], f, ensure_ascii=False, indent=2)

    def add_card(self, original: str, translation: str) -> None:
        new_card = Card(original=original, translation=translation)
        self.cards.append(new_card)
        self.save_cards()

    def import_from_file(self, import_path: str) -> None:
        with open(import_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        imported = [Card.from_dict(d) for d in data]
        self.cards.extend(imported)
        self.save_cards()

    def get_due_cards(self) -> List[Card]:
        now_iso = datetime.now().isoformat()
        due = []
        for c in self.cards:
            if c.is_learned:
                continue
            if c.repetitions == 0 or c.next_review <= now_iso:
                due.append(c)
        return sorted(due, key=lambda c: c.next_review)

    def repeat_card(self, card: Card) -> None:
        card.next_review = datetime.now().isoformat()
        self.save_cards()

    def remember_card(self, card: Card, threshold: int = 5) -> None:
        card.repetitions += 1
        card.interval_days *= 2
        next_dt = datetime.fromisoformat(card.next_review) + timedelta(days=card.interval_days)
        card.next_review = next_dt.isoformat()
        if card.repetitions >= threshold:
            card.is_learned = True
        self.save_cards()

    def get_all_cards(self) -> List[Card]:
        return self.cards
