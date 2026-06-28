import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel ,QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cool GUI")
        self.setGeometry(700,300,700,700)
        self.label=QLabel("Hello",self)
        self.initUI()

    def initUI(self):
        self.button=QPushButton("Click Me",self)
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet('font-size: 30px;')
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(0,0,500,100)
        self.label.setStyleSheet("color:red;"
                                "background-color:black;"
                                "font-weight:bold;"
                                "font-style:italic;"
                                "text-decoration:underline;")

    def on_click(self):
        self.label.setText("Button Clicked")
       
 
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


