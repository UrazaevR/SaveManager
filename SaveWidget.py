from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QApplication
from PyQt6.QtGui import QPixmap
import sys
from typing import overload


class SaveWidget(QWidget):
    @overload
    def __init__(self, name: str, icon_path: str):
        ...

    @overload
    def __init__(self, parent: QWidget | None, name: str, icon_path: str):
        ...

    def __init__(self, *args):
        if len(args) == 2:
            parent = None
            name, icon_path = args
        elif len(args) == 3:
            parent, name, icon_path = args
        else:
            raise TypeError(f'SaveWidget expected 3 or 4 argument, got {len(args) + 1}')

        super().__init__(parent=parent)

        # метки
        self.icon = QLabel(self)
        self.name = QLabel(name, self)
        self.last_saves = QLabel(self)

        #иконка
        self.icon.setPixmap(QPixmap(icon_path))

        # кнопки
        self.save_but = QPushButton('Save', self)
        self.load_but = QPushButton('Load', self)
        self.edit_but = QPushButton('...', self)

        #слои
        main_layout = QHBoxLayout()
        labels_layout = QVBoxLayout()
        buttons_layout = QVBoxLayout()
        
        labels_layout.addWidget(self.name)
        labels_layout.addWidget(self.last_saves)
        
        buttons_layout.addWidget(self.save_but)
        buttons_layout.addWidget(self.load_but)

        main_layout.addWidget(self.icon)
        main_layout.addLayout(labels_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.edit_but)

        self.setLayout(main_layout)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = SaveWidget(None, 'Новое сохранение', 'default_icon.ico')
    widget.show()
    app.exec()