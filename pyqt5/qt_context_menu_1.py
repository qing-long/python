import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, qApp


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.common()
        pass

    def init_ui(self):
        pass

    def contextMenuEvent(self, event):
        contextMenu = QMenu()
        newAct = contextMenu.addAction('New')
        openAct = contextMenu.addAction('Open')
        quitAct = contextMenu.addAction('Quit')

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()
        if action == newAct:
            pass
        if action == openAct:
            pass

    def common(self):
        self.setGeometry(800, 400, 300, 300)
        self.setWindowTitle('this is windows title')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())
