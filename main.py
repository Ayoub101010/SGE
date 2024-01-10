from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import MySQLdb
import datetime

ui, _ = loadUiType('Admin.ui')
login,_ = loadUiType('Login.ui')

def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handel_Login)
        
class Login(QWidget , login):
        
    def Handel_Login(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='jenousJe@123' , db='APOGEE')
        #La création de l'objet cursor pour interagir avec la bdd, pour exécuter des requêtes SQL
        self.cur = self.db.cursor()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        sql = ''' SELECT * FROM users'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data  :
            if username == row[1] and password == row[3]:
                self.window2 = MainApp()
                self.close()
                self.window2.show()

            else:
                self.label.setText('Make Sure You Enterd Your Username And Password Correctly')  

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()

        self.Handel_Buttons()  


    def Handel_Buttons(self):
     pass 
 
 
def main():
       app = QApplication(sys.argv)
       window = Login()
       window.show()
       sys.exit(app.exec_())

if __name__ == '__main__':
     main()