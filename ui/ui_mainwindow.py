# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitle = QLabel(self.centralwidget)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.labelTitle.setMargin(10)

        self.verticalLayout.addWidget(self.labelTitle)

        self.statsLayout = QHBoxLayout()
        self.statsLayout.setObjectName(u"statsLayout")
        self.labelTotalCards = QLabel(self.centralwidget)
        self.labelTotalCards.setObjectName(u"labelTotalCards")
        self.labelTotalCards.setAlignment(Qt.AlignLeft)

        self.statsLayout.addWidget(self.labelTotalCards)

        self.labelLearnedCards = QLabel(self.centralwidget)
        self.labelLearnedCards.setObjectName(u"labelLearnedCards")
        self.labelLearnedCards.setAlignment(Qt.AlignRight)

        self.statsLayout.addWidget(self.labelLearnedCards)


        self.verticalLayout.addLayout(self.statsLayout)

        self.btnViewCards = QPushButton(self.centralwidget)
        self.btnViewCards.setObjectName(u"btnViewCards")

        self.verticalLayout.addWidget(self.btnViewCards)

        self.btnStartLearning = QPushButton(self.centralwidget)
        self.btnStartLearning.setObjectName(u"btnStartLearning")

        self.verticalLayout.addWidget(self.btnStartLearning)

        self.btnImport = QPushButton(self.centralwidget)
        self.btnImport.setObjectName(u"btnImport")

        self.verticalLayout.addWidget(self.btnImport)

        self.btnAddCard = QPushButton(self.centralwidget)
        self.btnAddCard.setObjectName(u"btnAddCard")

        self.verticalLayout.addWidget(self.btnAddCard)

        self.btnSettings = QPushButton(self.centralwidget)
        self.btnSettings.setObjectName(u"btnSettings")

        self.verticalLayout.addWidget(self.btnSettings)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Vocabulary Trainer", None))
        MainWindow.setStyleSheet(QCoreApplication.translate("MainWindow", u"?QPushButton {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-weight: bold;\n"
"   }\n"
"   QPushButton:hover {\n"
"    background-color: #45a049;\n"
"   }\"?", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"Vocabulary Trainer", None))
        self.labelTitle.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-size: 18pt; font-weight: bold;", None))
        self.labelTotalCards.setText(QCoreApplication.translate("MainWindow", u"Total cards: 0", None))
        self.labelLearnedCards.setText(QCoreApplication.translate("MainWindow", u"Learned: 0", None))
        self.btnViewCards.setText(QCoreApplication.translate("MainWindow", u"View Cards", None))
        self.btnStartLearning.setText(QCoreApplication.translate("MainWindow", u"Start Learning", None))
        self.btnImport.setText(QCoreApplication.translate("MainWindow", u"Import Cards", None))
        self.btnAddCard.setText(QCoreApplication.translate("MainWindow", u"Add Card", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

