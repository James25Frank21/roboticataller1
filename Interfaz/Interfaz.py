import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Interfaz")
        #self.setFixedSize(QSize(600,400))
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

        
         # Radio Buttons 
            # Button yx
        self.radio_buttonyx = QRadioButton('yx')
       
        layout.addWidget(self.radio_buttonyx)
            # Button xz
        self.radio_buttonxz = QRadioButton('xz')
        
        layout.addWidget(self.radio_buttonxz)
            # Button yz
        self.radio_buttonyz = QRadioButton('yz')
        layout.addWidget(self.radio_buttonyz)

        # Button yt
        ytbutton = QPushButton("yt")   
        ytbutton.setFixedSize(QSize(80, 30)) 
        layout.addWidget(ytbutton)

        # Button Visit
        Visitbutton = QPushButton("Visit")   
        Visitbutton.setFixedSize(QSize(80, 30)) 
        layout.addWidget(Visitbutton)

        # Button close
        closebutton = QPushButton("close")   
        closebutton.setFixedSize(QSize(80, 30)) 
        layout.addWidget(closebutton)

        # nums of ...
        num_of = QSpinBox()
        layout.addWidget(num_of)

        # Horizantal layout 1
        Hlayout = QHBoxLayout()
        layout.addLayout(Hlayout)

        # num animation
        num_anima1 = QSpinBox()
        layout.addWidget(num_anima1)

        num_anima2 = QSpinBox()
        layout.addWidget(num_anima2)

         # Button animation 
        animation_button = QPushButton("Animation")   
        layout.addWidget(animation_button)

        # label row
        text_box = QLabel('#of row')
        Hlayout.addWidget(text_box)
        # text_box.move(50,14)
        # text_box.setGeometry(100, 50, 100, 30) 


        # num of rows
        num_rows = QSpinBox()
        Hlayout.addWidget(num_rows)
      
        
        # num of columns
        num_columns = QSpinBox()
        Hlayout.addWidget(num_columns)

        # label colunm
        column_labe = QLabel('#of column')
        Hlayout.addWidget(column_labe)
        
        # casillas 
        pngBox = QCheckBox(".png")
        mp4Box  = QCheckBox(".mp4")
        syncBox = QCheckBox("sync panel")

        Hlayout.addWidget(pngBox)
        Hlayout.addWidget(mp4Box)
        Hlayout.addWidget(syncBox)

       
        # Radio Buttons 
            # Button 1 
        self.radio_button1 = QRadioButton()
       
        layout.addWidget(self.radio_button1)
            # Button 2
        self.radio_button2 = QRadioButton()
        
        layout.addWidget(self.radio_button2)
            # Button 3
        self.radio_button3 = QRadioButton()
        
        layout.addWidget(self.radio_button3)
            # Button 4
        self.radio_button4 = QRadioButton()
        
        layout.addWidget(self.radio_button4)
            # Button 5
        self.radio_button5 = QRadioButton()
        
        layout.addWidget(self.radio_button5)
        
            # Button 6
        self.radio_button6 = QRadioButton()
        
        layout.addWidget(self.radio_button6)

        # Button config. load 
        load_button = QPushButton("Config. load")   
        load_button.setFixedSize(QSize(90, 30)) 
        layout.addWidget(load_button, alignment=Qt.AlignmentFlag.AlignRight)

         # Button config. save 
        save_button = QPushButton("Config. save")  
        save_button.setFixedSize(QSize(90, 30)) 
        layout.addWidget(save_button, alignment=Qt.AlignmentFlag.AlignRight)

        # Button Quit
        quit_button = QPushButton("Quit")   
        quit_button.clicked.connect(self.close)  
        quit_button.setFixedSize(QSize(40,30))
        
        layout.addWidget(quit_button, alignment=Qt.AlignmentFlag.AlignRight)

   

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
