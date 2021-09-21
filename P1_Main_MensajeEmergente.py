import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P1_MensajeEmergente.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.Btn.clicked.connect(self.saludar)

    # Área de los Slots
    def saludar(self):
        print("Hiciste click")
        self.mensaje("Saludos")

    def mensaje(selfself,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())