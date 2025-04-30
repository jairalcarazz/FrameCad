from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QPoint, QRect

class FileOperations:
    def __init__(self, parent):
        self.parent = parent
        self.currentFile = None

    def newFile(self):
        self.parent.drawing_tools.walls = []
        self.parent.drawing_tools.windows = []
        self.parent.drawing_tools.doors = []
        self.parent.drawing_tools.dimensions = []
        self.parent.drawing_tools.posts = []
        self.currentFile = None
        self.parent.update()
        print("Nuevo archivo creado")

    def saveFile(self):
        if self.currentFile:
            self.saveToFile(self.currentFile)
        else:
            self.saveFileAs()

    def saveFileAs(self):
        fileName, _ = QFileDialog.getSaveFileName(self.parent, "Guardar Archivo", "", "Archivos RCAD (*.rcad)")
        if fileName:
            if not fileName.endswith('.rcad'):
                fileName += '.rcad'
            self.saveToFile(fileName)
            self.currentFile = fileName

    def saveToFile(self, fileName):
        with open(fileName, 'w') as file:
            # Here you should implement the logic to save all elements
            # For now, we'll just save the walls as an example
            for wall in self.parent.drawing_tools.walls:
                file.write(f"wall,{wall[0].x()},{wall[0].y()},{wall[1].x()},{wall[1].y()}\n")
        print(f"Archivo guardado como {fileName}")

    def loadFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self.parent, "Cargar Archivo", "", "Archivos RCAD (*.rcad)")
        if fileName:
            self.loadFromFile(fileName)
            self.currentFile = fileName

    def loadFromFile(self, fileName):
        self.parent.drawing_tools.walls = []
        self.parent.drawing_tools.windows = []
        self.parent.drawing_tools.doors = []
        self.parent.drawing_tools.dimensions = []
        self.parent.drawing_tools.posts = []
        with open(fileName, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if parts[0] == 'wall':
                    self.parent.drawing_tools.walls.append((QPoint(int(parts[1]), int(parts[2])), QPoint(int(parts[3]), int(parts[4]))))
        self.parent.update()
        print(f"Archivo cargado: {fileName}")

    def exportPNG(self):
        fileName, _ = QFileDialog.getSaveFileName(self.parent, "Exportar como PNG", "", "Imágenes PNG (*.png)")
        if fileName:
            if not fileName.endswith('.png'):
                fileName += '.png'
            # Here you should implement the logic to export the drawing as PNG
            print(f"Exportado como PNG: {fileName}")