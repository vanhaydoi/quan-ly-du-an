import sys

from utils import app, widget
from View.employee_view import EmployeeView

# from Model.database import MySQLConnector
from View.login_view import LoginView
from View.overview_view import OverviewView
from View.signup_view import SignUpView
from View.task_view import TaskView

# Xử lý
if __name__ == "__main__":
    Login_f = LoginView()
    Signup_f = SignUpView()
    Man_chinh_f = OverviewView()
    EmployeeView_f = EmployeeView()
    TaskView_f = TaskView()

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
