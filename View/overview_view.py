from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox

from controllers.project_controller import ProjectController
from templates import mainUI
from utils import widget


class OverviewView(QMainWindow):
    def __init__(self):
        super(OverviewView, self).__init__()
        uic.loadUi(mainUI, self)

        self.projectController = ProjectController()

        self.Tim_kiem.clicked.connect(self.handleSearchProject)
        self.pushButton.clicked.connect(self.handleCreateProject)
        self.Hien_thi_du_an.itemClicked.connect(self.handleSelectProject)

        self.handleSearchProject()

    def handleSearchProject(self):
        keyword = self.Ten_Du_An.text()

        projects = self.projectController.search(keyword)

        self.Hien_thi_du_an.clear()
        for project in projects:
            self.Hien_thi_du_an.addItem(
                f"{project.id} | {project.name} | {project.description}"
            )

        self.Hien_thi_du_an.show()

    def handleCreateProject(self):
        name = self.lineEdit_2.text()
        description = self.get_ghi_chu_1.text()
        user_id = int(open("current_user.txt", "r").read())
        print(name, description, user_id)

        project = self.projectController.create(name, description, user_id)

        if project:
            self.handleSearchProject()
            QMessageBox.information(
                self, "Create project output", "Create project success"
            )
        else:
            QMessageBox.information(
                self, "Create project output", "Create project fail"
            )

    def handleSelectProject(self, item):
        id = int(item.text().split(" | ")[0])
        print(id)
        from View.task_view import TaskView

        abc = TaskView(id)
        abc.setProjectId(id)
        widget.setCurrentIndex(4)
        widget.removeWidget(widget.currentWidget())
        widget.addWidget(abc)
        widget.setCurrentIndex(4)
