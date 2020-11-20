from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from User_interface import Ui_MainWindow
from Particulas.admparticulas import Particulas
from Particulas.Act9 import Particula
from PySide2.QtGui import QPen, QColor, QTransform
from random import randint
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
        self.ui.Mostrar_tabla_pushButton_2.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)
        self.ui.dibujar_pushButton.clicked.connect(self.dibujar)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar)
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
    def wheelEvent(self, event):
        if event.delta > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)
        for Particula in self.particulas:
            r= Particula.red
            g= Particula.green
            b= Particula.blue
            color = QColor(r,g,b)
            pen.setColor(color)
            self.scene.addEllipse(Particula.ox,Particula.oy, 3, 3,pen) 
            self.scene.addEllipse(Particula.dx,Particula.dy, 3, 3,pen) 
            self.scene.addLine(Particula.ox+3,Particula.oy+3, Particula.dx,Particula.dy,pen)
    @Slot()
    def limpiar(self):
        self.scene.clear()
    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()
        encontrado = False
        for Particula in self.particulas:
            if id == Particula.id:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)
            id_widget = QTableWidgetItem(str(Particula.id))
            ox_widget = QTableWidgetItem(str(Particula.ox))
            oy_widget = QTableWidgetItem(str(Particula.oy))
            dx_widget = QTableWidgetItem(str(Particula.dx))
            dy_widget = QTableWidgetItem(str(Particula.dy))
            velocidad_widget = QTableWidgetItem(str(Particula.velocidad))
            red_widget = QTableWidgetItem(str(Particula.red))
            green_widget = QTableWidgetItem(str(Particula.green))
            blue_widget = QTableWidgetItem(str(Particula.blue))
            distancia_widget = QTableWidgetItem(str(Particula.distancia))
            self.ui.tabla.setItem(0, 0, id_widget)
            self.ui.tabla.setItem(0, 1, ox_widget)
            self.ui.tabla.setItem(0, 2, oy_widget)
            self.ui.tabla.setItem(0, 3, dx_widget)
            self.ui.tabla.setItem(0, 4, dy_widget)
            self.ui.tabla.setItem(0, 5, velocidad_widget)
            self.ui.tabla.setItem(0, 6, red_widget)
            self.ui.tabla.setItem(0, 7, green_widget)
            self.ui.tabla.setItem(0, 8, blue_widget)
            self.ui.tabla.setItem(0, 9, distancia_widget)
            encontrado = True
            return
            if not encontrado:
                QMessageBox.warning(
                self,
                "Atencion", 
                f'La particula con el id "{id}" no fue encontrado'
                )
            
    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)    
        headers = ["Id","Origen en x", "Origen en y", "Destino en x", "Destino en y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.particulas))
        row = 0
        for Particula in self.particulas:
            id_widget = QTableWidgetItem(str(Particula.id))
            ox_widget = QTableWidgetItem(str(Particula.ox))
            oy_widget = QTableWidgetItem(str(Particula.oy))
            dx_widget = QTableWidgetItem(str(Particula.dx))
            dy_widget = QTableWidgetItem(str(Particula.dy))
            velocidad_widget = QTableWidgetItem(str(Particula.velocidad))
            red_widget = QTableWidgetItem(str(Particula.red))
            green_widget = QTableWidgetItem(str(Particula.green))
            blue_widget = QTableWidgetItem(str(Particula.blue))
            distancia_widget = QTableWidgetItem(str(Particula.distancia))
            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, ox_widget)
            self.ui.tabla.setItem(row, 2, oy_widget)
            self.ui.tabla.setItem(row, 3, dx_widget)
            self.ui.tabla.setItem(row, 4, dy_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)
            row += 1
    
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
        velocidad = self.ui.Velocidad_spinBox.value()
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
        velocidad = self.ui.Velocidad_spinBox.value()
        red = self.ui.Red_spinBox.value()
        green = self.ui.Green_spinBox.value()
        blue = self.ui.Blue_spinBox.value()

        particula = Particula(id,OX,OY,DX,DY,velocidad,red,green,blue)
        self.particulas.agregar_inicio(particula)
