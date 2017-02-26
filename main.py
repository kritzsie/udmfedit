#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from PyQt5 import QtWidgets

import qt5gui

if __name__ == "__main__":
    pid = os.fork()
    if pid:
        print("PID={}".format(pid))
    else:
        app = QtWidgets.QApplication(sys.argv)

        win = qt5gui.MapEditorWindow("Qt UDMF Editor")

        exit(app.exec())
