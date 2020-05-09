import sys
from PyQt5.QtWidgets import QApplication
from forms.main_menu import MainMenu

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    app.exec_()
