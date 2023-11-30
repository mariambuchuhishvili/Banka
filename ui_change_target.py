# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'changeTarget.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_Target(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(239, 200)
        Dialog.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.labelNew = QLabel(Dialog)
        self.labelNew.setObjectName(u"labelNew")
        self.labelNew.setGeometry(QRect(30, 20, 181, 91))
        self.labelNew.setStyleSheet(u"background-color: rgba(255, 255, 255,200);\n"
"font: 900 14pt \"Arial Black\";\n"
"border-radius:7px;")
        self.labelNew.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.inputTargetEdit = QLineEdit(Dialog)
        self.inputTargetEdit.setObjectName(u"inputTargetEdit")
        self.inputTargetEdit.setGeometry(QRect(40, 50, 161, 51))
        self.inputTargetEdit.setStyleSheet(u"font: 900 12pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;")
        self.inputTargetEdit.setMaxLength(6)
        self.inputTargetEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.saveTargetButton = QPushButton(Dialog)
        self.saveTargetButton.setObjectName(u"saveTargetButton")
        self.saveTargetButton.setGeometry(QRect(40, 130, 161, 50))
        self.saveTargetButton.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0446\u0435\u043b\u044c", None))
        self.labelNew.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0446\u0435\u043b\u044c", None))
        self.saveTargetButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

