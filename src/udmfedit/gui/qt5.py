#1/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from . import qt5ui

class MapEditorWindow(QtWidgets.QWidget, qt5ui.Ui_window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)

        scene.setBackgroundBrush(QtGui.QBrush(QtCore.Qt.black))
