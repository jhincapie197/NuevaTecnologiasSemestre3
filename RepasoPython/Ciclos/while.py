#Bucles - Ciclos

#While (Mientras)
#Itera hasta que la condicion cambia a falsa

#Sintaxys: Inicializar variables importantes
#while (conficion):
    #instruccion(es)


#Imprimir los numeros menores o iguales que 10

num = 0
while num <= 10:
    print(num)
    num += 1

#Solicitar al usuario un numero inicial y numero final de un rango, validar si un numero es par y mostrar solo los numeros pares del rango

num_inicial = int(input("Ingrese el número inicial del rango: "))
num_final = int(input("Ingrese el número final del rango: "))

while num_inicial <= num_final:
    if num_inicial % 2 == 0:
        print(num_inicial)
    num_inicial += 1

