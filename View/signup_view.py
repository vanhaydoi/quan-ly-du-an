from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from templates import signupUI


class SignUpView(QWidget):
    def __init__(self):
        super(SignUpView, self).__init__()
        uic.loadUi(signupUI, self)
