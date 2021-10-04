'''
Hearder
'''


# IMPORTAR MODULOS
from genericpath import isfile
from PySide6 import QtWidgets
import sys
import os
from os.path import join , isfile
from os import getcwd
from json import dumps, load, loads

# IMPORTAR QT CORE

from qt_core import *

# IMPORTAR CLAESE MAIN WINDOW
from gui.windows.main_window.ui_main_window import UI_MainWindow

# IMPORTAR  ARQUIVO MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Curso de Python e Pyside6") # muda o nome da aplicação 

        
        

        # Setup Mani Window
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        self.verifica_json()

        # Toggle Button
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        # BTN HOME
        self.ui.btn_1.clicked.connect(self.show_page_1)

        # BTN TOMADA 
        self.ui.btn_2.clicked.connect(self.show_page_2)

        #BTN CONFIGURAÇÕES
        self.ui.settings_btn.clicked.connect(self.show_page_3)

        #Evento de click para o botão btn_change_text
        self.ui.ui_pages.pushentrada.clicked.connect(self.change_text)
        
        self.ui.ui_pages.pushPdf.clicked.connect(self.pdf_select)


        self.ui.ui_pages.cadastrarcliente.clicked.connect(self.cadastrarcliente)

        self.ui.ui_pages.pushXml.clicked.connect(self.xml_select)

        self.ui.ui_pages.pushTxt.clicked.connect(self.txt_select)

        self.ui.ui_pages.pushButton_5.clicked.connect(self.csv_select)

        self.ui.ui_pages.pushButton.clicked.connect(self.salvar)

        # Exibir a aplicação 
        self.show()

    def cadastrarcliente(self):
        with open(r'C:/Users/Sandro Bispo/Desktop/Py_tons_prog/log.html', encoding='utf-8', errors='ignore') as f:
            contents = f.read()
            self.ui.ui_pages.label_2.setText(contents)

    # FUNÇÃO DE ALTERAR TEXTO
    def change_text(self):
    
        arquivo = QtWidgets.QFileDialog.getExistingDirectory(
         None, 'teste sandro', "exemplo_dir"
        )
        self.ui.ui_pages.linetexto.setText(arquivo)

    def pdf_select(self):

        arquivo = QtWidgets.QFileDialog.getExistingDirectory(
         None, 'teste sandro', "exemplo_dir"
        )
        self.ui.ui_pages.linepdf.setText(arquivo)
    
    def xml_select(self):

        arquivo = QtWidgets.QFileDialog.getExistingDirectory(
         None, 'teste sandro', "exemplo_dir"
        )
        self.ui.ui_pages.linexml.setText(arquivo)

    def txt_select(self):

        arquivo = QtWidgets.QFileDialog.getExistingDirectory(
         None, 'teste sandro', "exemplo_dir"
        )
        self.ui.ui_pages.linetxt.setText(arquivo)
    
    def csv_select(self):

        arquivo = QtWidgets.QFileDialog.getExistingDirectory(
         None, 'teste sandro', "exemplo_dir"
        )
        self.ui.ui_pages.linecsv.setText(arquivo)
    
    # SALVA 
    def salvar(self):
        with open(join(getcwd(), 'config.json'), 'w') as f:
            complemento = {"entrada":{'caminho':self.ui.ui_pages.linetexto.text() , 'tipo': 'pst', 'verifica': True}, 
            "pdf":{'caminho':self.ui.ui_pages.linepdf.text(), 'tipo': 'pst', 'verifica': True},
            "saida":{'caminho':self.ui.ui_pages.linexml.text(),'tipo': 'pst', 'verifica': True},
            "xml":{'caminho':self.ui.ui_pages.linetxt.text(),'tipo': 'pst', 'verifica': True},}
            f.write(dumps(complemento, indent=4)) 
            QtWidgets.QMessageBox.information(None, "TESTES DE QUALQUER COISA", f"SALVANDO O JSON <b>{join(getcwd(), 'config.json')}</b> COM SUCESSO!!")

    # VERIFICA SE O JSON EXISTE 
    def verifica_json(self):
        if isfile(join(getcwd(), 'config.json')):
            self.existe_json()
        else:
            self.nao_json_existe()


    # SE O JSON NÃO EXISTIR  
    def nao_json_existe(self):
        self.ui.ui_pages.linetexto.setText("Favor selecione o Arquivo")
        self.ui.ui_pages.linepdf.setText("Favor selecione o Arquivo")
        self.ui.ui_pages.linecsv.setText("Favor selecione o Arquivo")
        self.ui.ui_pages.linetxt.setText("Favor selecione o Arquivo")
        self.ui.ui_pages.linexml.setText("Favor selecione o Arquivo")

    # SE JSON EXISTIR 
    def existe_json(self):
        with open(join(getcwd(), 'config.json'), 'r') as f:
           arq =  f.read()
           json = loads(arq)
           self.ui.ui_pages.linetexto.setText(json['entrada']['caminho'])
           self.ui.ui_pages.linepdf.setText(json['pdf']['caminho'])
           self.ui.ui_pages.linetxt.setText(json['saida']['caminho'])
           self.ui.ui_pages.linexml.setText(json['xml']['caminho'])
           

    
    # FUNÇÃO TROCA O ESTADO DO ACTTIVE DO BOTÃO PARA FALSE 
    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    #  BUSCAR AS PAGINAS A SEREM EXIBIDAS 

    def show_page_1(self):
        self.reset_selection() # CHAMA A FUNÇÃO RESET_SELECTION 
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page1) 
        self.ui.btn_1.set_active(True) # ATIVA O ESTILO DE ATIVO DO BOTÃO (A BARRINHA NA LATERAL)

    def show_page_2(self):
        self.reset_selection() 
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page2)
        self.ui.btn_2.set_active(True)
    
    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page)
        self.ui.settings_btn.set_active(True)


    def toggle_button(self):
        # Get largura do Menu
        menu_width = self.ui.left_menu.width()

        # Conferir a largura
        width = 50
        if menu_width == 50:
            width =240
        
        # Inicio animação
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth") #Cria a Animação da barra lateral
        self.animation.setStartValue(menu_width) # Inicia o que vai ser animado
        self.animation.setEndValue(width) # Define o final da animação
        self.animation.setDuration(500) # define o tempo milisegudos 
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)# curva de animação 
        self.animation.start() # Inicia a animação total 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
