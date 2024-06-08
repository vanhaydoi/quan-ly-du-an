from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

from templates import employeeUI


class EmployeeView(QMainWindow):
    def __init__(self):
        super(EmployeeView, self).__init__()
        uic.loadUi(employeeUI, self)
