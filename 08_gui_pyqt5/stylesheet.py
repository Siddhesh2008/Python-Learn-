#PyQt5 StyleSheet()
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLineEdit,QPushButton,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cool GUI")
        self.button1=QPushButton("Button 1",self)
        self.button2=QPushButton("Button 2",self)
        self.button3=QPushButton("Button 3",self)
        self.initUI()

    def initUI(self):
        central_widget=QWidget()
        self.setCentralWidget(central_widget)
        
        hbox=QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
                           QPushButton{
            font-size: 30px;
            font-family:Arial;
            padding:15px 70px;
            margin:25px;
            border:3px solid blue;
            border-radius:15px;
            }

             QPushButton#button1{
             background-color:red;
                            }

             QPushButton#button2{
            background-color:blue;
                            }

             QPushButton#button3{
             background-color:green;
                            }
                           QPushButton#button1:hover{
             background-color:light red;
                            }

             QPushButton#button2:hover{
            background-color:light blue;
                            }

             QPushButton#button3:hover{
             background-color:light green;
                            }
                           """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
