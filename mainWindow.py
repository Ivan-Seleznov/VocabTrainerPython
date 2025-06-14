from PySide6.QtWidgets import QMainWindow

from card.add_card_dialog import AddCardDialog
from settings.settings_dialog import SettingsDialog
from settings.settings_manager import SettingsManager
from ui.ui_mainwindow import Ui_MainWindow
from card.cards_dialog import CardsDialog
from card.cards import CardManager
from learn.learning import LearningDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.manager = CardManager()
        self.settings = SettingsManager()

        self.update_statistics()

        self.ui.btnViewCards.clicked.connect(self.show_all_cards)
        self.ui.btnStartLearning.clicked.connect(self.start_learning)
        self.ui.btnImport.clicked.connect(self.import_cards)
        self.ui.btnAddCard.clicked.connect(self.show_add_dialog)
        self.ui.btnSettings.clicked.connect(self.open_settings)

    def update_statistics(self):
        all_cards = self.manager.get_all_cards()
        total = len(all_cards)
        learned = sum(1 for c in all_cards if c.is_learned)
        self.ui.labelTotalCards.setText(f"Total cards: {total}")
        self.ui.labelLearnedCards.setText(f"Learned: {learned}")

    def show_all_cards(self):
        dlg = CardsDialog(self.manager)
        dlg.finished.connect(self.update_statistics)
        dlg.exec()

    def start_learning(self):
        dlg = LearningDialog(self.manager, self.settings.get_cards_per_day())
        dlg.finished.connect(self.update_statistics)
        dlg.exec()

    def import_cards(self):
        from PySide6.QtWidgets import QFileDialog
        path, _ = QFileDialog.getOpenFileName(self, "Import JSON", "", "JSON Files (*.json)")
        if path:
            self.manager.import_from_file(path)
            self.update_statistics()
            self.statusBar().showMessage("Cards imported", 2000)

    def show_add_dialog(self):
        dlg = AddCardDialog(self.manager)
        if dlg.exec():
            self.update_statistics()
            self.statusBar().showMessage("Card added", 2000)

    def open_settings(self):
        dlg = SettingsDialog(self.settings)
        if dlg.exec():
            self.update_statistics()
            self.statusBar().showMessage("Settings saved", 2000)