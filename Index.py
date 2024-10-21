import math

def factores_primos(n):
    factores = []
    
    # Eliminamos los factores de 2
    while n % 2 == 0:
        factores.append(2)
        n = n // 2

    # Revisamos los números impares desde 3 en adelante
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factores.append(i)
            n = n // i

    # Si n es un número primo mayor que 2
    if n > 2:
        factores.append(n)
    
    return factores

# Solicitar al usuario que ingrese un número
numero = int(input("Introduce un número grande: "))
factores = factores_primos(numero)
print(f"Los factores primos de {numero} son: {factores}")
