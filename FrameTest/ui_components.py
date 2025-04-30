import os
from PyQt5.QtWidgets import QAction, QToolBar, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class UIComponents:
    def __init__(self, parent):
        self.parent = parent
        self.toolbar = None

    def createMenus(self):
        menubar = self.parent.menuBar()

        # File Menu
        fileMenu = menubar.addMenu('Archivo')
        fileMenu.addAction(self.createAction('Nuevo', self.parent.file_ops.newFile, 'Ctrl+N'))
        fileMenu.addAction(self.createAction('Guardar', self.parent.file_ops.saveFile, 'Ctrl+S'))
        fileMenu.addAction(self.createAction('Guardar como', self.parent.file_ops.saveFileAs, 'Ctrl+Shift+S'))
        fileMenu.addAction(self.createAction('Cargar', self.parent.file_ops.loadFile, 'Ctrl+O'))

        # Model Menu
        modelMenu = menubar.addMenu('Modelar')
        modelMenu.addAction(self.createAction('Mostrar herramientas', self.toggleToolbar, 'Ctrl+T'))

        # Export Menu
        exportMenu = menubar.addMenu('Exportar')
        exportMenu.addAction(self.createAction('Exportar como PNG', self.parent.file_ops.exportPNG))

        # Help Menu
        helpMenu = menubar.addMenu('Ayuda')
        helpMenu.addAction(self.createAction('Acerca de', self.showAbout))

    def createAction(self, text, slot, shortcut=None):
        action = QAction(text, self.parent)
        action.triggered.connect(slot)
        if shortcut:
            action.setShortcut(shortcut)
        return action

    def createToolbar(self):
        self.toolbar = QToolBar()
        self.parent.addToolBar(Qt.LeftToolBarArea, self.toolbar)
        self.toolbar.setMovable(False)
        self.toolbar.setFloatable(False)

        current_dir = os.path.dirname(os.path.abspath(__file__))

        self.toolbar.addAction(self.createToolAction('Muro', self.parent.drawing_tools.setWallTool, os.path.join(current_dir, 'muro.png')))
        self.toolbar.addAction(self.createToolAction('Ventana', self.parent.drawing_tools.setWindowTool, os.path.join(current_dir, 'ventana.png')))
        self.toolbar.addAction(self.createToolAction('Puerta', self.parent.drawing_tools.setDoorTool, os.path.join(current_dir, 'puerta.png')))
        self.toolbar.addAction(self.createToolAction('Dimensión', self.parent.drawing_tools.setDimensionTool, os.path.join(current_dir, 'dimension.png')))
        self.toolbar.addAction(self.createToolAction('Poste', self.parent.drawing_tools.setPostTool, os.path.join(current_dir, 'poste.png')))

        self.toolbar.hide()  # Initially hide the toolbar

    def createToolAction(self, text, slot, icon_path):
        action = QAction(QIcon(icon_path), text, self.parent)
        action.triggered.connect(slot)
        return action

    def toggleToolbar(self):
        if self.toolbar.isVisible():
            self.toolbar.hide()
        else:
            self.toolbar.show()

    def showAbout(self):
        QMessageBox.about(self.parent, "Acerca de", "CAD para Dibujo Rápido de Paredes\nVersión 1.0\n© 2024")