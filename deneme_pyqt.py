from PyQt5 import QtWidgets
import sys
from Atm_project_admin import *
from Atm_project_client import *

control_client = Process_of_client()

control_admin = Process_of_admin()

class Login(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.dialog()

    def dialog(self):        
        self.setWindowTitle("Login")
        self.resize(500,120)

        layout = QtWidgets.QGridLayout()

        label_name = QtWidgets.QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QtWidgets.QLineEdit()
        self.lineEdit_username.setPlaceholderText("Please enter your user name")
        layout.addWidget(label_name,0,0)
        layout.addWidget(self.lineEdit_username,0,1)

        label_password = QtWidgets.QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QtWidgets.QLineEdit()
        self.lineEdit_password.setPlaceholderText("Please enter your user password")
        layout.addWidget(label_password,1,0)
        layout.addWidget(self.lineEdit_password,1,1)

        login_buton = QtWidgets.QPushButton("Login")
        layout.addWidget(login_buton,2,1)

        login_buton.clicked.connect(self.client_entering)

        self.setLayout(layout)


    def client_entering(self,no):
        entered_password = self.lineEdit_password.text()
        self.entered_no = self.lineEdit_username.text()
        true_password = control_admin.client_enter(self.entered_no)
        if(int(entered_password) == true_password):            
            self.accept()
            balance = control_client.client_info(self.entered_no).Balance
            return balance
                    
        else :
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or password')
            self.lineEdit_password.clear()
            self.lineEdit_username.clear()

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.window()
        
    def window(self):
        self.setWindowTitle("Window")
        self.resize(600,600)
        vbox = QtWidgets.QVBoxLayout()
        tabWidget = QtWidgets.QTabWidget()

        tabWidget.addTab(Tab_ballance(), "Varlıklar")
        tabWidget.addTab(Tab_debt(), "Borçlar")

        vbox.addWidget(tabWidget)

        self.setLayout(vbox)



class Tab_ballance(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ballance_ui()
        
    
    def ballance_ui(self):

        g_box = QtWidgets.QGridLayout()

        self.total_balance = QtWidgets.QLabel("Toplam")
        self.checking_account = QtWidgets.QLabel("Vadesiz Hesap")
        self.deposit_account = QtWidgets.QLabel("Vadeli Hesap")
        self.total_balance_amount = QtWidgets.QLabel()
        self.checking_account_amount = QtWidgets.QLabel()
        self.deposit_account_amount = QtWidgets.QLabel()

        g_box.addWidget(self.total_balance,0,1)
        g_box.addWidget(self.checking_account,1,0)
        g_box.addWidget(self.deposit_account,2,0)
        g_box.addWidget(self.total_balance_amount,0,1)
        g_box.addWidget(self.checking_account_amount,1,1)
        g_box.addWidget(self.deposit_account_amount,2,1)

        self.setLayout(g_box)

class Tab_debt(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.debt_ui()    

    def debt_ui(self):
        g_box = QtWidgets.QGridLayout()

        self.total_balance = QtWidgets.QLabel("Toplam")
        self.checking_account = QtWidgets.QLabel("Vadesiz Hesap")
        self.deposit_account = QtWidgets.QLabel("Vadeli Hesap")
        self.total_balance_amount = QtWidgets.QLabel("143,18TL")
        self.checking_account_amount = QtWidgets.QLabel("0,00TL")
        self.deposit_account_amount = QtWidgets.QLabel("0,00TL")

        g_box.addWidget(self.total_balance,0,0)
        g_box.addWidget(self.checking_account,1,0)
        g_box.addWidget(self.deposit_account,2,0)
        g_box.addWidget(self.total_balance_amount,0,1)
        g_box.addWidget(self.checking_account_amount,1,1)
        g_box.addWidget(self.deposit_account_amount,2,1)

        self.setLayout(g_box)

class Tab_currency(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.currency_ui()    

    def currency_ui(self):
        pass



if __name__ == '__main__':


    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())


























