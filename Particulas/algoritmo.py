import math

def distancia_euclidiana(origen_x, origen_y, destino_x, destino_y):
    distan = math.sqrt((origen_x-origen_y)**2+(destino_x-destino_y)**2)
    return distan