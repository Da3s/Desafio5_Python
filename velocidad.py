# Se calcula el promedio de las velocidades
def promedio_calculo(velocidades):
    total = sum(velocidades)
    promedio = total / len(velocidades)
    return promedio

# Se toman las velocidades sobre la media
def correas_promedio_sobre(velocidades):
    promedio = promedio_calculo(velocidades)
    posiciones_promedio_sobre = [posicion for posicion, veloz in enumerate(velocidades) if veloz > promedio]
    return posiciones_promedio_sobre

velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19, 
             14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22, 
             14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5, 
             23, 20, 23, 21]


posiciones_promedio_sobre = correas_promedio_sobre(velocidad)
print(posiciones_promedio_sobre)

