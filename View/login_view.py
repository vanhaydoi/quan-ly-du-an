from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from templates import loginUI


class LoginView(QWidget):
    def __init__(self):
        super(LoginView, self).__init__()
        uic.loadUi(loginUI, self)

    #     self.login.clicked.connect(self.login)

    # # Xử lý khi ấn vào đăng ký
    # def sign_up(self):
    #     widget.setCurrentIndex(1)

    # # Xử lý đăng nhập
    # def login(self):
    #     username = self.userName.text()
    #     password = self.passWord.text()

    #     # Kết nối tới mysql
    #     connector = MySQLConnector(
    #         host="localhost",
    #         port=3306,
    #         username="root",
    #         password="123456",
    #         database="qlda",
    #     )
    #     connector.connect()

    #     # Thực hiện câu lệnh sql
    #     query = f"SELECT * FROM qlda.user WHERE username = '{username}' and password ='{password}'"

    #     # Thực thi truy vấn SQL
    #     result = connector.execute_query(query)

    #     # Đóng kết nối với cơ sở dữ liệu MySQL
    #     connector.close_connection()
    #     # Kiểm tra đăng nhập
    #     if result:
    #         QMessageBox.information(self, "Login output", "Login succsess")
    #         widget.setCurrentIndex(2)
    #     else:
    #         QMessageBox.information(self, "Login output", "Login fail")
