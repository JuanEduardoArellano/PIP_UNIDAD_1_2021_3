import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P4_Suma2Numeros.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)

    # Área de los Slots
    def sumar(self):

        num1 = self.txt_numero1.text()
        num2 = self.txt_numero2.text()

        if(num1 == ""):
            num1 = 0
        else:
            num1 = int(num1)

        if (num2 == ""):
            num2 = 0
        else:
            num2 = int(num2)

        result = str(num1 + num2)

        self.txt_resultado.setText(result)

    def mensaje(selfself,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())