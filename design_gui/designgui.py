import sys

import qrcod
from design_gui.designqr import *
from PyQt6.QtWidgets import QMainWindow, QApplication
from qrcod import gerar_qrcode


class GeradorQr(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        #self.inputQr.setText()
        self.btnGerar.clicked.connect(gerar_qrcode)
