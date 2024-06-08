import sys

from utils import app, widget
from View import EmployeeView_f, Login_f, Man_chinh_f, Signup_f, TaskView_f

# from Model.database import MySQLConnector


# Xử lý
if __name__ == "__main__":

    widget.addWidget(Login_f)
    widget.addWidget(Signup_f)
    widget.addWidget(Man_chinh_f)
    widget.addWidget(EmployeeView_f)
    widget.addWidget(TaskView_f)

    widget.setCurrentIndex(0)
    widget.setFixedHeight(820)
    widget.setFixedWidth(680)
    widget.show()
    sys.exit(app.exec())
