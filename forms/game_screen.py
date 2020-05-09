from PyQt5.QtWidgets import QMainWindow
from forms.design.game_screen_design import Ui_MainWindow


class GameScreen(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

