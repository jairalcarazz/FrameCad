from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import Qt
from ui_components import UIComponents
from drawing_tools import DrawingTools
from file_operations import FileOperations

class CADapp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.drawing_tools = DrawingTools()
        self.file_ops = FileOperations(self)

    def initUI(self):
        self.setWindowTitle('FramerCad')
        self.setGeometry(100, 100, 1000, 800)

        self.ui_components = UIComponents(self)
        self.ui_components.createMenus()
        self.ui_components.createToolbar()

        # Main drawing area
        self.drawingArea = QWidget()
        self.setCentralWidget(self.drawingArea)

    def mousePressEvent(self, event):
        self.drawing_tools.mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.drawing_tools.mouseReleaseEvent(event)

    def paintEvent(self, event):
        self.drawing_tools.paintEvent(event, self)

# This ensures CADApp is available when importing from this module
if __name__ == '__main__':
    print("CADApp is available for import")