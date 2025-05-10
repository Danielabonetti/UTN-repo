# Ejercicio 1: Programa que solicita la edad del usuario y muestra si es mayor de edad.
# Solicitar al usuario su edad
edad = int(input("Introduce tu edad: "))

# Comprobar si es mayor de edad
if edad > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# Ejercicio 2: Programa que solicita la nota al usuario y muestra si ha aprobado o no.
# Solicitar al usuario su nota
nota = float(input("Introduce tu nota: "))

# Comprobar si ha aprobado
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3: Programa que permite ingresar solo números pares.
# Solicitar al usuario un número
numero = int(input("Ingresa un número: "))

# Comprobar si el número es par
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Ejercicio 4: Clasificación de edad en categorías.
# Solicitar al usuario su edad
edad = int(input("Introduce tu edad: "))

# Clasificar la edad en categorías
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Ejercicio 5: Validar la longitud de una contraseña.
# Solicitar al usuario una contraseña
contraseña = input("Introduce una contraseña: ")

# Comprobar si la longitud es adecuada
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6: Comparar la moda, la mediana y la media para determinar el sesgo.
from statistics import mode, median, mean
import random

# Crear una lista con 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Comprobar el sesgo
if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo")

# Ejercicio 7: Modificar la frase si termina con vocal.
# Solicitar al usuario una frase o palabra
frase = input("Introduce una frase o palabra: ")

# Comprobar si la última letra es vocal
if frase[-1].lower() in 'aeiou':
    print(frase + "!")
else:
    print(frase)

# Ejercicio 8: Cambiar el formato del nombre según la opción seleccionada.
# Solicitar al usuario su nombre
nombre = input("Introduce tu nombre: ")

# Solicitar al usuario la opción de formato
opcion = int(input("Elige una opción (1, 2, 3):\n1. Mayúsculas\n2. Minúsculas\n3. Primera letra mayúscula\n"))

# Aplicar el formato según la opción seleccionada
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")

# Ejercicio 9: Clasificar la magnitud de un terremoto.
# Solicitar al usuario la magnitud del terremoto
magnitud = float(input("Introduce la magnitud del terremoto: "))

# Clasificar la magnitud del terremoto
if magnitud < 3:
    print("Muy leve")
elif 3 <= magnitud < 4:
    print("Leve")
elif 4 <= magnitud < 5:
    print("Moderado")
elif 5 <= magnitud < 6:
    print("Fuerte")
elif 6 <= magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

# Ejercicio 10: Determinar la estación del año según el hemisferio y la fecha.
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("¿Qué mes del año es? (1-12): "))
dia = int(input("¿Qué día del mes es?: "))

# Clasificar la estación según el hemisferio y la fecha
if hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and mes != 3) or (mes == 3 and dia <= 20):
        print("Es invierno")
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 6) or (mes == 6 and dia <= 20):
        print("Es primavera")
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 9) or (mes == 9 and dia <= 20):
        print("Es verano")
    else:
        print("Es otoño")
else:
    if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and mes != 3) or (mes == 3 and dia <= 20):
        print("Es verano")
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 6) or (mes == 6 and dia <= 20):
        print("Es otoño")
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 9) or (mes == 9 and dia <= 20):
        print("Es invierno")
    else:
        print("Es primavera")
