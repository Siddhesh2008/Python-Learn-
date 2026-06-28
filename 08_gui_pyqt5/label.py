#PyQt5 Qlabels
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cool GUI")
        self.setGeometry(700,300,700,700)

        label=QLabel("Hello",self)
        label.setFont( QFont("Arial",40))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color:red;"
                            "background-color:black;"
                            "font-weight:bold;"
                            "font-style:italic;"
                            "text-decoration:underline;")
      #  label.setAlignment(Qt.AlignTop)    #top
       # label.setAlignment(Qt.AlignBottom)   #bottom
        #label.setAlignment(Qt.AlignVCenter)    #vertical center  
       # label.setAlignment(Qt.AlignRight)   #right
       #label.setAlignment(Qt.AlignHCenter)   #horizotal center
        #label.setAlignment(Qt.AlignLeft)   #left

        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)     #for multiple

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()

