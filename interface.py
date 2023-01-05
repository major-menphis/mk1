import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QLabel, QStatusBar,
    QStackedLayout, QWidget
    )
from PyQt6.QtGui import QAction, QIcon, QGuiApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # titulo da janela
        self.setWindowTitle('MK1')
        # tamanho da janela
        self.resize(800, 600)
        # obter tamanho da tela e centralizar a janela
        screen = QGuiApplication.primaryScreen().availableGeometry()
        x = (screen.width() - self.size().width()) // 2
        y = (screen.height() - self.size().height()) // 2
        self.move(x, y)
        # cria o layout principal
        self.main_layout = QStackedLayout()
        self.setLayout(self.main_layout)
        # cria label button 1
        self.label_button_1 = QLabel()
        self.label_button_1.setText('botao 1')
        # cria label button 2
        self.label_button_2 = QLabel()
        self.label_button_2.setText('botao 2')
        # cria o botao 1
        button_action = QAction(QIcon(), "Botão 1", self)
        button_action.setStatusTip("Este é meu primeiro botão.")
        button_action.triggered.connect(self.button_1)
        self.main_layout.addWidget(self.label_button_1)
        # cria o botão 2
        button_action2 = QAction(QIcon(), "Botão 2", self)
        button_action2.setStatusTip("Este é meu segundo botão.")
        button_action2.triggered.connect(self.button_2)
        self.main_layout.addWidget(self.label_button_2)
        # exibe as a dica na barra de status
        self.setStatusBar(QStatusBar(self))
        # referencia a barra de menu
        menu = self.menuBar()
        # adiciona os itens na opção 'Menu'
        file_menu = menu.addMenu("Menu")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)
        # configura o widget central
        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

    def button_1(self, s):
        self.main_layout.setCurrentIndex(0)
        print("click", s)

    def button_2(self, s):
        self.main_layout.setCurrentIndex(1)
        print("click", s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
