# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'learningview.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_LearningDialog(object):
    def setupUi(self, LearningDialog):
        if not LearningDialog.objectName():
            LearningDialog.setObjectName(u"LearningDialog")
        LearningDialog.resize(400, 250)
        self.verticalLayout = QVBoxLayout(LearningDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelOriginal = QLabel(LearningDialog)
        self.labelOriginal.setObjectName(u"labelOriginal")
        self.labelOriginal.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelOriginal)

        self.labelTranslation = QLabel(LearningDialog)
        self.labelTranslation.setObjectName(u"labelTranslation")
        self.labelTranslation.setAlignment(Qt.AlignCenter)
        self.labelTranslation.setVisible(False)

        self.verticalLayout.addWidget(self.labelTranslation)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnToggle = QPushButton(LearningDialog)
        self.btnToggle.setObjectName(u"btnToggle")

        self.buttonLayout.addWidget(self.btnToggle)

        self.btnRemember = QPushButton(LearningDialog)
        self.btnRemember.setObjectName(u"btnRemember")

        self.buttonLayout.addWidget(self.btnRemember)

        self.btnRepeat = QPushButton(LearningDialog)
        self.btnRepeat.setObjectName(u"btnRepeat")

        self.buttonLayout.addWidget(self.btnRepeat)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(LearningDialog)

        QMetaObject.connectSlotsByName(LearningDialog)
    # setupUi

    def retranslateUi(self, LearningDialog):
        LearningDialog.setWindowTitle(QCoreApplication.translate("LearningDialog", u"Learning Session", None))
        self.labelOriginal.setText(QCoreApplication.translate("LearningDialog", u"Original Word", None))
        self.labelOriginal.setStyleSheet(QCoreApplication.translate("LearningDialog", u"font-size:20pt;", None))
        self.labelTranslation.setText(QCoreApplication.translate("LearningDialog", u"Translation", None))
        self.labelTranslation.setStyleSheet(QCoreApplication.translate("LearningDialog", u"font-size:18pt; color: gray;", None))
        self.btnToggle.setText(QCoreApplication.translate("LearningDialog", u"Show/Hide", None))
        self.btnRemember.setText(QCoreApplication.translate("LearningDialog", u"Remember", None))
        self.btnRepeat.setText(QCoreApplication.translate("LearningDialog", u"Repeat", None))
    # retranslateUi

