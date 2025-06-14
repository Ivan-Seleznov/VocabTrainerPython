# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cardsview.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_CardsDialog(object):
    def setupUi(self, CardsDialog):
        if not CardsDialog.objectName():
            CardsDialog.setObjectName(u"CardsDialog")
        CardsDialog.resize(600, 400)
        self.verticalLayout = QVBoxLayout(CardsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableCards = QTableWidget(CardsDialog)
        self.tableCards.setObjectName(u"tableCards")
        self.tableCards.setColumnCount(5)
        self.tableCards.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableCards.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout.addWidget(self.tableCards)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.btnClose = QPushButton(CardsDialog)
        self.btnClose.setObjectName(u"btnClose")

        self.buttonLayout.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(CardsDialog)

        QMetaObject.connectSlotsByName(CardsDialog)
    # setupUi

    def retranslateUi(self, CardsDialog):
        CardsDialog.setWindowTitle(QCoreApplication.translate("CardsDialog", u"All Cards", None))
        self.tableCards.setHorizontalHeaderLabels([
            QCoreApplication.translate("CardsDialog", u"Original", None),
            QCoreApplication.translate("CardsDialog", u"Translation", None),
            QCoreApplication.translate("CardsDialog", u"Repetitions", None),
            QCoreApplication.translate("CardsDialog", u"Next Review", None),
            QCoreApplication.translate("CardsDialog", u"Learned", None)])
        self.btnClose.setText(QCoreApplication.translate("CardsDialog", u"Close", None))
    # retranslateUi

