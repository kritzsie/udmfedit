#1/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets

class MapEditorWindow(QtWidgets.QMainWindow):
    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setCentralWidget(QtWidgets.QGraphicsView())
        self.setWindowTitle(title)

        self.centralWidget().show()
        self.show()
