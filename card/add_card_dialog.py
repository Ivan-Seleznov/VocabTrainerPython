from PySide6.QtWidgets import QDialog
from ui.ui_addcardview import Ui_AddCardDialog
from card.cards import Card

class AddCardDialog(QDialog):
    def __init__(self, manager):
        super().__init__()
        self.ui = Ui_AddCardDialog()
        self.ui.setupUi(self)
        self.manager = manager
        self.ui.btnAdd.clicked.connect(self.on_add)
        self.ui.btnCancel.clicked.connect(self.reject)

    def on_add(self):
        orig = self.ui.editOriginal.text().strip()
        trans = self.ui.editTranslation.text().strip()
        if orig and trans:
            card = Card(original=orig, translation=trans)
            self.manager.cards.append(card)
            self.manager.save_cards()
            self.accept()
