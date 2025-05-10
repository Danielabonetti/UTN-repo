# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4
multiples_de_4 = list(range(4, 101, 4))
print("Multiples de 4:", multiples_de_4)

# 2) Crear una lista con cinco elementos (coloca los elementos que más te gusten) y mostrar el penúltimo
mis_elementos = ["pizza", "libro", "música", "película", "viaje"]
print("Penúltimo elemento:", mis_elementos[-2])  # El penúltimo

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista
lista_vacia = []
lista_vacia.append("perro")
lista_vacia.append("gato")
lista_vacia.append("conejo")
print("Lista vacía con palabras:", lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales”
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"  # Segundo valor
animales[-1] = "oso"  # Último valor
print("Lista de animales modificada:", animales)

# 5) Explicación del programa
# (Te puedo ayudar con esta explicación si tienes el código)

# 6) Crear una lista con números del 10 al 30 (incluido), saltando de 5 en 5 y mostrar los dos primeros
numeros = list(range(10, 31, 5))
print("Primeros dos números:", numeros[:2])  # Los dos primeros

# 7) Reemplazar los dos valores centrales de la lista “autos”
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "ford"  # Reemplaza el segundo valor
autos[2] = "fiat"  # Reemplaza el tercero
print("Lista de autos modificada:", autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Lista con los dobles:", dobles)

# 9) Manipulación de la lista “compras”
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

# d) Imprimir la lista resultante
print("Lista de compras modificada:", compras)

# 10) Crear una lista anidada llamada “lista_anidada”
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("Lista anidada:", lista_anidada)
