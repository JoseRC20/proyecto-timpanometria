import numpy as np

def datos_prueba():
    compliancia_estatica = float(input("Compliance: "))
    presion = int(input("Presion: "))
    gradiente = int(input("Gradiente: "))
    return compliancia_estatica, presion, gradiente


def preparar_datos(compliancia_estatica, presion, gradiente):
    mitad_compliance = compliancia_estatica / 2
    mitad_gradiente = round(gradiente / 2)
    
    ancho_1 = presion + mitad_gradiente
    ancho_2 = presion - mitad_gradiente
    
    return mitad_compliance, ancho_1, ancho_2


def crear_coordenadas(presion, compliancia_estatica, mitad_compliance, ancho_1, ancho_2):
    Punto_1 = np.array([presion, compliancia_estatica])
    Punto_2 = np.array([ancho_1, mitad_compliance])
    Punto_3 = np.array([ancho_2, mitad_compliance])
    
    return Punto_1, Punto_2, Punto_3
