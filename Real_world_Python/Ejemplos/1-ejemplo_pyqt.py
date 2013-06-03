from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
 
class Controles(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args)
 
        contenedor = QVBoxLayout()
        self.setLayout(contenedor)
 
        label = QLabel("Texto: ")
        contenedor.addWidget(label)
 
        self.qle_texto = QLineEdit()
        contenedor.addWidget(self.qle_texto)
 
        btnBorrar = QPushButton("Borrar",None)
        contenedor.addWidget(btnBorrar)
        self.connect(btnBorrar, SIGNAL("clicked()"), self.borrar)
 
        btnSalir = QPushButton("Salir",None)
        contenedor.addWidget(btnSalir)
        self.connect(btnSalir, SIGNAL("clicked()"), self.salir)
 
    def borrar(self):
        self.qle_texto.setText("")
 
    def salir(self):
        exit()
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    controles = Controles()
    controles.show()
    sys.exit(app.exec_())