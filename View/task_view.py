from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

from templates import taskUI


class TaskView(QMainWindow):
    def __init__(self):
        super(TaskView, self).__init__()
        uic.loadUi(taskUI, self)
