# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addcardview.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_AddCardDialog(object):
    def setupUi(self, AddCardDialog):
        if not AddCardDialog.objectName():
            AddCardDialog.setObjectName(u"AddCardDialog")
        AddCardDialog.resize(300, 180)
        self.verticalLayout = QVBoxLayout(AddCardDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelOriginal = QLabel(AddCardDialog)
        self.labelOriginal.setObjectName(u"labelOriginal")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelOriginal)

        self.editOriginal = QLineEdit(AddCardDialog)
        self.editOriginal.setObjectName(u"editOriginal")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editOriginal)

        self.labelTranslation = QLabel(AddCardDialog)
        self.labelTranslation.setObjectName(u"labelTranslation")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelTranslation)

        self.editTranslation = QLineEdit(AddCardDialog)
        self.editTranslation.setObjectName(u"editTranslation")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editTranslation)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.btnCancel = QPushButton(AddCardDialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.buttonLayout.addWidget(self.btnCancel)

        self.btnAdd = QPushButton(AddCardDialog)
        self.btnAdd.setObjectName(u"btnAdd")

        self.buttonLayout.addWidget(self.btnAdd)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(AddCardDialog)

        QMetaObject.connectSlotsByName(AddCardDialog)
    # setupUi

    def retranslateUi(self, AddCardDialog):
        AddCardDialog.setWindowTitle(QCoreApplication.translate("AddCardDialog", u"Add Card", None))
        self.labelOriginal.setText(QCoreApplication.translate("AddCardDialog", u"Original:", None))
        self.labelTranslation.setText(QCoreApplication.translate("AddCardDialog", u"Translation:", None))
        self.btnCancel.setText(QCoreApplication.translate("AddCardDialog", u"Cancel", None))
        self.btnAdd.setText(QCoreApplication.translate("AddCardDialog", u"Add", None))
    # retranslateUi

