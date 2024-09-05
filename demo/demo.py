#Esto es un comentario de una linea
'''
Esto es un comentario
de varias lineas

'''

'''name = "Pere Perez"
salaryEmployee = 2500000
gender = True
print("Hola mundo...")
print("El nombre del empleado es: ", {name})
print(f"Nombre {name} y su salario es: {salaryEmployee}")'''

'''if salaryEmployee > 3500:
    print("El empleado es un empresario")
else:
    print("El empleado es un trabajador")'''

'''tipoEmp = "Empresario" if salaryEmployee > 3500000 else "Trabajador"
print(f"{tipoEmp}")''' #Se hizo la reduccion a dos lineas de codigo con operadores ternarios

#Se hizo la reduccion a una linea con operadores ternarios
#print(f"{"Empresario" if salaryEmployee > 3500000 else "Trabajador"}")

#El not es para negar la variable, es decir, se pregunta por el false
#print(f"El sexo es: {"Masculino" if not gender else "Femenino"}")
#print(f"El sexo es: {"Bono" if not gender and salaryEmployee < 2500000 else "Femenino"}")

'''category = input("Ingrese la categoria: ")
if category == "A":
    print("El empleado tiene un bonus de 20%")
elif category == "B":
    print("El empleado tiene un bonus de 15%")
elif category == "C":
    print("El empleado tiene un bonus de 10%")
elif category == "D":
    print("El empleado tiene un bonus de 5%")
else:
    print("El empleado no tiene un descuento")'''


#Ciclos
#While

'''c = 1

while c < 10:
    print(f"Iteracion {c}")
    c += 1

fullName = input("Ingrese el nombre (* para terminar): ")

while fullName != "*":
    print(f"Hola {fullName}")
    fullName = input("Ingrese el nombre (* para terminar): ")'''

'''sw = True
while sw:
    num = int(input("Ingrese un numero (0 para salir) "))
    # if num == 0:
    #     sw = False
    # else:
    #     print(f"El cuadrado de {num} es: {num**2}")

    sw = False if num == 0 else print(f"El cuadrado es: {num**2}")

    #Tarea: revisar por que no sigue en el ciclo'''


#For

"""for i in range(1,11,2):
    print(f"Iteracion {i}")
for j in range(20,0,-1):
    print(f"Iteracion {j}")"""
#0,1,1,2,3,5,8,13,21
#Realizar ejercicio que imprima esa serie


def fibonacci(n):
    """Imprime los primeros n términos de la secuencia de Fibonacci."""
    a, b = 0, 1
    for _ in range(n):
        print(a, end=', ' if _ < n-1 else '\n')
        a, b = b, a + b

# Número de términos que deseas imprimir
numero_de_terminos = 9
fibonacci(numero_de_terminos)
