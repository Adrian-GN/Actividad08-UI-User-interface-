from .algoritmo import distancia_euclidiana
class Particula:
    def __init__(self, id,x_1, y_1, x_2, y_2, velocidad,red,green,blue):
        self.__id = id
        self.__origen_x = x_1
        self.__origen_y = y_1
        self.__destino_x = x_2
        self.__destino_y = y_2
        self.__velocidad= velocidad
        self.__red= red
        self.__green= green
        self.__blue= blue
        self.__distancia= distancia_euclidiana(x_1,y_1, x_2, y_2)
    def __str__(self):
        return(
            'id: ' + str(self.__id) + '\n' +
            'Origen en x: ' + str(self.__origen_x) + '\n' +
            'Origen en y: ' + str(self.__origen_y) + '\n' +
            'Destino en x: ' + str(self.__destino_x) + '\n' +
            'Destino en y: ' + str(self.__destino_y) + '\n' +
            'Velocidad: ' + str(self.__velocidad) + '\n' +
            'Red: ' + str(self.__red) + '\n' +
            'Green: ' + str(self.__green) + '\n' +
            'Blue: ' + str(self.__blue) + '\n' +
            'Distancia: ' + str(self.__distancia) + '\n'
        )