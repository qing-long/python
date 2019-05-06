#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    pyqt5.qt_helloworld
    -------------------

    pyqt5 hello world a minimize pyqt5 application
    :copyright: (c) 2018-09-26 by buglan
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(250, 150)
    widget.move(300, 300)
    widget.setWindowTitle("Hello World")
    widget.show()
    sys.exit(app.exit_())
