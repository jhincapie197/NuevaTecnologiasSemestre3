#Tupla

# tuplaNros = (12,15,14,16)
# print (tuplaNros)

# for nro in tuplaNros:
#     print(f"El número de la tupla es: {nro}")

# #Buscar un numero
# nroBuscar = int(input("Ingrese el numero a buscar en la tupla: "))
# i = 0

# #Variable tipo bandera
# #bandera = False

# for num in tuplaNros:
#     if num == nroBuscar:
#         #bandera = True
#         break
#     i += 1
# #if bandera:
# if i < len(tuplaNros):
#     print(f"El numero {nroBuscar} esta en la posición {i}")
# else:
#     print(f"El numero {nroBuscar} no se encontró")

#----------------------------------------------------------------

#Set (conjunto de datos)
conj = {"María", "Pedro", "Teresa", "Valentina"}
print(conj)
for nombre in conj:
    print(nombre)

#Diccionario
dicProducto = {"ref":"A01", "nombre":"Mouse", "precio":25000,"estado":False}
for prod in dicProducto:
    print(f"{prod}: {dicProducto[prod]}")

#Lista con diccionario
empleados = [
    {"id":"10", "fullname":"Teresa Valencia", "salario": 2500000},
    {"id":"11", "fullname":"Fausto Zapata", "salario": 3500000},
    {"id":"12", "fullname":"Otilia Bonilla", "salario": 4500000}
]

#Iterar en empleados
for emp in empleados:
    print(f"El nombre completo es {emp["fullname"]}")
acumSalario = 0

for employee in empleados:
    acumSalario += employee["salario"]
promSalario = acumSalario / len(empleados)
print(f"El promedio de salarios es: {promSalario}")