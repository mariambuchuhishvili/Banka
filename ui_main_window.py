# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(476, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(0,0,0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.banka = QWidget(self.centralwidget)
        self.banka.setObjectName(u"banka")
        self.banka.setGeometry(QRect(30, 20, 191, 241))
        self.progressBar = QProgressBar(self.banka)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(29, 18, 131, 211))
        self.progressBar.setStyleSheet(u"QProgressBar::chunk {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.716, x2:1, y2:0.716, stop:0.0113636 rgba(255, 219, 219, 255), stop:0.386364 rgba(198, 148, 209, 255), stop:0.659091 rgba(224, 128, 182, 255), stop:1 rgba(104, 74, 132, 255));\n"
"}\n"
"QProgressBar {\n"
"text-align: center;\n"
"color: rgb(0, 0, 0);\n"
"font: 900 14pt \"Arial Black\";\n"
"}\n"
"")
        self.progressBar.setValue(100)
        self.progressBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Vertical)
        self.verticalFrame_2 = QFrame(self.banka)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setGeometry(QRect(-10, 10, 211, 231))
        self.verticalFrame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));\n"
"image: url(:/img/img/plese.png);")
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(30, 360, 420, 211))
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.205, y2:0.198864, stop:0 rgba(104, 74, 132, 255), stop:1 rgba(221, 164, 233, 255)); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"color: black;\n"
"font: 700 8pt \"Arial Black\";\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(104, 74, 132);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 12pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setTextElideMode(Qt.ElideMiddle)
        self.tableView.setShowGrid(False)
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setDefaultSectionSize(140)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setGeometry(QRect(50, 290, 161, 61))
        self.horizontalLayout = QHBoxLayout(self.verticalFrame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addButton = QPushButton(self.verticalFrame)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(14)
        font.setWeight(QFont.ExtraBold)
        font.setItalic(False)
        self.addButton.setFont(font)
        self.addButton.setMouseTracking(True)
        self.addButton.setAutoFillBackground(False)
        self.addButton.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.198, y2:0.1875, stop:0 rgba(32, 72, 34, 255), stop:1 rgba(0, 170, 0, 255));\n"
"border-radius: 7px;\n"
"font: 800 14pt \"Arial Black\";\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(98, 190, 93);\n"
"border-radius: 7px;\n"
"font: 800 14pt \"Arial Black\";\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(32, 72, 34);\n"
"border-radius: 7px;\n"
"font: 800 14pt \"Arial Black\";\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/img/img/add_circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setIconSize(QSize(25, 25))
        self.addButton.setCheckable(False)
        self.addButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.addButton)

        self.editButton = QPushButton(self.verticalFrame)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setMaximumSize(QSize(50, 50))
        self.editButton.setFont(font)
        self.editButton.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.198, y2:0.1875, stop:0 rgba(51, 52, 115, 255), stop:1 rgba(0, 96, 217, 255));\n"
"border-radius: 7px;\n"
"font: 800 14pt \"Arial Black\";\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(144, 155, 255);\n"
"border-radius: 7px;\n"
"font: 800 14pt \"Arial Black\";\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 0, 161);\n"
"border-radius: 7px;\n"
"font: 800 14pt \"Arial Black\";\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/img/img/edit_FILL0.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editButton.setIcon(icon1)
        self.editButton.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(self.verticalFrame)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setMaximumSize(QSize(50, 50))
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.324227, y2:0.267, stop:0 rgba(106, 11, 62, 255), stop:1 rgba(191, 20, 108, 255));\n"
"border-radius: 7px;\n"
"font: 800 14pt \"Arial Black\";\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(217, 76, 149);\n"
"border-radius: 7px;\n"
"font: 800 14pt \"Arial Black\";\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(106, 11, 62);\n"
"border-radius: 7px;\n"
"font: 800 14pt \"Arial Black\";\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/img/img/delete_FILL0.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteButton.setIcon(icon2)
        self.deleteButton.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.deleteButton)

        self.target = QLabel(self.centralwidget)
        self.target.setObjectName(u"target")
        self.target.setGeometry(QRect(270, 60, 141, 51))
        self.target.setStyleSheet(u"background-color: rgb(104, 74, 132);\n"
"font: 20pt \"Swis721 BlkCn BT\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 7px;")
        self.target.setScaledContents(False)
        self.target.setAlignment(Qt.AlignCenter)
        self.labelTarget = QLabel(self.centralwidget)
        self.labelTarget.setObjectName(u"labelTarget")
        self.labelTarget.setGeometry(QRect(260, 30, 161, 131))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(14)
        font1.setWeight(QFont.Black)
        font1.setItalic(False)
        self.labelTarget.setFont(font1)
        self.labelTarget.setStyleSheet(u"background-color: rgba(255, 255, 255,200);\n"
"font: 900 14pt \"Arial Black\";\n"
"border-radius:7px;")
        self.labelTarget.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.labelCurrent = QLabel(self.centralwidget)
        self.labelCurrent.setObjectName(u"labelCurrent")
        self.labelCurrent.setGeometry(QRect(260, 170, 161, 91))
        self.labelCurrent.setStyleSheet(u"background-color: rgba(255, 255, 255,200);\n"
"font: 900 14pt \"Arial Black\";\n"
"border-radius:7px;")
        self.labelCurrent.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.labelTarget_2 = QLabel(self.centralwidget)
        self.labelTarget_2.setObjectName(u"labelTarget_2")
        self.labelTarget_2.setGeometry(QRect(370, 30, 31, 31))
        font2 = QFont()
        font2.setFamilies([u"Swis721 BlkCn BT"])
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        self.labelTarget_2.setFont(font2)
        self.labelTarget_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));")
        self.labelTarget_2.setPixmap(QPixmap(u":/img/img/target_FILL0.svg"))
        self.labelTarget_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.targetButton = QPushButton(self.centralwidget)
        self.targetButton.setObjectName(u"targetButton")
        self.targetButton.setGeometry(QRect(270, 120, 141, 31))
        self.targetButton.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setFamilies([u"Arial Black"])
        font3.setPointSize(10)
        font3.setWeight(QFont.ExtraBold)
        font3.setItalic(False)
        self.targetButton.setFont(font3)
        self.targetButton.setMouseTracking(True)
        self.targetButton.setAutoFillBackground(False)
        self.targetButton.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.205, y2:0.198864, stop:0 rgba(104, 74, 132, 255), stop:1 rgba(221, 164, 233, 255));\n"
"border-radius: 7px;\n"
"font: 800 10pt \"Arial Black\";\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(216, 179, 229);\n"
"border-radius: 7px;\n"
"font: 800 10pt \"Arial Black\";\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(104, 74, 132);\n"
"border-radius: 7px;\n"
"font: 800 10pt \"Arial Black\";\n"
"}\n"
"")
        self.targetButton.setCheckable(False)
        self.targetButton.setAutoDefault(False)
        self.current = QLabel(self.centralwidget)
        self.current.setObjectName(u"current")
        self.current.setGeometry(QRect(270, 200, 141, 51))
        self.current.setStyleSheet(u"background-color: rgb(104, 74, 132);\n"
"font: 20pt \"Swis721 BlkCn BT\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 7px;")
        self.current.setScaledContents(False)
        self.current.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.labelCurrent.raise_()
        self.banka.raise_()
        self.tableView.raise_()
        self.verticalFrame.raise_()
        self.labelTarget.raise_()
        self.target.raise_()
        self.labelTarget_2.raise_()
        self.targetButton.raise_()
        self.current.raise_()

        self.retranslateUi(MainWindow)

        self.addButton.setDefault(False)
        self.targetButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043d\u043a\u0430", None))
        self.addButton.setText("")
        self.editButton.setText("")
        self.deleteButton.setText("")
        self.target.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.labelTarget.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043b\u044c", None))
        self.labelCurrent.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0431\u0430\u043d\u043a\u0435", None))
        self.labelTarget_2.setText("")
        self.targetButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0446\u0435\u043b\u044c", None))
        self.current.setText(QCoreApplication.translate("MainWindow", u"1000", None))
    # retranslateUi

