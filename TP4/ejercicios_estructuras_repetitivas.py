# Ejercicio 1: Imprimir números enteros del 0 al 100
print("Ejercicio 1: Números enteros del 0 al 100")
for i in range(101):
    print(i)
print("\n")

# Ejercicio 2: Determinar la cantidad de dígitos de un número ingresado por el usuario
print("Ejercicio 2: Cantidad de dígitos de un número")
numero = int(input("Ingrese un número entero: "))
cantidad_digitos = len(str(abs(numero)))  # abs() para manejar números negativos
print(f"El número tiene {cantidad_digitos} dígitos.\n")

# Ejercicio 3: Sumar números entre dos valores dados por el usuario, excluyendo esos dos valores
print("Ejercicio 3: Sumar números entre dos valores")
inicio = int(input("Ingrese el valor inicial: "))
fin = int(input("Ingrese el valor final: "))
suma = 0

for i in range(inicio + 1, fin):
    suma += i

print(f"La suma de los números entre {inicio} y {fin} es {suma}.\n")

# Ejercicio 4: Sumar números hasta que el usuario ingrese 0
print("Ejercicio 4: Sumar números hasta que el usuario ingrese 0")
total = 0

while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break
    total += numero

print(f"El total acumulado es {total}.\n")

# Ejercicio 5: Adivinar un número aleatorio entre 0 y 9
print("Ejercicio 5: Adivinar un número aleatorio entre 0 y 9")
import random

numero_aleatorio = random.randint(0, 9)
intentos = 0
adivinanza = -1

while adivinanza != numero_aleatorio:
    adivinanza = int(input("Adivina un número entre 0 y 9: "))
    intentos += 1

print(f"¡Correcto! El número era {numero_aleatorio}. Te tomó {intentos} intentos.\n")

# Ejercicio 6: Imprimir números pares entre 0 y 100 en orden decreciente
print("Ejercicio 6: Números pares entre 0 y 100 en orden decreciente")
for i in range(100, -1, -2):
    print(i)
print("\n")

# Ejercicio 7: Calcular la suma de todos los números entre 0 y un número dado por el usuario
print("Ejercicio 7: Suma de números entre 0 y un número dado por el usuario")
n = int(input("Ingrese un número entero positivo: "))
suma = sum(range(n + 1))
print(f"La suma de los números entre 0 y {n} es {suma}.\n")

# Ejercicio 8: Contar cuántos números son pares, impares, negativos y positivos entre 100 números ingresados
print("Ejercicio 8: Contar pares, impares, negativos y positivos entre 100 números")
pares = impares = negativos = positivos = 0

for _ in range(100):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1

print(f"Pares: {pares}, Impares: {impares}, Negativos: {negativos}, Positivos: {positivos}\n")

# Ejercicio 9: Calcular la media de 100 números ingresados
print("Ejercicio 9: Calcular la media de 100 números ingresados")
suma = 0

for _ in range(100):
    numero = int(input("Ingrese un número entero: "))
    suma += numero

media = suma / 100
print(f"La media de los números ingresados es {media}.\n")

# Ejercicio 10: Invertir el orden de los dígitos de un número
print("Ejercicio 10: Invertir el orden de los dígitos de un número")
numero = input("Ingrese un número: ")
numero_invertido = numero[::-1]
print(f"El número invertido es {numero_invertido}.")

