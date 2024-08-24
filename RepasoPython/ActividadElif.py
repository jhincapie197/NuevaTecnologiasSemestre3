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

"""num1 = int(input("Ingrese el número 1: "))
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
    print("Hay un número repetido al menos 2 veces.")"""

#*************************************************************************************************


"""IF – ELSE y
OPERADORES
LOGICOS:

1. Para tributar un determinado impuesto se debe ser mayor de 18 años
y tener unos ingresos iguales o superiores a 2.500.000 mensuales.
Escribir un programa que pregunte al usuario su edad y sus ingresos
mensuales y muestre por pantalla si el usuario tiene que tributar o
no."""

"""edad = int(input("Digite su edad: "))
ingresos = float(input("Digite sus ingresos mensuales: "))

if edad > 18 and ingresos >= 2500000:
    print("Tiene que tributar")
else:
    print("No tiene que tributar")"""


#*************************************************************************************************

"""OPERADOR DE ASIGNACION

1. Realizar una calculadora que:
• Realice las operaciones básicas (suma, resta, multiplicación, división, potenciación, resto).
• Debe crear un menú de opciones con las operaciones a
realizar.
• Para realizar cada operación se debe solicitar solo 2 números.
• El código debe funcionar con una sola variable"""



menu = input("Digite operacion a realizar:\n" 
             "1: Suma \n"
             "2: Resta \n"
             "3: Multiplicacion \n"
             "4: Division \n"
             "5: Potenciacion\n"
             "6: Resto\n")


if menu == "1":
    num = int(input("Digite el numero 1: "))
    num += int(input("Digite el numero 2: "))
    print(f"El resultado de la suma es {num}")
elif menu == "2":
    num = int(input("Digite el numero 1: "))
    num -= int(input("Digite el numero 2: "))
    print(f"El resultado de la resta es {num}")
elif menu == "3":
    num = int(input("Digite el numero 1: "))
    num *= int(input("Digite el numero 2: "))
    print(f"El resultado de la multiplicacion es {num}")
elif menu == "4":
    num = int(input("Digite el numero 1: "))
    num /= int(input("Digite el numero 2: "))
    print(f"El resultado de la division es {num}")
elif menu == "5":
    num = int(input("Digite el numero 1: "))
    num **= int(input("Digite el numero 2: "))
    print(f"El resultado de la potenciacion es {num}")
elif menu == "6":
    num = int(input("Digite el numero 1: "))
    num %= int(input("Digite el numero 2: "))
    print(f"El resultado del resto es {num}")
else:
    print("Ingrese una opción válida")