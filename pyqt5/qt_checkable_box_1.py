import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.MonacoFont = QFont('Monaco', 14)
        self.init_ui()
        self.common()

    def init_ui(self):
        self.statusBar().setFont(self.MonacoFont)
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('this is statusbar')

        menubar = self.menuBar()
        menubar.setFont(self.MonacoFont)

        fileMenu = menubar.addMenu('File')
        settingMenu = menubar.addMenu('Setting')

        newAct = QAction('new', self)
        impMenu = QMenu('Import', self)
        impAct = QAction('imp Action', self)
        impMenu.addAction(impAct)
        fontAct = QAction('font', self)

        viewStatAct = QAction('view checkbox', self, checkable=True)
        viewStatAct.setStatusTip('this is view status tip')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        fileMenu.addAction(newAct)
        fileMenu.addAction(viewStatAct)
        fileMenu.addMenu(impMenu)
        settingMenu.addAction(fontAct)

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def common(self):
        self.setGeometry(800, 400, 300, 300)
        self.setWindowTitle('this is windows title')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())
