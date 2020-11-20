# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'User_Interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(772, 577)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Agregar = QTabWidget(self.centralwidget)
        self.Agregar.setObjectName(u"Agregar")
        self.Agregar.setGeometry(QRect(10, 0, 751, 541))
        self.Tab = QWidget()
        self.Tab.setObjectName(u"Tab")
        self.Salida = QPlainTextEdit(self.Tab)
        self.Salida.setObjectName(u"Salida")
        self.Salida.setGeometry(QRect(470, 10, 261, 481))
        self.groupBox_2 = QGroupBox(self.Tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 0, 461, 491))
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.ID_lineEdit = QLineEdit(self.groupBox_2)
        self.ID_lineEdit.setObjectName(u"ID_lineEdit")

        self.gridLayout.addWidget(self.ID_lineEdit, 0, 1, 1, 1)

        self.Id_label = QLabel(self.groupBox_2)
        self.Id_label.setObjectName(u"Id_label")

        self.gridLayout.addWidget(self.Id_label, 0, 0, 1, 1)

        self.Origen_y_spinBox = QSpinBox(self.groupBox_2)
        self.Origen_y_spinBox.setObjectName(u"Origen_y_spinBox")
        self.Origen_y_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.Origen_y_spinBox, 2, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.Destino_y_spinBox = QSpinBox(self.groupBox_2)
        self.Destino_y_spinBox.setObjectName(u"Destino_y_spinBox")
        self.Destino_y_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.Destino_y_spinBox, 4, 1, 1, 1)

        self.Destino_x_spinBox = QSpinBox(self.groupBox_2)
        self.Destino_x_spinBox.setObjectName(u"Destino_x_spinBox")
        self.Destino_x_spinBox.setMaximumSize(QSize(42, 22))
        self.Destino_x_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.Destino_x_spinBox, 3, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.Origen_x_spinBox = QSpinBox(self.groupBox_2)
        self.Origen_x_spinBox.setObjectName(u"Origen_x_spinBox")
        self.Origen_x_spinBox.setMinimumSize(QSize(42, 22))
        self.Origen_x_spinBox.setMaximumSize(QSize(42, 22))
        self.Origen_x_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.Origen_x_spinBox, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.Velocidad_spinBox = QSpinBox(self.groupBox_2)
        self.Velocidad_spinBox.setObjectName(u"Velocidad_spinBox")
        self.Velocidad_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.Velocidad_spinBox, 5, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.Color_RGB = QGroupBox(self.groupBox_2)
        self.Color_RGB.setObjectName(u"Color_RGB")
        self.gridLayout_2 = QGridLayout(self.Color_RGB)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(self.Color_RGB)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_8 = QLabel(self.Color_RGB)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.Green_spinBox = QSpinBox(self.Color_RGB)
        self.Green_spinBox.setObjectName(u"Green_spinBox")
        self.Green_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.Green_spinBox, 1, 1, 1, 1)

        self.Red_spinBox = QSpinBox(self.Color_RGB)
        self.Red_spinBox.setObjectName(u"Red_spinBox")
        self.Red_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.Red_spinBox, 0, 1, 1, 1)

        self.label_7 = QLabel(self.Color_RGB)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.Blue_spinBox = QSpinBox(self.Color_RGB)
        self.Blue_spinBox.setObjectName(u"Blue_spinBox")
        self.Blue_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.Blue_spinBox, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.Color_RGB, 1, 0, 1, 1)

        self.Agregar_Final_pushButton = QPushButton(self.groupBox_2)
        self.Agregar_Final_pushButton.setObjectName(u"Agregar_Final_pushButton")

        self.gridLayout_4.addWidget(self.Agregar_Final_pushButton, 2, 0, 1, 1)

        self.Agregar_Inicio_pushButton = QPushButton(self.groupBox_2)
        self.Agregar_Inicio_pushButton.setObjectName(u"Agregar_Inicio_pushButton")

        self.gridLayout_4.addWidget(self.Agregar_Inicio_pushButton, 3, 0, 1, 1)

        self.Mostrar_pushButton = QPushButton(self.groupBox_2)
        self.Mostrar_pushButton.setObjectName(u"Mostrar_pushButton")

        self.gridLayout_4.addWidget(self.Mostrar_pushButton, 4, 0, 1, 1)

        self.Agregar.addTab(self.Tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_3.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.Mostrar_tabla_pushButton_2 = QPushButton(self.tab_2)
        self.Mostrar_tabla_pushButton_2.setObjectName(u"Mostrar_tabla_pushButton_2")

        self.gridLayout_3.addWidget(self.Mostrar_tabla_pushButton_2, 1, 2, 1, 1)

        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_3.addWidget(self.tabla, 0, 0, 1, 3)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_3.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.Agregar.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_9 = QGridLayout(self.tab_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_9.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar_pushButton = QPushButton(self.tab_3)
        self.dibujar_pushButton.setObjectName(u"dibujar_pushButton")

        self.gridLayout_9.addWidget(self.dibujar_pushButton, 1, 0, 1, 1)

        self.limpiar_pushButton = QPushButton(self.tab_3)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")

        self.gridLayout_9.addWidget(self.limpiar_pushButton, 1, 1, 1, 1)

        self.Agregar.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 772, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.Agregar.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.Id_label.setText(QCoreApplication.translate("MainWindow", u"ID: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en x:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino y:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen en y:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino x:", None))
        self.Color_RGB.setTitle(QCoreApplication.translate("MainWindow", u"Color (rgb):", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.Agregar_Final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al Final", None))
        self.Agregar_Inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al Inicio", None))
        self.Mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.Agregar.setTabText(self.Agregar.indexOf(self.Tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Mostrar_tabla_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Titulo del libro", None))
        self.Agregar.setTabText(self.Agregar.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.Agregar.setTabText(self.Agregar.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujo", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi