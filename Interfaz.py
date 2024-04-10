import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Botón Quit en PyQt6")
        self.setFixedSize(QSize(600,400))
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)


        text_box = QLabel('#of row')
        layout.addWidget(text_box,alignment=Qt.AlignmentFlag.AlignRight)
        #text_box.setGeometry(100, 50, 100, 30) 

        spin_box = QSpinBox()
        layout.addWidget(spin_box)

        spin_box1 = QSpinBox()
        layout.addWidget(spin_box1)

        text_box1 = QLabel('#of column')
        layout.addWidget(text_box1,alignment=Qt.AlignmentFlag.AlignRight)

        option1_checkbox = QCheckBox(".png")
        option2_checkbox = QCheckBox(".mp4")
        option3_checkbox = QCheckBox("sync panel")

        layout.addWidget(option1_checkbox)
        layout.addWidget(option2_checkbox)
        layout.addWidget(option3_checkbox)

        # Crear un botón llamado "Quit"
        quit_button = QPushButton("Quit")
        quit_button.setGeometry(50, 50, 50, 40)
        quit_button.clicked.connect(self.close)  
        quit_button.setFixedSize(QSize(40,30))
        
        #layout.addWidget(quit_button)
        layout.addWidget(quit_button, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
