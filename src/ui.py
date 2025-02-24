# UI Panel
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import maya.cmds as cmds
from version_control import save_new_version, load_last_version
from review_system import add_comment

def get_maya_main_window():
    """Get the Maya main window as a PySide2 object."""
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QMainWindow)

class VersionControlUI(QtWidgets.QDialog):
    def __init__(self, parent=get_maya_main_window()):
        super(VersionControlUI, self).__init__(parent)
        self.setWindowTitle("Maya Version Control")
        self.setMinimumWidth(300)

        self.layout = QtWidgets.QVBoxLayout(self)

        # Version Control Buttons
        self.version_label = QtWidgets.QLabel("Current Version: 1.0")
        self.layout.addWidget(self.version_label)

        self.save_button = QtWidgets.QPushButton("Save New Version")
        self.layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.save_version)

        self.load_button = QtWidgets.QPushButton("Load Previous Version")
        self.layout.addWidget(self.load_button)
        self.load_button.clicked.connect(self.load_version)

        # Review System (Comments)
        self.comment_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.comment_input)

        self.comment_button = QtWidgets.QPushButton("Add Comment")
        self.layout.addWidget(self.comment_button)
        self.comment_button.clicked.connect(self.add_comment)

    def save_version(self):
        versioned_file = save_new_version()
        cmds.confirmDialog(title="Save", message=f"Saved: {versioned_file}")

    def load_version(self):
        load_last_version()

    def add_comment(self):
        obj = cmds.ls(selection=True)
        if obj:
            add_comment(self.comment_input.text(), obj[0])
            cmds.confirmDialog(title="Comment", message="Comment added!")
        else:
            cmds.confirmDialog(title="Error", message="No object selected!")
