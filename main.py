# Thư viện
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSlot
import sys
from Model.database import MySQLConnector

# Cửa số đăng nhập

class Login_w(QWidget):
    def __init__(self):
        super(Login_w, self).__init__()
        uic.loadUi('login.ui', self)

# Cửa sổ đăng ký

class Signup_w(QWidget):
    def __init__(self):
        super(Signup_w, self).__init__()
        uic.loadUi('signup.ui', self)



# Cửa số quản lý dự án

class Quan_ly_du_an(QMainWindow):
    def __init__(self):
        super(Quan_ly_du_an, self).__init__()
        uic.loadUi('Màn chính.ui', self)
        self.login.clicked.connect(self.login)


    # Xử lý khi ấn vào đăng ký
    def sign_up(self):
        widget.setCurrentIndex(1)

    # Xử lý đăng nhập
    def login(self):
        username = self.userName.text()
        password = self.passWord.text()

        # Kết nối tới mysql
        connector = MySQLConnector(host='localhost', port=3306, username='root', password='123456', database='qlda')
        connector.connect()

        # Thực hiện câu lệnh sql
        query = f"SELECT * FROM qlda.user WHERE username = '{username}' and password ='{password}'"
        
        # Thực thi truy vấn SQL
        result = connector.execute_query(query)
        
        # Đóng kết nối với cơ sở dữ liệu MySQL
        connector.close_connection()
        # Kiểm tra đăng nhập
        if result:
            QMessageBox.information(self, "Login output", "Login succsess")
            widget.setCurrentIndex(2)
        else:
            QMessageBox.information(self, "Login output", "Login fail")


# Cửa số để chọn Nhân viên hoặc Công việc

class Man_1(QMainWindow):
    def __init__(self):
        super(Man_1, self).__init__()
        uic.loadUi('Màn 1.ui', self)

# Cửa số quản lý nhân viên

class Man_2(QMainWindow):
    def __init__(self):
        super(Man_2, self).__init__()
        uic.loadUi('Màn 1.ui', self)

# Cửa số quản lý công việc

class Man_3(QMainWindow):
    def __init__(self):
        super(Man_3, self).__init__()
        uic.loadUi('Màn 1.ui', self)

# Xử lý
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    
    Login_f = Login_w()
    Signup_f = Signup_w()
    Man_chinh_f = Quan_ly_du_an()
    Man_1_f = Man_1()
    Man_2_f = Man_2()
    Man_3_f = Man_3()
    
    widget.addWidget(Login_f)
    widget.addWidget(Signup_f)
    widget.addWidget(Man_chinh_f)
    widget.addWidget(Man_1_f)
    widget.addWidget(Man_2_f)
    widget.addWidget(Man_3_f)
    
    widget.setCurrentIndex(0)
    widget.setFixedHeight(820)
    widget.setFixedWidth(680)
    widget.show()
    sys.exit(app.exec())