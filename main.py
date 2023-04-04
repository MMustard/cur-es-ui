import sys
from ui import Ui_platform
from PyQt5 import QtCore, QtGui, QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    platform = Ui_platform()
    platform.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
