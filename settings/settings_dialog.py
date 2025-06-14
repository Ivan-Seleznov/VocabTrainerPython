from PySide6.QtWidgets import QDialog
from ui.ui_settingsview import Ui_SettingsDialog
from settings.settings_manager import SettingsManager

class SettingsDialog(QDialog):
    def __init__(self, settings: SettingsManager):
        super().__init__()
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.settings = settings

        self.ui.spinBoxCardsPerDay.setValue(self.settings.get_cards_per_day())
        self.ui.spinBoxLearnThreshold.setValue(self.settings.get_learn_threshold())

        self.ui.buttonBox.accepted.connect(self.save_and_close)
        self.ui.buttonBox.rejected.connect(self.reject)

    def save_and_close(self):
        self.settings.set_cards_per_day(self.ui.spinBoxCardsPerDay.value())
        self.settings.set_learn_threshold(self.ui.spinBoxLearnThreshold.value())
        self.accept()
