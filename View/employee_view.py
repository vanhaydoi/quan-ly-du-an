from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem

from templates import employeeUI
from controllers.project_controller import ProjectController
from utils import widget


class EmployeeView(QMainWindow):
    def __init__(self):
        super(EmployeeView, self).__init__()
        uic.loadUi(employeeUI, self)

        self.projectController = ProjectController()

        self.Button_tim_kiem_1.clicked.connect(self.handleSearchStaff)
        self.back_1.clicked.connect(self.handleBackToHome)
        self.Cong_viec.clicked.connect(self.changeToQLNV)

        self.handleSearchStaff()

    
    def handleSearchStaff(self):
        keyword = self.get_nhan_vien.text()

        staffs = self.projectController.search_staff(keyword)

        self.table_Nhan_Vien.clear()
        for staff in staffs:
            self.table_Nhan_Vien.insertRow(self.table_Nhan_Vien.rowCount())
            self.table_Nhan_Vien.setItem(
                self.table_Nhan_Vien.rowCount() - 1, 0, QTableWidgetItem(str(staff.id))
            )
            self.table_Nhan_Vien.setItem(
                self.table_Nhan_Vien.rowCount() - 1, 1, QTableWidgetItem(str(staff.email))
            )
            self.table_Nhan_Vien.setItem(
                self.table_Nhan_Vien.rowCount() - 1, 2, QTableWidgetItem("Quản lý " if staff.is_manager else "Nhân viên")
            )

    def handleBackToHome(self):
        widget.setCurrentIndex(2)

    def changeToQLNV(self):
        widget.setCurrentIndex(4)
