# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesuzhezy.ui'
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
        aplication_pages.resize(1002, 610)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1.setEnabled(True)
        self.widget = QWidget(self.page1)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 10, 871, 511))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.linetexto = QLineEdit(self.widget)
        self.linetexto.setObjectName(u"linetexto")
        self.linetexto.setStyleSheet(u"QLineEdit{\n"
"     background-color:#44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.linetexto)

        self.pushentrada = QPushButton(self.widget)
        self.pushentrada.setObjectName(u"pushentrada")
        self.pushentrada.setStyleSheet(u"QPushButton{\n"
"     background-color: #44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"     border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"      background-color: rgb(255, 0, 127);\n"
"}")

        self.horizontalLayout.addWidget(self.pushentrada)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.linepdf = QLineEdit(self.widget)
        self.linepdf.setObjectName(u"linepdf")
        self.linepdf.setStyleSheet(u"QLineEdit{\n"
"     background-color:#44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.linepdf)

        self.pushPdf = QPushButton(self.widget)
        self.pushPdf.setObjectName(u"pushPdf")
        self.pushPdf.setStyleSheet(u"QPushButton{\n"
"     background-color: #44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"     border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"      background-color: rgb(255, 0, 127);\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushPdf)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.linexml = QLineEdit(self.widget)
        self.linexml.setObjectName(u"linexml")
        self.linexml.setStyleSheet(u"QLineEdit{\n"
"     background-color:#44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.linexml)

        self.pushXml = QPushButton(self.widget)
        self.pushXml.setObjectName(u"pushXml")
        self.pushXml.setStyleSheet(u"QPushButton{\n"
"     background-color: #44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"     border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"      background-color: rgb(255, 0, 127);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushXml)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.linetxt = QLineEdit(self.widget)
        self.linetxt.setObjectName(u"linetxt")
        self.linetxt.setStyleSheet(u"QLineEdit{\n"
"     background-color:#44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.linetxt)

        self.pushTxt = QPushButton(self.widget)
        self.pushTxt.setObjectName(u"pushTxt")
        self.pushTxt.setStyleSheet(u"QPushButton{\n"
"     background-color: #44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"     border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"      background-color: rgb(255, 0, 127);\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushTxt)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.linecsv = QLineEdit(self.widget)
        self.linecsv.setObjectName(u"linecsv")
        self.linecsv.setStyleSheet(u"QLineEdit{\n"
"     background-color:#44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"}")

        self.horizontalLayout_5.addWidget(self.linecsv)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"     background-color: #44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"     border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"      background-color: rgb(255, 0, 127);\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.pushButton = QPushButton(self.page1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(742, 540, 151, 41))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"     background-color: #44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"     border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"      background-color: rgb(255, 0, 127);\n"
"}")
        aplication_pages.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_2 = QVBoxLayout(self.page2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.page2_2 = QWidget(self.page2)
        self.page2_2.setObjectName(u"page2_2")
        self.alugarveiculo = QPushButton(self.page2_2)
        self.alugarveiculo.setObjectName(u"alugarveiculo")
        self.alugarveiculo.setGeometry(QRect(29, 20, 120, 100))
        self.alugarveiculo.setMinimumSize(QSize(70, 80))
        self.alugarveiculo.setMaximumSize(QSize(200, 200))
        self.alugarveiculo.setStyleSheet(u"QPushButton{\n"
"     background-color: #44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"     border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"      background-color: rgb(255, 0, 127);\n"
"}")
        self.cadastrarcliente = QPushButton(self.page2_2)
        self.cadastrarcliente.setObjectName(u"cadastrarcliente")
        self.cadastrarcliente.setGeometry(QRect(210, 20, 120, 100))
        self.cadastrarcliente.setMinimumSize(QSize(70, 80))
        self.cadastrarcliente.setMaximumSize(QSize(200, 200))
        self.cadastrarcliente.setStyleSheet(u"QPushButton{\n"
"     background-color: #44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"     border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"      background-color: rgb(255, 0, 127);\n"
"}")
        self.cadastrarveiculo = QPushButton(self.page2_2)
        self.cadastrarveiculo.setObjectName(u"cadastrarveiculo")
        self.cadastrarveiculo.setGeometry(QRect(390, 20, 120, 100))
        self.cadastrarveiculo.setMinimumSize(QSize(70, 80))
        self.cadastrarveiculo.setMaximumSize(QSize(200, 200))
        self.cadastrarveiculo.setStyleSheet(u"QPushButton{\n"
"     background-color: #44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"     border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"      background-color: rgb(255, 0, 127);\n"
"}")
        self.listarcliente = QPushButton(self.page2_2)
        self.listarcliente.setObjectName(u"listarcliente")
        self.listarcliente.setGeometry(QRect(580, 20, 120, 100))
        self.listarcliente.setMinimumSize(QSize(70, 80))
        self.listarcliente.setMaximumSize(QSize(200, 200))
        self.listarcliente.setStyleSheet(u"QPushButton{\n"
"     background-color: #44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"     border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"      background-color: rgb(255, 0, 127);\n"
"}")
        self.listarveiculo = QPushButton(self.page2_2)
        self.listarveiculo.setObjectName(u"listarveiculo")
        self.listarveiculo.setGeometry(QRect(750, 20, 120, 100))
        self.listarveiculo.setMinimumSize(QSize(70, 80))
        self.listarveiculo.setMaximumSize(QSize(200, 200))
        self.listarveiculo.setStyleSheet(u"QPushButton{\n"
"     background-color: #44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(255, 255, 255);\n"
"     border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"     background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"      background-color: rgb(255, 0, 127);\n"
"}")
        self.label_2 = QLabel(self.page2_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 130, 941, 461))
        self.label_2.setStyleSheet(u"QLabel{\n"
"     background-color:#44475a;\n"
"     padding: 8px;\n"
"     border: 2px solid #c3ccdf;\n"
"     color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"\n"
"}")

        self.verticalLayout_2.addWidget(self.page2_2)

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

        aplication_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(aplication_pages)
    # setupUi

    def retranslateUi(self, aplication_pages):
        aplication_pages.setWindowTitle(QCoreApplication.translate("aplication_pages", u"StackedWidget", None))
        self.label_3.setText(QCoreApplication.translate("aplication_pages", u"Entrada", None))
        self.pushentrada.setText(QCoreApplication.translate("aplication_pages", u"Entrada", None))
        self.label_4.setText(QCoreApplication.translate("aplication_pages", u"PDF", None))
        self.pushPdf.setText(QCoreApplication.translate("aplication_pages", u"PDF", None))
        self.label_5.setText(QCoreApplication.translate("aplication_pages", u"XML", None))
        self.pushXml.setText(QCoreApplication.translate("aplication_pages", u"XML", None))
        self.label_6.setText(QCoreApplication.translate("aplication_pages", u"TXT", None))
        self.pushTxt.setText(QCoreApplication.translate("aplication_pages", u"TXT", None))
        self.label_7.setText(QCoreApplication.translate("aplication_pages", u"CSV", None))
        self.pushButton_5.setText(QCoreApplication.translate("aplication_pages", u"CSV", None))
        self.pushButton.setText(QCoreApplication.translate("aplication_pages", u"Salvar", None))
        self.alugarveiculo.setText(QCoreApplication.translate("aplication_pages", u"Alugar Veiculo", None))
        self.cadastrarcliente.setText(QCoreApplication.translate("aplication_pages", u"Cadastrar Cliente", None))
        self.cadastrarveiculo.setText(QCoreApplication.translate("aplication_pages", u"Cadastrar Veiculo", None))
        self.listarcliente.setText(QCoreApplication.translate("aplication_pages", u"Listar Cliente", None))
        self.listarveiculo.setText(QCoreApplication.translate("aplication_pages", u"Listar Veiculo", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("aplication_pages", u"Pagina 3", None))
    # retranslateUi

