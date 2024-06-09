from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QWidget

from controllers.auth_controller import AuthController
from templates import loginUI
from utils import widget


class LoginView(QWidget):
    def __init__(self):
        super(LoginView, self).__init__()
        uic.loadUi(loginUI, self)
        self.authController = AuthController()

        self.login.clicked.connect(self.handleLogin)
        self.signup.clicked.connect(self.changeToSignUp)

    # Xử lý khi ấn vào đăng ký
    def changeToSignUp(self):
        widget.setCurrentIndex(1)

    # Xử lý đăng nhập
    def handleLogin(self):
        username = self.userName.text()
        password = self.passWord.text()

        result = self.authController.login(username, password)

        # Kiểm tra đăng nhập
        if result:
            with open("current_user.txt", "w") as f:
                f.write(str(result.id))
            QMessageBox.information(self, "Login output", "Login succsess")
            widget.setCurrentIndex(2)
        else:
            QMessageBox.information(self, "Login output", "Login fail")
