import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QSplitter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Splitter Example")
        self.setGeometry(100, 100, 800, 600)

        parteHorizontal  = QHBoxLayout()
        parteHorizontal.addLayout(parteHorizontal)

    def panelDerecho(self):
        pass
    def panelIzquierdo(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
