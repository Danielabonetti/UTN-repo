#1. Factorial de un número
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
       
        return "El factorial no está definido para números negativos"
    else:
        return n * factorial(n - 1)

def calcular_factoriales_hasta_n():
    try:
        num_ingresado = int(input("FACTORIAL - Ingresa un número entero positivo: "))
        if num_ingresado < 1:
            print("Por favor, ingresa un número igual o mayor a 1.")
            return

        for i in range(1, num_ingresado + 1):
            print(f"{i}! = {factorial(i)}")

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")

calcular_factoriales_hasta_n()



#2. Serie de Fibonacci hasta la posición dada
def fibonacci_recursivo(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

def mostrar_serie_fibonacci():
    try:
        num_ingresado = int(input("\nFIBONACCI - Introduce la cantidad de términos de la serie Fibonacci: "))
        if num_ingresado < 0:
            print("Por favor, ingresa un número positivo.")
            return

        print("Serie de Fibonacci:")
        for i in range(num_ingresado + 1):
            print(f"Fibonacci({i}) = {fibonacci_recursivo(i)}")

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")

mostrar_serie_fibonacci()


#3. Potencia de un número
def potencia(base, exponente):
   
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def calcular_potencia():
    try:
        base = int(input("\nPOTENCIA - Introduce la base: "))
        exponente = int(input("POTENCIA - Introduce el exponente (solo positivos para esta función): "))

        if exponente < 0:
            print("Por favor, ingresa un exponente positivo.")
            return

        print(f"{base}^{exponente} = {potencia(base, exponente)}")

    except ValueError:
        print("Entrada inválida. Por favor, ingresa números enteros.")

calcular_potencia()


#4. Conversión de decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return "0"
    return decimal_a_binario(n // 2) + str(n % 2)

def solicitar_numero():
    while True:
        try:
            num = int(input("Introduce un número entero positivo para convertirlo a binario: "))
            if num < 0:
                print("No se pueden convertir números negativos. Intenta de nuevo.")
            else:
                return num
        except ValueError:
            print("Eso no parece un número válido. Intenta de nuevo.")

num = solicitar_numero()
print(f"{num} en binario es {decimal_a_binario(num)}")




#5. Palíndromo 
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
   
    return es_palindromo(palabra[1:-1])

def solicitar_palabra_palindromo():
    palabra = input("\nPALÍNDROMO - Introduce una palabra sin espacios ni tildes: ").lower()
    resultado = es_palindromo(palabra)
    print(f"¿La palabra '{palabra}' es un palíndromo? ➡ {resultado}")

solicitar_palabra_palindromo()



# 6. Suma de dígitos
def suma_digitos(n):
    if n < 0:
        raise ValueError("Ingresa un número entero positivo.")
    elif n < 10: 
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

def solicitar_numero_suma_digitos():
    try:
        num_str = input("\nSUMA DÍGITOS - Introduce un número entero positivo: ")
        num = int(num_str)

        resultado = suma_digitos(num)
        print(f"La suma de los dígitos de {num} es: {resultado}")

    except ValueError:
        print("Entrada inválida. Por favor, ingresá un número válido.")
    except Exception:
        print("Ocurrió un error inesperado.")

solicitar_numero_suma_digitos()

#7. Contar bloques
def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)

def calcular_total_bloques():
    try:
        num_niveles = int(input("\nPIRÁMIDE DE BLOQUES - Ingresá el número de bloques en el nivel más bajo: "))
        if num_niveles < 0:
            print("Por favor, ingresá un número positivo o cero.")
            return

        resultado = contar_bloques(num_niveles)
        print(f"Total de bloques para {num_niveles} niveles: {resultado}")

    except ValueError:
        print("Entrada inválida. Por favor, ingresá un número entero válido.")
    except Exception:
        print("Ocurrió un error inesperado.")

calcular_total_bloques() 


#8. contar digitos
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

def solicitar_datos():
    try:
        numero = int(input("Introduce un número entero positivo: "))
        digito = int(input("Introduce un dígito (0-9): "))
        
        if numero < 0 or not (0 <= digito <= 9):
            print("Por favor, ingresa un número positivo y un dígito válido entre 0 y 9.")
        else:
            print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en {numero}.")

    except ValueError:
        print("Entrada inválida. Por favor, ingresa valores numéricos.")

solicitar_datos()
