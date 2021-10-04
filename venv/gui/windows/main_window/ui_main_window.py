'''
Hearder
'''

# IMPORTAR o QT CORE

from qt_core import *


# IMPORTAR PAGINAS 

from gui.pages.ui_pages import Ui_aplication_pages # IMPORTAR AS PAGINAS DO QT DESIGN

# IMPORTAR WIDGET CUSTOMIZADO

from gui.widgets.py_push_button import PyPushButton

# MAIN WINDOW

class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        
#==================== PARAMENTROS INICIAIS ==========================================

        parent.resize(1200, 720) # DEFINE O TAMANHO INICIAL DA JANELA 
        parent.setMinimumSize(960, 540) # DEFINE O TAMANHO MINIMO DA TAREFA 

        # CRIAR UM WIDGET CENTRAL
        self.central_frame = QFrame() # CRIA UM FRAME DE BASE "CENTRAL"
        self.central_frame.setStyleSheet("background-color: #282a36") # MODIFICA A COR DO FUNDO DA APLICAÇÃO

        # CRIAR LAYOUT PRINCIPAL
        self.main_layout = QHBoxLayout(self.central_frame) # DEFINE O MENU COMO HORIZONTAL 
        self.main_layout.setContentsMargins(0,0,0,0) # RETIRA A MARGEM 
        self.main_layout.setSpacing(0) # RETIRA OS ESPAÇOS 

#====================== MENU ESQUERDO =================================================

        # CRIAR O MENU A ESQUERDA
        self.left_menu = QFrame()    
        self.left_menu.setStyleSheet("background-color: #44475a") # MODIFICA A COR DO LAYOUT
        self.left_menu.setMaximumWidth(50) # MODIFICA O TAMANHO DO MENU
        self.left_menu.setMinimumWidth(50)

        # LAYOUT DO MENU ESQUERDO
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)  # SE NÃO RETIRAR A MARGEM O LAYOUT FICA TODO QUEBRADO
        self.left_menu_layout.setSpacing(0) # ACOMPANHA A LINHA ACIMA 

        #MENU DA BARRA LATERAL 
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        

        # LAYOUT TOP FRAME
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0) # RETIRA A MARGEM 
        self.left_menu_top_layout.setSpacing(0) # RETIRA OS ESPAÇOS 

        # BOTÕES SUPERIORES 
        self.toggle_button = PyPushButton(
            text="Ocultar menu ",
            icon_path = "icon_menu.svg",
        )
        self.btn_1 = PyPushButton(
            text = "Pagina Incial",
            is_active = True,
            icon_path = "icon_home.svg",
        )
        self.btn_2 = PyPushButton(
            text="Pagina 2 ",
            icon_path = "icon_widgets.svg",
        )

        #ADICIONAR AO BARRA LATERAL ESQUERDA
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_2)
        
        # ESPAÇADOR DO MENU
        self.left_menu_spacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # FRAME DO MENU DE RODAPÉ MENU ESQUERDO
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(40)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        


        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0,0,0,0) # RETIRA A MARGEM 
        self.left_menu_bottom_layout.setSpacing(0) # RETIRA OS ESPAÇOS 

        # BOTÕES INFERRIOR MENU ESQUERDO
        self.settings_btn = PyPushButton(
            text="Configurações",
             icon_path = "icon_settings.svg",

        )

        # ADICIONAR FRAME AO MENU LATERAL ESQUERDO
        self.left_menu_bottom_layout.addWidget(self.settings_btn)

        #LABEL DO MENU DA BARRA LATERAL 
        self.left_menu_label_version =  QLabel("v1.0.0")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet("color: #c3ccdf")

        #ADICIONAR AO LAYOUT

        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)

#======================= CORPO DA APLICAÇÃO =====================================

        # CONTEUDO
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36") # MODIFICA A COR DO LAYOUT


        # LAYOUT DO CONTEUDO 
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        # BARRA SUPERIOR
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30) # define a altura minima da barra 
        self.top_bar.setMaximumHeight(30) # define a altura maxima da barra 
        self.top_bar.setStyleSheet("background-color: #21232d ; color: #6272a4")# MODIFICA A COR DO LAYOUT e a COR DO TEXTO
        self.top_bar_layout = QHBoxLayout(self.top_bar)# BARRA SUPERIOR COM TEXTO SOBRE A BARRA SUPERIOR PADRÃO
        self.top_bar_layout.setContentsMargins(10,0,10,0)# CONFIGURA OS ESPAÇOS NO TEXTO DA BARRA SUPERIOR 

        # LABEL DA ESQUERDA 
        self.top_label_left = QLabel("Essa é minha primeira aplicação com Pyside6")

        # ESPASSADOR SUPERIOR 
        self.top_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)


        # LABEL DA DIREITA 
        self.top_label_right = QLabel("| PÁGINA INICIAL")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # ADICIONAR OS LABEL A BARRA SUPERIOR 
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

        # RODAPÉ
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30) # define a altura minima da barra 
        self.bottom_bar.setMaximumHeight(30) # define a altura maxima da barra 
        self.bottom_bar.setStyleSheet("background-color: #21232d ; color: #6272a4")# MODIFICA A COR DO LAYOUT e a COR DO TEXTO

        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)# BARRA SUPERIOR COM TEXTO SOBRE A BARRA SUPERIOR PADRÃO
        self.bottom_bar_layout.setContentsMargins(10,0,10,0)# CONFIGURA OS ESPAÇOS NO TEXTO DA BARRA SUPERIOR 

        # LABEL DA ESQUERDA 
        self.bottom_label_left = QLabel("Criado por Sandro Bispo")

        # ESPASSADOR SUPERIOR 
        self.bottom_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)


        # LABEL DA DIREITA 
        self.bottom_label_right = QLabel("@ 2021")

        # ADICIONAR OS LABEL A BARRA SUPERIOR 
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)

        # PAGINAS DA APLICAÇÃO
        self.pages = QStackedWidget() # Cria paginas dentro da aplicação 
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2 ; background-color: #282a36 ")
        self.ui_pages = Ui_aplication_pages()
        self.ui_pages.setupUi(self.pages) # IMPORTAR AS PAGINAS
        self.pages.setCurrentWidget(self.ui_pages.page1) # PRIORIZAÇÃO DA PAGINA DE EXECUÇÃO 
    

        # ADICIONAR A BARRA SUPERIOR AO LAYOUT DA APLICAÇÃO 
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # ADICIONAR WIDGETS AO APP
        self.main_layout.addWidget(self.left_menu) # ADICIONA O MENU A APLICAÇÃO PRINCIPAL 
        self.main_layout.addWidget(self.content) # ADICIONA A PAGINA DE CONTEUDO A APLICAÇÃO 

        # SETAR O CENTRAL WIDGET (TROCAR PARAMETROS DO FRAME CENTRAL)
        parent.setCentralWidget(self.central_frame) 


