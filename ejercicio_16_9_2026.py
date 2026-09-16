def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(numero1, numero2, operacion):
    if operacion == "+":
        return sumar(numero1, numero2)
    elif operacion == "-":
        return restar(numero1, numero2)
    elif operacion == "*":
        return multiplicar(numero1, numero2)
    elif operacion == "/":
        return dividir(numero1, numero2)


while True:
    numero1 = float(input("Introduzca el primer numero: "))
    numero2 = float(input("Introduzca el segundo numero: "))
    operacion = input("Introduzca la operacion a realizar (+, -, *, /): ")

    print(calcular(numero1, numero2, operacion))

    opcion = input("Escribe 'salir' para terminar: ")

    if opcion == "salir":
        break

calcular(5, 3, "+")