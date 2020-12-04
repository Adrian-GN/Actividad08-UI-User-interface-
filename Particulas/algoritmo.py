import math

def distancia_euclidiana(origen_x, origen_y, destino_x, destino_y):
    distan = math.sqrt((origen_y-origen_x)**2+(destino_y-destino_x)**2)
    return distan