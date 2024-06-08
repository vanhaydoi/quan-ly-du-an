from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

from templates import mainUI


class OverviewView(QMainWindow):
    def __init__(self):
        super(OverviewView, self).__init__()
        uic.loadUi(mainUI, self)
