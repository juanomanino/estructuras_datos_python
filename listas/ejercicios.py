# EJERCICIOS LISTAS

# Ejercicios manipulación

#1. Consiste en la definición de una lista con elementos de diferentes tipos y el mostrarla por pantalla, tanto entero como por elementos accediendo a la posición que ocupa dentro de la lista.
lista=["Python", "Guanentá", 2022, "Libro", 3]
print(lista)
print(lista[0])
print(lista[2])

# 2. Consiste del uso del operador + para realizar uniones de listas. Además, utilizar la función len para conoceer el número de elementos que componen la lista
lista1=["Camiseta", "Pantalón", "Zapatillas"]
lista2=["Abrigo", "Jersey", "Sudadera", "Calcetines"]

print("Número de elementos lista1: ", len(lista1))
print("lista1: ", lista1)
print("Número de elementos lista2: ", len(lista2))
print("lista2: ", lista2)

lista_concatenada= lista1+lista2
print("Número de elementos lista_concatenada: ", len(lista_concatenada))
print("lista_concatenada: ", lista_concatenada)

# 3. Añadir elementos a la lista de diferentes formas
lista=["Camiseta", "Pantalón", "Zapatillas"]
print(lista)
lista=lista+["Abrigo"]
print(lista)
lista=lista+["Jersey", "Sudadera"]
print(lista)
lista=lista+["Calcetines"]+["Bufanda"]
print(lista)

# 4. Modificar elementos de una lista y borrar elementos de la misma
lista=["Camiseta", "Pantalón", "Zapatillas"]
print(lista)
lista[1]="Cazadora"
print(lista)
del lista[0]
print(lista)

