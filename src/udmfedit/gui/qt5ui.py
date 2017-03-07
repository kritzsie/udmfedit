# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'udmfedit-qt.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(800, 600)
        window.setMinimumSize(QtCore.QSize(320, 200))
        self.windowLayout = QtWidgets.QVBoxLayout(window)
        self.windowLayout.setContentsMargins(0, 0, 0, 0)
        self.windowLayout.setObjectName("windowLayout")
        self.tabWidget = QtWidgets.QTabWidget(window)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabLayout = QtWidgets.QVBoxLayout(self.tab)
        self.tabLayout.setContentsMargins(0, 0, 0, 0)
        self.tabLayout.setObjectName("tabLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setObjectName("graphicsView")
        self.tabLayout.addWidget(self.graphicsView)
        self.tabWidget.addTab(self.tab, "")
        self.windowLayout.addWidget(self.tabWidget)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Qt UDMF Editor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("window", "Untitled"))

