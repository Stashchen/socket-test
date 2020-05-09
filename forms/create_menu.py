from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from forms.design.create_menu_design import Ui_create_menu
from forms.main_menu import MainMenu
from logic.server import Server
from logic.client import Client


class CreateMenu(QMainWindow, Ui_create_menu):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ip, port = Server.get_address()
        self.server = Server(ip, port)
        self.share_adr_edit.setText(ip + ':' + str(port))

        self.players_table.setRowCount(3)
        self.players_table.setColumnCount(2)

        # Binding buttons
        self.back_btn.clicked.connect(self.open_main_menu)
        self.create_sever_btn.clicked.connect(lambda: self.server.wait_connections(3, self.players_table))
        self.start_game_btn.clicked.connect(self.start_game)

    def open_main_menu(self):
        self.server.sock.close()
        self.close()
        self.window = MainMenu()
        self.window.show()

    def start_game(self):
        self.server.send_all('open_game_screen')
