# EJERCICIOS TUPLAS

# Ejercicios manipulación

# 1. Consiste en la definición de una tupla y el cómo acceder a sus elementos.
print("------Ejercicio 1-------")

tupla= ("Casa", "2", 345, "Perro", 99)
print("Elementos de la tupla: ", tupla)
print("Elemento de la posición 0: ", tupla [0] )
print("Elemento de la posición 1: ", tupla [1] )
print("Elemento de la posición 2: ", tupla [2] )
print("Elemento de la posición 3: ", tupla [3] )
print("Elemento de la posición 4: ", tupla [4] )


# 2. Extraer porciones de una tupla en otra tupla nueva

print("------Ejercicio 2-------")
tupla=(1,2,3,4,5,6,7,8,9)
print(tupla)
print(tupla[4:9])
print(tupla[:3])
print(tupla[2:])


# Consiste en el uso del operador + para realizar uniones de tuplas 
print("------Ejercicio 3-------")
tupla1=(29, "Televisión",8763)
tupla2=(1,2,3, "Videojuego")
print("Número de elementos de tupla1: ", len(tupla1))
print("Tupla1: ", tupla1)
print("Número de elementos de tupla2: ", len(tupla2))
print("Tupla2: ", tupla2)
tuplaconcatenada=tupla1+tupla2
print("Número de elementos de tuplaconcatenada: ", len(tuplaconcatenada))
print("tuplaconcatenada: ", tuplaconcatenada)

#Consiste en el uso del operador * para concatenar una tupla con ella misma un número finito de veces.
print("------Ejercicio 4-------")
tupla=(1,2,3,4,5,6,7,8,9)
print(tupla)
tuplaresultante=tupla*4
print(tuplaresultante)






