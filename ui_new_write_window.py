# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newWriteWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateEdit, QDialog,
    QFrame, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(238, 251)
        Dialog.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 201, 211))
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.labelNew = QLabel(self.frame)
        self.labelNew.setObjectName(u"labelNew")
        self.labelNew.setGeometry(QRect(10, 0, 181, 141))
        self.labelNew.setStyleSheet(u"background-color: rgba(255, 255, 255,200);\n"
"font: 900 14pt \"Arial Black\";\n"
"border-radius:7px;\n"
"color: rgb(0, 0, 0);")
        self.labelNew.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(20, 90, 161, 41))
        self.dateEdit.setStyleSheet(u"background-color: rgb(199, 149, 210);\n"
"font: 16pt \"Swis721 BlkCn BT\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 7px;")
        self.dateEdit.setAlignment(Qt.AlignCenter)
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateEdit.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(14, 0, 0)))
        self.dateEdit.setDate(QDate(2023, 1, 1))
        self.saveButton = QPushButton(self.frame)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(20, 160, 161, 50))
        self.saveButton.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.205, y2:0.198864, stop:0 rgba(104, 74, 132, 255), stop:1 rgba(221, 164, 233, 255));\n"
"border-radius: 7px;\n"
"font: 800 16pt \"Arial Black\";\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(216, 179, 229);\n"
"border-radius: 7px;\n"
"font: 800 16pt \"Arial Black\";\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(104, 74, 132);\n"
"border-radius: 7px;\n"
"font: 800 16pt \"Arial Black\";\n"
"}")
        self.inputLineEdit = QLineEdit(self.frame)
        self.inputLineEdit.setObjectName(u"inputLineEdit")
        self.inputLineEdit.setGeometry(QRect(20, 30, 161, 51))
        self.inputLineEdit.setStyleSheet(u"font: 900 12pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;")
        self.inputLineEdit.setMaxLength(6)
        self.inputLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.labelNew.raise_()
        self.saveButton.raise_()
        self.inputLineEdit.raise_()
        self.dateEdit.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.labelNew.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.saveButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

