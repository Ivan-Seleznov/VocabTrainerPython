# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsview.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        self.verticalLayout = QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelCardsPerDay = QLabel(SettingsDialog)
        self.labelCardsPerDay.setObjectName(u"labelCardsPerDay")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelCardsPerDay)

        self.spinBoxCardsPerDay = QSpinBox(SettingsDialog)
        self.spinBoxCardsPerDay.setObjectName(u"spinBoxCardsPerDay")
        self.spinBoxCardsPerDay.setMinimum(1)
        self.spinBoxCardsPerDay.setMaximum(100)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBoxCardsPerDay)

        self.labelLearnThreshold = QLabel(SettingsDialog)
        self.labelLearnThreshold.setObjectName(u"labelLearnThreshold")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelLearnThreshold)

        self.spinBoxLearnThreshold = QSpinBox(SettingsDialog)
        self.spinBoxLearnThreshold.setObjectName(u"spinBoxLearnThreshold")
        self.spinBoxLearnThreshold.setMinimum(1)
        self.spinBoxLearnThreshold.setMaximum(10)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBoxLearnThreshold)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(SettingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SettingsDialog)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.labelCardsPerDay.setText(QCoreApplication.translate("SettingsDialog", u"Cards per day:", None))
        self.labelLearnThreshold.setText(QCoreApplication.translate("SettingsDialog", u"Learn threshold:", None))
    # retranslateUi

