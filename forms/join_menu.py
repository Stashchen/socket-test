from PyQt5.QtWidgets import QMainWindow
from forms.design.join_menu_design import Ui_join_menu
from forms.main_menu import MainMenu
from logic.client import Client
import threading


class JoinMenu(QMainWindow, Ui_join_menu):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back_btn.clicked.connect(self.open_main_menu)
        self.join_btn.clicked.connect(self.join_game)

    def join_game(self):
        ip, port = Client.parse_address(self.adr_edit.text())
        client = Client(ip, port)
        client.connect_to_server()
        client.send_str(self.nickname_edit.text())
        self.join_btn.setEnabled(False)
        self.wait_players_lable.setText('Wait for other players')

    def open_main_menu(self):
        self.close()
        self.window = MainMenu()
        self.window.show()
