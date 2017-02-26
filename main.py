#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

import qt5gui

if __name__ == "__main__":
    app = qt5gui.MapEditor(sys.argv)

    win = qt5gui.MapEditorWindow()
    win.setWindowTitle("Hello, world!")
    win.show()

    exit(app.exec())
