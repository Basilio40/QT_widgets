# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesoyjJYY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_aplication_pages(object):
    def setupUi(self, aplication_pages):
        if not aplication_pages.objectName():
            aplication_pages.setObjectName(u"aplication_pages")
        aplication_pages.resize(808, 589)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout = QVBoxLayout(self.page1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.page1)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 70))
        self.frame.setMaximumSize(QSize(500, 70))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 14pt \"Segoe UI\";\n"
"color:rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"     background-color: rgb(68, 71, 90);\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.btn_change_text = QPushButton(self.frame)
        self.btn_change_text.setObjectName(u"btn_change_text")
        self.btn_change_text.setMinimumSize(QSize(120, 36))
        self.btn_change_text.setMaximumSize(QSize(36, 36))
        self.btn_change_text.setMouseTracking(True)
        self.btn_change_text.setTabletTracking(True)
        self.btn_change_text.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")

        self.gridLayout.addWidget(self.btn_change_text, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)

        aplication_pages.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_2 = QVBoxLayout(self.page2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        aplication_pages.addWidget(self.page2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        aplication_pages.addWidget(self.page)

        self.retranslateUi(aplication_pages)

        QMetaObject.connectSlotsByName(aplication_pages)
    # setupUi

    def retranslateUi(self, aplication_pages):
        aplication_pages.setWindowTitle(QCoreApplication.translate("aplication_pages", u"StackedWidget", None))
        self.label_3.setText(QCoreApplication.translate("aplication_pages", u"Ol\u00e1...", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("aplication_pages", u"Escreva o seu nome ", None))
        self.btn_change_text.setText(QCoreApplication.translate("aplication_pages", u"Alterar Texto", None))
        self.label_2.setText(QCoreApplication.translate("aplication_pages", u"Pagina 2 ", None))
        self.label.setText(QCoreApplication.translate("aplication_pages", u"Pagina 3", None))
    # retranslateUi

