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
            'origen en x: ' + str(self.__origen_x) + '\n' +
            'origen en y: ' + str(self.__origen_y) + '\n' +
            'destino en x: ' + str(self.__destino_x) + '\n' +
            'destino en y: ' + str(self.__destino_y) + '\n' +
            'velocidad: ' + str(self.__velocidad) + '\n' +
            'red: ' + str(self.__red) + '\n' +
            'green: ' + str(self.__green) + '\n' +
            'blue: ' + str(self.__blue) + '\n' +
            'distancia: ' + str(self.__distancia) + '\n'
        )

    def to_dict(self):
        return {
            "id": self.__id,
            "origen_x": self.__origen_x,
            "origen_y": self.__origen_y,
            "destino_x": self.__destino_x,
            "destino_y": self.__destino_y,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue
        }