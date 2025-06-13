import math

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

def saludar_usuario(nombre):
    return f"Hola {nombre}"

nombre_ingreso = input("ingresa tu nombre ")
print(saludar_usuario(nombre_ingreso))

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre_ingresado = input("nombre") 
apellido_ingresado = input("apellido")
edad_ingresado = input("edad")
residencia_ingresado = input("residencia")

informacion_personal(nombre_ingresado, apellido_ingresado, edad_ingresado, residencia_ingresado)

#pixradioalcuadrado
#perimetro 2xpixradio

def calcular_area_circulo(radio):
    return math.pi*(radio**2)

def calcular_perimetro_circulo(radio):
    return math.pi*2*radio

try:
    radio_ingresado = float(input("ingrese radio"))
except ValueError:
    print("Entrada invalida, por favor ingrese un valor valido")
else:
    area = calcular_area_circulo(radio_ingresado)
    perimetro = calcular_perimetro_circulo(radio_ingresado)


    print(f"el area es {area} y el perimetro {perimetro}")   


def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

try:
    segundo_ingresados = float(input("ingrese segundos"))
except ValueError:
    print("Valor invalido, ingreso un valor valido")
if segundo_ingresados <0:
    print("Ingrese un valor que no sea negativo")
else: 
    horas_calculadas = segundos_a_horas(segundo_ingresados)
    print(f"los segundos {segundo_ingresados} ingresados son {horas_calculadas} horas.")

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Introduce un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num)


def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b if b != 0 else "División por cero no permitida")

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)

peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))
print(f"Tu índice de masa corporal (IMC) es: {calcular_imc(peso, altura)}")


def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Introduce la temperatura en Celsius: "))
print(f"La temperatura en Fahrenheit es: {celsius_a_fahrenheit(celsius)}")


def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
c = float(input("Introduce el tercer número: "))
print(f"El promedio es: {calcular_promedio(a, b, c)}")







    