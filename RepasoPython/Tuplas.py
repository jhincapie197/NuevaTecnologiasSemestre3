#Tuplas
"""
Se representan con parentesis:
tupla1 = ()

Tambien puede tener cualquier tipo de datos:
tupla2 = (1, "texto", 1.0, True)

Son inmutables
Son indexadas

Metodos no compatibles con las tuplas: insert, append, sort

"""

dias_semana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes")
print(type(dias_semana))

#Para que Python detecte una consulta de una tupla, debe llevar una , al final
dias1 = ("Lunes",)

#Acceder a un elemento de la tupla:
print(dias_semana[2])

#Conocer el indice o posicion de un elemento de la tupla:
print(dias_semana.index("Jueves"))

""" Arroja error por que no se puede modificar, no son mutables
dias_semana["Lunes"] = "Sabado"
print(dias_semana)"""

#Contar cuantas veces aparece "Viernes" en la tupla
print(dias_semana.count("Viernes"))

#Convertir una tupla en una lista
# lista_dias = list(dias_semana)
# print(lista_dias)

#Eliminar objeto dias_semana
del dias_semana
print(dias_semana)