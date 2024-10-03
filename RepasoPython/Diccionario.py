# #Diccionario
# datos_personales = {
#     "Nombre": "Juan",
#     "Apellido": "Lopez",
#     "Edad": 33,
#     "Sexo": "M"
# }
# print(type(datos_personales))

# #Opcion2:
# # datos = dict(
# #     Nombre = "Juan",
# #     Apellido = "Lopez",
# #     Edad = 33,
# #     Sexo = "M"
# # )
# # print(type(datos))

# #Acceder a la edad de Juan:
# print(datos_personales["Edad"])
# print(datos_personales.get("Edad"))

# #Modificar la edad de Juan:
# datos_personales["Edad"] = 34
# print(datos_personales)

# datos_personales["Fecha_nac"] = "07/10/1991"
# print(datos_personales)

# #Eliminar elemento 
# #pop(clave)
# #popitem() elimina el ultimo elemento
# datos_personales.popitem()
# print(datos_personales)
# #del, clear
# #keys(): obtiene claves del diccionario
# claves = datos_personales.keys()
# print(claves)

# for c in datos_personales.keys():
#     print(c)
# #value(): obtiene los valores del diccionario
# print(datos_personales.values())

# for v in datos_personales.values():
#     print(v)

# #items(): obtiene claves y valores al tiempo
# XY = datos_personales.items()
# print(XY)

# for x, y in datos_personales.items():
#     print(f"El valor de la clave {x} es {y}")

# otros_datos = {
#     "Fecha_nac": "19/07/1991",
#     "Profesion": "Administrador de empresas",
#     "Ocupacion": "Líder de equipo"
#     }

# #Update: actualizar diccionario
# datos_personales.update(otros_datos)
# print(datos_personales)


#----------------------------------------------------------------

#Ejercicio 1: Solicitar un numero por teclado y crear un diccionario, cuyas claves sean desde el 1 hasta el numero ingresado
#  y los valores sean el cubo de las claves. Mostrar claves y su valor correspondiente

# numero = int(input("Ingrese un número: "))

# diccionario = {
#     clave: clave**3 for clave in range(1, numero+1)
# }

# for clave, valor in diccionario.items():
#     print(f"La clave {clave} tiene el valor {valor}")


#Ejercicio 2: Crear un diccionario que almacene nombres de frutas como clave y su precio como valor. Solicitar al usuario un nombre de una fruta 
# (Validar si la fruta existe o no) si no existe mostrar el mensaje correspondiente, si existe preguntar la cantidad que desea comprar y debe mostrar cual seria el precio total

frutas = {
    "manzana": 2000,
    "mango": 4000,
    "uva": 3500,
    "naranja": 5000
}

nombre_fruta = input("Ingrese el nombre de la fruta: ").lower()

if nombre_fruta in frutas:
    precio_fruta = frutas[nombre_fruta]
    cantidad = int(input("Ingrese la cantidad de la fruta que desea comprar: "))
    total_precio = precio_fruta * cantidad
    print(f"El precio total de la compra es: {total_precio}")
else: print("La fruta no esta disponible")

