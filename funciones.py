#funciones o metodos en python
#funcion sin retorno
def saludar():
    print("hola como estamos")

#invocacion de la funcion
saludar()
#funcion con retorno
def ver_numero():
    return 150

a = 10
suma = a + ver_numero()
print("la suma es ",suma)

#funcion con parametros
def saludoCustom(saludos:str):
    print(saludos)

saludoCustom("Hola como estas")


def getDatosCliente(nombre, apellido, email, telefono):
    datos_cliente = f"Nombre: {nombre}, Apellido: {apellido}, Email: {email}, Telefono: {telefono}"
    print(datos_cliente)
datos_cliente = True

getDatosCliente("Hector", "Pacheco", "hector@example.com", "1234567890")

#como buena practica
def calcular_sumatoria(num1:float, num2:float)->float:
    print(num1 + num2)
    suma = num1 + num2
    return suma
calcular_sumatoria(100, 20)

def calcularCuadrado(num:int)->int:
    return num*num

print ('respuesta:', calcularCuadrado(5))

try:
    print('Respuesta:', calcularCuadrado('True'))
except Exception as ex:
    print("deberias controlar el error", ex)

print("Fin de las pruebas de funciones")