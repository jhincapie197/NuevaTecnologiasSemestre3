"""Bucles - Ciclos

for: Itera hasta finalizar rango especifico

Sintaxys: for (variable) in (objeto iterable):
    instruccion(es)


for variable in range(inicial, final, salto):
    instruccion(es)"""

#Imprimir numeros menores o iguales que 10

for n in range(1,10):
    print(n)

#Solicitar al usuario una palabra, contar cuantas vocales "a" tiene la palabra ingresada. Mostrar la cantidad encontrada. 
#Estandarizar la palabra encontrada ya sea mayuscula o minuscula

#upper(): convierte las palabras a mayuscula
#lower(): convierte las palabras a minuscula
#Title(): convierte la primera letra de las palabras a mayuscula

palabra = input("Ingrese una palabra: ")
contador_vocales = 0

for letra in palabra:
    if letra.lower() == 'a':
        contador_vocales += 1
print(contador_vocales)