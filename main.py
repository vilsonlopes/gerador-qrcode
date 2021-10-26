from design_gui.designgui import *


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gerarqr = GeradorQr()
    gerarqr.show()
    qt.exec()
