from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

from controllers.task_controller import TaskController
from templates import taskUI
from utils import widget


class TaskView(QMainWindow):
    def __init__(self, project_id=None):
        super(TaskView, self).__init__()
        uic.loadUi(taskUI, self)
        self.project_id = project_id
        self.taskController = TaskController()

        self.Button_tim_kiem_2.clicked.connect(self.handleSearchTask)
        self.add_cong_viec.clicked.connect(self.handleCreateTask)
        self.table_Cong_viec.itemChanged.connect(self.handleEditTask)
        self.back_2.clicked.connect(self.handleBackToHome)
        self.delete_cong_viec.clicked.connect(self.handleDeleteTask)
        self.Cong_viec.clicked.connect(self.handleChangeToEmployeeView)

        self.handleSearchTask()

    def setProjectId(self, project_id: int):
        self.project_id = project_id

    def handleSearchTask(self):
        keyword = self.get_cong_viec.text()

        tasks = self.taskController.search(keyword, self.project_id)
        for task in tasks:
            self.table_Cong_viec.insertRow(self.table_Cong_viec.rowCount())
            self.table_Cong_viec.setItem(
                self.table_Cong_viec.rowCount() - 1, 0, QTableWidgetItem(str(task.id))
            )
            self.table_Cong_viec.setItem(
                self.table_Cong_viec.rowCount() - 1, 1, QTableWidgetItem(task.name)
            )
            self.table_Cong_viec.setItem(
                self.table_Cong_viec.rowCount() - 1,
                2,
                QTableWidgetItem(task.description),
            )
            self.table_Cong_viec.setItem(
                self.table_Cong_viec.rowCount() - 1,
                3,
                QTableWidgetItem(str(task.status).split(".")[1]),
            )
            self.table_Cong_viec.setItem(
                self.table_Cong_viec.rowCount() - 1,
                4,
                QTableWidgetItem(task.start_date.strftime("%Y-%m-%d %H:%M:%S")),
            )
            self.table_Cong_viec.setItem(
                self.table_Cong_viec.rowCount() - 1,
                5,
                QTableWidgetItem(task.end_date.strftime("%Y-%m-%d %H:%M:%S")),
            )

    def handleCreateTask(self):
        userId = int(self.get_add_manv.text())
        taskName = self.get_tennv_2.text()

        description = self.description.toPlainText()
        status = self.status.currentText()

        if status == "Not Started":
            status = "NOT_STARTED"
        start_date = self.get_add_start_date.dateTime().toPyDateTime()
        end_date = self.get_add_end_date_.dateTime().toPyDateTime()

        task = self.taskController.create(
            taskName,
            description,
            status,
            start_date,
            end_date,
            self.project_id,
            userId,
        )

        if task:
            QMessageBox.information(self, "Success", "Create task successfully")
            self.handleSearchTask()
        else:
            QMessageBox.critical(self, "Error", "Create task failed")

    def handleBackToHome(self):
        widget.setCurrentIndex(2)

    def handleEditTask(self, item: QTableWidgetItem):
        self.table_Cong_viec.blockSignals(True)
        try:
            row = item.row()
            column = item.column()
            value = item.text()
            if self.table_Cong_viec.item(row, 5) is not None:
                task_id = self.table_Cong_viec.item(row, 0).text()
                task_name = self.table_Cong_viec.item(row, 1).text()
                description = self.table_Cong_viec.item(row, 2).text()
                status = self.table_Cong_viec.item(row, 3).text()
                start_date = self.table_Cong_viec.item(row, 4).text()
                end_date = self.table_Cong_viec.item(row, 5).text()

                if column == 1:
                    task_name = value
                elif column == 2:
                    description = value
                elif column == 3:
                    status = value
                elif column == 4:
                    start_date = value
                elif column == 5:
                    end_date = value

                task = self.taskController.edit(
                    task_id, task_name, description, status, start_date, end_date
                )

                if task:
                    QMessageBox.information(self, "Success", "Edit task successfully")
                else:
                    QMessageBox.critical(self, "Error", "Edit task failed")
            else:
                print("Invalid column count")

        finally:
            self.table_Cong_viec.blockSignals(False)

    def handleDeleteTask(self):
        selected_items = self.table_Cong_viec.selectedItems()
        if selected_items:
            # Get the row of the first selected item
            selected_row = selected_items[0].row()
            self.taskController.delete(
                int(self.table_Cong_viec.item(selected_row, 0).text())
            )
            self.table_Cong_viec.removeRow(selected_row)
            QMessageBox.information(
                self, "Success", f"Row {selected_row + 1} deleted successfully"
            )
        else:
            QMessageBox.warning(self, "No selection", "No row selected to delete")

    def handleChangeToEmployeeView(self):
        widget.setCurrentIndex(3)
