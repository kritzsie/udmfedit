#1/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class MapEditorWindow(QtWidgets.QMainWindow):
    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)

        scene = QtWidgets.QGraphicsScene()
        view = QtWidgets.QGraphicsView(scene)

        scene.setBackgroundBrush(QtGui.QBrush(QtCore.Qt.black))

        self.setCentralWidget(view)
        self.setWindowTitle(title)
        self.showMaximized()
