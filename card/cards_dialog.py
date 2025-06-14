from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QTableWidgetItem
from card.cards import CardManager
from ui.ui_cardsview import Ui_CardsDialog

class CardsDialog(QDialog):
    def __init__(self, manager: CardManager):
        super().__init__()
        self.ui = Ui_CardsDialog()
        self.ui.setupUi(self)
        self.manager = manager

        self.ui.tableCards.itemChanged.connect(self.on_item_changed)

        self.populate_table()
        self.ui.btnClose.clicked.connect(self.close)

    def populate_table(self):
        cards = self.manager.get_all_cards()
        tbl = self.ui.tableCards

        tbl.blockSignals(True)

        tbl.setRowCount(len(cards))
        for row, card in enumerate(cards):
            tbl.setItem(row, 0, QTableWidgetItem(card.original))
            tbl.setItem(row, 1, QTableWidgetItem(card.translation))
            tbl.setItem(row, 2, QTableWidgetItem(str(card.repetitions)))
            tbl.setItem(row, 3, QTableWidgetItem(card.next_review))

            chk = QTableWidgetItem()
            chk.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            chk.setCheckState(Qt.Checked if card.is_learned else Qt.Unchecked)
            tbl.setItem(row, 4, chk)

        tbl.blockSignals(False)

    def on_item_changed(self, item: QTableWidgetItem):
        if item.column() == 4:
            row = item.row()
            card = self.manager.get_all_cards()[row]
            card.is_learned = (item.checkState() == Qt.Checked)
            self.manager.save_cards()
