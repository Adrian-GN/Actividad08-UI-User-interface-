from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from User_interface import Ui_MainWindow
from Particulas.admparticulas import Particulas
from Particulas.Act9 import Particula
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.particulas = Particulas()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Agregar_Final_pushButton.clicked.connect(self.click_agregar)
        self.ui.Agregar_Inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.Mostrar_pushButton.clicked.connect(self.click_mostar)
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
    @Slot()
    def action_abrir_archivo(self):
        #print('abrir_archivo')
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrio el archivo" + ubicacion
            )
        else:QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion)
    @Slot()
    def action_guardar_archivo(self):
        #print('guardar_archivo')
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo" + ubicacion
            )

    @Slot()
    def click_mostar(self):
        #self.particulas.mostrar()
        self.ui.Salida.insertPlainText(str(self.particulas))

    @Slot()
    def click_agregar(self):
        id = self.ui.ID_lineEdit.text()
        OX = self.ui.Origen_x_spinBox.value()
        OY = self.ui.Origen_y_spinBox.value()
        DX = self.ui.Destino_x_spinBox.value()
        DY = self.ui.Destino_y_spinBox.value()
        velocidad = self.ui.Velocidad_lineEdit.text()
        red = self.ui.Red_spinBox.value()
        green = self.ui.Green_spinBox.value()
        blue = self.ui.Blue_spinBox.value()

        particula = Particula(id,OX,OY,DX,DY,velocidad,red,green,blue)
        self.particulas.agregar_final(particula)


    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.ID_lineEdit.text()
        OX = self.ui.Origen_x_spinBox.value()
        OY = self.ui.Origen_y_spinBox.value()
        DX = self.ui.Destino_x_spinBox.value()
        DY = self.ui.Destino_y_spinBox.value()
        velocidad = self.ui.Velocidad_lineEdit.text()
        red = self.ui.Red_spinBox.value()
        green = self.ui.Green_spinBox.value()
        blue = self.ui.Blue_spinBox.value()

        particula = Particula(id,OX,OY,DX,DY,velocidad,red,green,blue)
        self.particulas.agregar_inicio(particula)
