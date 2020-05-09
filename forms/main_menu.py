import sys

from PyQt5.QtWidgets import QMainWindow
from forms.design.main_menu_design import Ui_main_menu


class MainMenu(QMainWindow, Ui_main_menu):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Binding buttons
        self.create_btn.clicked.connect(self.open_create_menu)
        self.join_btn.clicked.connect(self.open_join_menu)
        self.exit_btn.clicked.connect(sys.exit)

    def open_create_menu(self):
        from forms.create_menu import CreateMenu
        self.close()
        self.window = CreateMenu()
        self.window.show()

    def open_join_menu(self):
        from forms.join_menu import JoinMenu
        self.close()
        self.window = JoinMenu()
        self.window.show()