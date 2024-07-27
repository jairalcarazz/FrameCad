import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QMessageBox, QToolBar, QWidget
from PyQt5.QtGui import QPainter, QPen, QIcon
from PyQt5.QtCore import Qt, QPoint, QRect

class CADApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.walls = []
        self.windows = []
        self.doors = []
        self.dimensions = []
        self.posts = []
        self.drawing = False
        self.lastPoint = QPoint()
        self.currentFile = None
        self.currentTool = None

    def initUI(self):
        self.setWindowTitle('CAD para Dibujo Rápido de Paredes')
        self.setGeometry(100, 100, 1000, 800)

        self.createMenus()
        self.createToolbar()

        # Área principal de dibujo
        self.drawingArea = QWidget()
        self.setCentralWidget(self.drawingArea)

    def createMenus(self):
        menubar = self.menuBar()

        # Menú Archivo
        fileMenu = menubar.addMenu('Archivo')
        fileMenu.addAction(self.createAction('Nuevo', self.newFile, 'Ctrl+N'))
        fileMenu.addAction(self.createAction('Guardar', self.saveFile, 'Ctrl+S'))
        fileMenu.addAction(self.createAction('Guardar como', self.saveFileAs, 'Ctrl+Shift+S'))
        fileMenu.addAction(self.createAction('Cargar', self.loadFile, 'Ctrl+O'))

        # Menú Modelar
        modelMenu = menubar.addMenu('Modelar')
        modelMenu.addAction(self.createAction('Mostrar herramientas', self.toggleToolbar, 'Ctrl+T'))

        # Menú Exportar
        exportMenu = menubar.addMenu('Exportar')
        exportMenu.addAction(self.createAction('Exportar como PNG', self.exportPNG))

        # Menú Ayuda
        helpMenu = menubar.addMenu('Ayuda')
        helpMenu.addAction(self.createAction('Acerca de', self.showAbout))

    def createAction(self, text, slot, shortcut=None):
        action = QAction(text, self)
        action.triggered.connect(slot)
        if shortcut:
            action.setShortcut(shortcut)
        return action

    def createToolbar(self):
        self.toolbar = QToolBar()
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)
        self.toolbar.setMovable(False)
        self.toolbar.setFloatable(False)

        current_dir = os.path.dirname(os.path.abspath(__file__))

        self.toolbar.addAction(self.createToolAction('Muro', self.setWallTool, os.path.join(current_dir, 'muro.png')))
        self.toolbar.addAction(self.createToolAction('Ventana', self.setWindowTool, os.path.join(current_dir, 'ventana.png')))
        self.toolbar.addAction(self.createToolAction('Puerta', self.setDoorTool, os.path.join(current_dir, 'puerta.png')))
        self.toolbar.addAction(self.createToolAction('Dimensión', self.setDimensionTool, os.path.join(current_dir, 'dimension.png')))
        self.toolbar.addAction(self.createToolAction('Poste', self.setPostTool, os.path.join(current_dir, 'poste.png')))

        self.toolbar.hide()  # Ocultar la barra de herramientas inicialmente

    def createToolAction(self, text, slot, icon_path):
        action = QAction(QIcon(icon_path), text, self)
        action.triggered.connect(slot)
        return action

    def toggleToolbar(self):
        if self.toolbar.isVisible():
            self.toolbar.hide()
        else:
            self.toolbar.show()

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

    def newFile(self):
        self.walls = []
        self.windows = []
        self.doors = []
        self.dimensions = []
        self.posts = []
        self.currentFile = None
        self.update()
        print("Nuevo archivo creado")

    def saveFile(self):
        if self.currentFile:
            self.saveToFile(self.currentFile)
        else:
            self.saveFileAs()

    def saveFileAs(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo", "", "Archivos RCAD (*.rcad)")
        if fileName:
            if not fileName.endswith('.rcad'):
                fileName += '.rcad'
            self.saveToFile(fileName)
            self.currentFile = fileName

    def saveToFile(self, fileName):
        with open(fileName, 'w') as file:
            # Aquí deberías implementar la lógica para guardar todos los elementos
            # Por ahora, solo guardaremos las paredes como ejemplo
            for wall in self.walls:
                file.write(f"wall,{wall[0].x()},{wall[0].y()},{wall[1].x()},{wall[1].y()}\n")
        print(f"Archivo guardado como {fileName}")

    def loadFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Cargar Archivo", "", "Archivos RCAD (*.rcad)")
        if fileName:
            self.loadFromFile(fileName)
            self.currentFile = fileName

    def loadFromFile(self, fileName):
        self.walls = []
        self.windows = []
        self.doors = []
        self.dimensions = []
        self.posts = []
        with open(fileName, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if parts[0] == 'wall':
                    self.walls.append((QPoint(int(parts[1]), int(parts[2])), QPoint(int(parts[3]), int(parts[4]))))
        self.update()
        print(f"Archivo cargado: {fileName}")

    def exportPNG(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Exportar como PNG", "", "Imágenes PNG (*.png)")
        if fileName:
            if not fileName.endswith('.png'):
                fileName += '.png'
            # Aquí deberías implementar la lógica para exportar el dibujo como PNG
            print(f"Exportado como PNG: {fileName}")

    def showAbout(self):
        QMessageBox.about(self, "Acerca de", "CAD para Dibujo Rápido de Paredes\nVersión 1.0\n© 2024")

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
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Dibujar muros
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        for wall in self.walls:
            painter.drawLine(wall[0], wall[1])

        # Dibujar ventanas
        painter.setPen(QPen(Qt.blue, 2, Qt.SolidLine))
        for window in self.windows:
            painter.drawRect(window)

        # Dibujar puertas
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        for door in self.doors:
            painter.drawArc(door, 0, 90 * 16)

        # Dibujar dimensiones
        painter.setPen(QPen(Qt.green, 1, Qt.DashLine))
        for dim in self.dimensions:
            painter.drawLine(dim[0], dim[1])

        # Dibujar postes
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        for post in self.posts:
            painter.drawEllipse(post, 5, 5)

def main():
    app = QApplication(sys.argv)
    ex = CADApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()