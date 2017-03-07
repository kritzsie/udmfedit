#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

from PyQt5 import QtWidgets

import gui.qt5

def main():
    pid = os.fork()
    if pid:
        print(pid)
    else:
        app = QtWidgets.QApplication(sys.argv)

        win = gui.qt5.MapEditorWindow()
        win.showMaximized()

        return app.exec()

if __name__ == "__main__":
    main()
