import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.common()
        pass

    def init_ui(self):
        lable = QLabel('buglan', self)
        lable.move(0, 0)

        lable1 = QLabel('lan', self)
        lable1.move(10, 20)

        lable2 = QLabel('bug', self)
        lable2.move(30, 60)
        pass

    def common(self):
        self.setGeometry(800, 400, 300, 300)
        self.setWindowTitle('this is windows title')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())
