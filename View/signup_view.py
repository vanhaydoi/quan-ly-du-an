from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QWidget

from controllers.auth_controller import AuthController
from templates import signupUI
from utils import widget


class SignUpView(QWidget):
    def __init__(self):
        super(SignUpView, self).__init__()
        uic.loadUi(signupUI, self)

        self.authController = AuthController()

        self.signup1.clicked.connect(self.handleSignUp)

    def handleSignUp(self):
        username = self.userName.text()
        password = self.passWord.text()
        email = self.EnterPassword.text()

        print(username, password, email)

        result = self.authController.register(username, password, email)

        if result:
            QMessageBox.information(self, "Sign up output", "Sign up succsess")
            widget.setCurrentIndex(0)
        else:
            QMessageBox.information(self, "Sign up output", "Sign up fail")
