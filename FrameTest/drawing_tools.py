from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QPen

class DrawingTools:
    def __init__(self):
        self.walls = []
        self.windows = []
        self.doors = []
        self.dimensions = []
        self.posts = []
        self.drawing = False
        self.lastPoint = QPoint()
        self.currentTool = None

    def setWallTool(self):
        self.currentTool = 'wall'
        print("Herramienta de muro seleccionada")

    def setWindowTool(self):
        self.currentTool = 'window'
        print("Herramienta de ventana seleccionada")

    def setDoorTool(self):
        self.currentTool = 'door'
        print("Herramienta de puerta seleccionada")

    def setDimensionTool(self):
        self.currentTool = 'dimension'
        print("Herramienta de dimensión seleccionada")

    def setPostTool(self):
        self.currentTool = 'post'
        print("Herramienta de poste seleccionada")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.drawing:
            self.drawing = False
            endPoint = event.pos()
            if self.currentTool == 'wall':
                self.walls.append((self.lastPoint, endPoint))
            elif self.currentTool == 'window':
                self.windows.append(QRect(self.lastPoint, endPoint).normalized())
            elif self.currentTool == 'door':
                self.doors.append(QRect(self.lastPoint, endPoint).normalized())
            elif self.currentTool == 'dimension':
                self.dimensions.append((self.lastPoint, endPoint))
            elif self.currentTool == 'post':
                self.posts.append(self.lastPoint)

    def paintEvent(self, event, parent):
        painter = QPainter(parent)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw walls
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        for wall in self.walls:
            painter.drawLine(wall[0], wall[1])

        # Draw windows
        painter.setPen(QPen(Qt.blue, 2, Qt.SolidLine))
        for window in self.windows:
            painter.drawRect(window)

        # Draw doors
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        for door in self.doors:
            painter.drawArc(door, 0, 90 * 16)

        # Draw dimensions
        painter.setPen(QPen(Qt.green, 1, Qt.DashLine))
        for dim in self.dimensions:
            painter.drawLine(dim[0], dim[1])

        # Draw posts
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        for post in self.posts:
            painter.drawEllipse(post, 5, 5)
            