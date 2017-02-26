#1/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets

class MapEditorWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class MapEditor(object):
    def __init__(self, argv, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.qapplication = QtWidgets.QApplication(argv)

    def exec(self):
        return self.qapplication.exec()
