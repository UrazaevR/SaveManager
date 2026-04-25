import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget


class SaveManagerWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle = 'SaveManager v0.0.1'

        # Панель инструментов
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        edit_menu = menu_bar.addMenu('&Edit')
        help_menu = menu_bar.addMenu('&Help')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SaveManagerWin()
    win.show()
    app.exec()