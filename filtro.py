#{}  []

from sys import argv

umbral = int(argv[1])
umbral2 = argv[2]

precios = {'Notebook': 700000,
           'Teclado': 25000,
           'Mouse': 12000,
           'Monitor': 250000,
           'Escritorio': 135000,
           'Tarjeta de Video': 1500000}

def filtrar(diccionario, umbral, umbral2):
    if umbral2 == "mayor":
        nombre = [k for k, v in diccionario.items() if v > umbral]
    elif umbral2 == "menor":
        nombre = [k for k, v in diccionario.items() if v < umbral]
    else:
        print("Lo sentimos, no es una operación válida'.")
        return []
    return nombre

filtro = filtrar(precios, umbral, umbral2)

print(f"Los productos {argv[2]} al umbral son: {filtro}")