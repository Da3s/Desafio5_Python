def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def productoria(lista):
    result = 1
    for num in lista:
        result *= num
    return result

def calcular(**kwargs):
    for key, value in kwargs.items():
        if key.startswith('fact_'):
            num = int(value)
            print(f"El factorial de {num} es {factorial(num)}")
        elif key.startswith('prod_'):
            lista = value
            print(f"La productoria de {lista} es {productoria(lista)}")

if __name__ == "__main__":
    calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
