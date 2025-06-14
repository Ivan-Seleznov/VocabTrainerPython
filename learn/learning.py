from datetime import datetime
from PySide6.QtWidgets import QDialog
from ui.ui_learningview import Ui_LearningDialog
from card.cards import CardManager
from settings.settings_manager import SettingsManager

class LearningDialog(QDialog):
    def __init__(self, manager: CardManager, cards_per_day: int):
        super().__init__()
        self.ui = Ui_LearningDialog()
        self.ui.setupUi(self)
        self.manager = manager
        self.settings = SettingsManager()

        due = self.manager.get_due_cards()

        max_cards = cards_per_day or self.settings.get_cards_per_day()
        self.queue = due[:max_cards]
        self.current = None

        self.ui.btnToggle.clicked.connect(self.toggle_translation)
        self.ui.btnRemember.clicked.connect(self.on_remember)
        self.ui.btnRepeat.clicked.connect(self.on_repeat)

        self.next_card()

    def next_card(self):
        if not self.queue:
            self.current = None
            self.ui.labelOriginal.setText("No cards to study")
            self.ui.labelTranslation.setVisible(False)
            self.ui.btnToggle.setEnabled(False)
            self.ui.btnRemember.setEnabled(False)
            self.ui.btnRepeat.setEnabled(False)
            return

        self.current = self.queue.pop(0)
        self.ui.labelOriginal.setText(self.current.original)
        self.ui.labelTranslation.setText(self.current.translation)
        self.ui.labelTranslation.setVisible(False)
        self.ui.btnToggle.setEnabled(True)
        self.ui.btnRemember.setEnabled(True)
        self.ui.btnRepeat.setEnabled(True)

    def toggle_translation(self):
        if not self.current:
            return
        self.ui.labelTranslation.setVisible(not self.ui.labelTranslation.isVisible())

    def on_remember(self):
        if not self.current:
            return

        self.manager.remember_card(self.current, threshold=self.settings.get_learn_threshold())
        self.next_card()

    def on_repeat(self):
        if not self.current:
            return

        self.manager.repeat_card(self.current)
        self.queue.append(self.current)
        self.next_card()
