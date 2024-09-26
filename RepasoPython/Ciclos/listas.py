"""Estructura de datos: es para almacenar gran cantidad de informacion en una sola variable

*Listas --> []
Soporta cualquier tipo de datos.
Son mutables: se pueden modificar
Son idexadas: tienen un indice

Metodos:
-Longitud: len()
-Insertar elementos: append(argumento)
                     insert(indice, valor)"""

# dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
# #Cantidad de elementos
# print(len(dias))
# #Acceder a los elementos de la lista
# print(dias[2])
# #Insertar elemento en la ultima posicion: append(argumento)
# dias.append("Sabado")
# print(dias)
# #Insertar elemento en una posicion especifica: insert()
# dias.insert(0, "Domingo")
# print(dias)

#Crear dos listas, una con numeros aleatorios y otra vacia, de la lista numerica validar que numeros son multiplos de 5 y agregarlos a la lista vacia, 
#mostrar la lista con los multipos de 5 y la cantidad de elementos que contiene

# multiplo_5 = []
# numeros = [10,19,6,20,28,7,91,30,45,90,33,5,10]
# for indice in range(len(numeros)):
#     if numeros[indice] % 5 == 0:
#         multiplo_5.append(numeros[indice])
# print(multiplo_5)
# print(f"La lista multiplo_5, contiene {len(multiplo_5)} elementos")

#Metodos para eliminar elementos de la lista
#POP(): elimina un elemento en la posicion especifica, si no se especifica elimina y retorna el ultimo
#REMOVE(): elimina el elemento epecificado como argumento
#CLEAR(): elimina todos los elementos de la lista
#DEL(): elimina el objeto, es decir, la lista

#De la lista numerica utilizada anteriormente, eliminar los numeros iguales a 10
# while 10 in numeros:
#     numeros.remove(10)
# print(numeros)


#Conocer la posicion del elemento: index(), tambien es compatible con las tuplas.

# nombres = ["Juan", "Camilo", "Juliana", "Analia", "Fernanda", "Fernando"]
# nombres.insert(3, "Arturo")
# print(nombres)

#En que posicion esta Fernanda?
#Opcion 1:
# buscar = nombres.index("Fernanda")
# print(buscar)

# #Opcion 2:
# print(nombres.index("Fernanda"))

#count(argumento): indica cuantas veces esta repetido un elemento en la lista

#Cuantas veces esta repetido el numero 1 en la lista
# digitos = [1,2,3,4,5,6,1,5,6,9,4,1,1,1]
# print(digitos.count(1))
# print(nombres.count("Arturo"))

#Ordenar listas:

#sort(): organiza de forma ascendente
#sort(reverse=True): oganiza de forma descendente

#Organizar la lista de digitos de forma ascendente:
# digitos.sort()
# print(digitos)

# nombres.sort()
# print(nombres)

#Organizar la lista de digitos de forma descendente:
# digitos.sort(reverse=True)
# print(digitos)

# nombres.sort(reverse=True)
# print(nombres)

#----------------------------------------------------------------

#Recorrer dos listas al tiempo: zip()
# tipo_animales = ["Terrestre", "Acuatico", "Aereo"]
# animales = ["Gato", "Pez", "Pajaro"]

# for Ta, A in zip(tipo_animales, animales):
#     print(f"El {A} es un animal {Ta}")



# Una empresa llamada “Transportes Cesde” requiere guardar los nombres de los
# conductores y el dinero que recaudan cada día de la semana (lun a sábado)
# movilizando a la comunidad educativa y el porcentaje de recaudo de cada conductor.
# Para guardar esta información se crearán las siguientes listas:
# NombreConductor: para almacenar los nombres de los conductores.
# DiasSemana: que contiene los días de lunes a sábado.
# Recaudo: lista para guardar la cantidad recolectada cada día de la semana.
# Se debe generar una lista llamada total recaudo con la suma total de lo recaudado por
# cada conductor.
# Debe solicitar el número de conductores que hacen parte de la empresa de Transporte Cesde.

nombreConductor = []
diasSemana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
recaudosDia = []
totalRecaudo = []

numConductores = int(input("Ingrese el numero de conductores: "))

for i in range(numConductores):
    nombre = input(f"Ingrese el nombre del conductor {i+1}: ")
    nombreConductor.append(nombre)
    recaudo_dia = [] 
    total = 0

    for dia in diasSemana:
        recaudo = float(input(f"Ingrese el recaudo del conductor {nombre} en el dia {dia}: "))
        recaudo_dia.append(recaudo)
        total += recaudo

    recaudosDia.append(recaudo_dia)
    totalRecaudo.append(total)

print("\nReporte de conductores:")
for i in range (numConductores):
    print(f"Conductor: {nombreConductor[i]}")
    print(f"Recaudos diarios: {recaudosDia[i]}")
    print(f"Total recaudo: {totalRecaudo[i]}\n")