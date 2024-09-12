"""Estructura de datos

*Listas --> []
Soporta cualquier tipo de datos.
Son mutables: se pueden modificar
Son idexadas: tienen un indice

Metodos:
-Longitud: len()
-Insertar elementos: append(argumento)
                     insert(indice, valor)"""

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
#Cantidad de elementos
print(len(dias))
#Acceder a los elementos de la lista
print(dias[2])
#Insertar elemento en la ultima posicion: append(argumento)
dias.append("Sabado")
print(dias)
#Insertar elemento en una posicion especifica: insert()
dias.insert(0, "Domingo")
print(dias)

#Crear dos listas, una con numeros aleatorios y otra vacia, de la lista numerica validar que numeros son multiplos de 5 y agregarlos a la lista vacia, 
#mostrar la lista con los multipos de 5 y la cantidad de elementos que contiene

multiplo_5 = []
numeros = [10,19,6,20,28,7,91,30,45,90,33,5,10]
for indice in range(len(numeros)):
    if numeros[indice] % 5 == 0:
        multiplo_5.append(numeros[indice])
print(multiplo_5)
print(f"La lista multiplo_5, contiene {len(multiplo_5)} elementos")

#Metodos para eliminar elementos de la lista
#POP(): elimina un elemento en la posicion especifica, si no se especifica elimina y retorna el ultimo
#REMOVE(): elimina el elemento epecificado como argumento
#CLEAR(): elimina todos los elementos de la lista
#DEL(): elimina el objeto, es decir, la lista

#De la lista numerica utilizada anteriormente, eliminar los numeros iguales a 10
while 10 in numeros:
    numeros.remove(10)
print(numeros)