import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolTip, QPushButton
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.MonacoFont = QFont('Monaco', 14)

        # do something
        self.init_ui()
        self.common()

    def init_ui(self):
        # global tooltip
        QToolTip.setFont(self.MonacoFont)
        self.setToolTip('This is a <b>global</b> tooltip')

        # button tooltip
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>button</b> widget')
        btn.setFont(self.MonacoFont)
        btn.move(50, 50)

    def common(self):
        # set height and width
        self.setGeometry(800, 400, 300, 300)

        # set window title
        self.setWindowTitle('this is windows title')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())
