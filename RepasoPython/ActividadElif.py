"""ACTIVIDAD ELIF
1. Escriba un programa que solicite al usuario el año actual y otro año
cualquiera, este debe mostrar en un mensaje claro para el usuario
cuantos años han pasado o faltan para llegar a ese año."""


"""currentYear = int(input("Ingrese el año actual: "))
anotherYear = int(input("Ingrese un año cualquiera: "))

calculateYear = currentYear - anotherYear

# Mostrar el resultado utilizando condicionales elif
if calculateYear > 0:
    print(f"Han pasado {calculateYear} años desde el año {anotherYear}.")
elif calculateYear < 0:
    print(f"Faltan {calculateYear} años para llegar al año {anotherYear}.")
else:
    print("El año introducido es el año actual.")"""

#*************************************************************************************************

"""2. Escribir un programa que calcule el área de las siguientes figuras:
triangulo, circulo, cuadrado y rectángulo, el usuario debe escoger la
figura a la que desea calcular el área.
Debe mostrar mensaje que indique los parámetros utilizados para
calcular el área y el resultado de la operación."""

"""figura = input("Seleccione la figura a la cual le desea calcular el area:  1: Triangulo, 2: Circulo, 3: Cuadrado, 4: Rectangulo): ")


if figura == "1":
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    area = base * altura
    print(f"El area de la figura {figura} es {area}")
elif figura == "2":
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    area = base * altura
    print(f"El area de la figura {figura} es {area}")
elif figura == "3":
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    area = base * altura
    print(f"El area de la figura {figura} es {area}")
elif figura == "4":
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    area = base * altura
    print(f"El area de la figura {figura} es {area}")
else:
    print("Ingrese una opción correcta")"""







#*************************************************************************************************


"""3. Solicitar al usuario 4 números, el programa debe mostrar si hay un
numero repetido al menos 2 veces, si todos son diferentes o todos son
iguales."""

num1 = int(input("Ingrese el número 1: "))
num2 = int(input("Ingrese el número 2: "))
num3 = int(input("Ingrese el número 3: "))
num4 = int(input("Ingrese el número 4: "))

numeros = [num1, num2, num3, num4]

if num1 == num2 == num3 == num4:
    print("Todos los números son iguales.")

# Verificar si todos los números son diferentes
elif len(set(numeros)) == 4:
    print("Todos los números son diferentes.")

# Verificar si hay al menos un número repetido
else:
    print("Hay un número repetido al menos 2 veces.")