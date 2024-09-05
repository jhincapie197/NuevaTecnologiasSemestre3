def operMat(valor1, valor2, operador):
    resultado = 0
    if operador == "+":
        resultado = valor1 + valor2
    elif operador == "-":
        resultado = valor1 - valor2
    elif operador == "*":
        resultado = valor1 * valor2
    elif operador == "/":
        if valor2 != 0:
            resultado = valor1 / valor2
        else:
            print("Error: División por cero")
    elif operador == "e":
        resultado = pow(valor1, valor2)
    elif operador == "r":
        resultado = pow(valor1, 1/valor2)
    return resultado
