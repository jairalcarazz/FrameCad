import sys
from PyQt5.QtWidgets import QApplication
from cad_app import Cadapp, Cadapp

def main():
    app = QApplication(sys.argv)
    ex = CADapp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()