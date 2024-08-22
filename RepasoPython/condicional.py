#Condicionales (IF - ELIF):
"""numero = int(input("Ingrese un numero entero positivo: "))
if numero % 2 == 0:
    print("El número es par")
    print(f"El número {numero} es par")
    print("El número " + str(numero) + " es par")
    print("El número", numero, "es par")
else:
    print("El número es impar")
    print(f"El número {numero} es impar")
    print("El número", numero, "es impar")"""


#Solicitar nombre, edad de un usuario y si el usuario tiene o no pasaporte.
#Si el usuario es mayor de edad y tiene pasaporte debe mostrar "Puede realizar viajes internacionales", de lo contrario "No puede abandonar el pais"
"""nombre = input("Ingrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))
pasaporte = input("¿Tiene pasaporte? Si/No: ")

if edad >= 18 and pasaporte == "Si":
    print(f"El usuario {nombre} puede realizar viajes internacionales")
else:
    print(f"El usuario {nombre} no puede abandonar el pais")"""

#Elif: se utiliza para validar 2 o mas condiciones

nombre = input("Ingrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))
pasaporte = input("¿Tiene pasaporte? Si/No: ")

if edad >= 18 and pasaporte == "Si":
    print(f"El usuario {nombre} puede realizar viajes internacionales")
elif edad <18 and pasaporte == "Si":
    print(f"El usuario {nombre} puede realizar viajes internacionales si tiene permisos de sus acudientes")
else:
    print(f"El usuario {nombre} no puede abandonar el pais")


#If anidado: es un if dentro de otro if
#Ejemplo: if condicion
            #if condicion
                #instruccion