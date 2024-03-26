#{}  []

# Calculo factorial

def factorial(numero):
    valor = 1
    for n in range(1, numero + 1):
        valor = valor * n
    return valor
    
    
# Calculo productoria
def productoria(lista):
    valor = 1
    for elemento in lista:
        valor *= elemento
    return valor

# *Tupla     ** Diccionario
def calcular(**parametros):
    for clave, valor in parametros.items():
        if 'fact' in clave:
            print(f'El Factorial de {valor} es {factorial(valor)}')
        else:
            print(f'La productoria de {valor} es {productoria(valor)}')
            
calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)