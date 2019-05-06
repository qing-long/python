import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.MonacoFont = QFont('Monaco', 14)
        self.init_ui()
        self.common()

    def init_ui(self):
        self.statusBar().setFont(self.MonacoFont)
        self.statusBar().showMessage('this is statusbar')
        pass

    def common(self):
        self.setGeometry(800, 400, 300, 300)
        self.setWindowTitle('this is windows title')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())
