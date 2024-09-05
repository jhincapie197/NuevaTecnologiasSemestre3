#Importar funciones del archivo funciones.py

from misfunciones.funciones import operMat

valor1 = int(input("Digite el numero 1: "))
valor2 = int(input("Digite el numero 2: "))
operador = input("Digite la operación a realizar (+, -, *, /, e, r): ")

print(operMat(valor1, valor2, operador))
# print(operMat(5,2,"-"))
# print(operMat(5,2,"*"))
# print(operMat(5,2,"/"))
# print(operMat(5,2,"e"))
# print(operMat(4,2,"r"))
