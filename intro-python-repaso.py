#cometarios en una sola linea

"""
comentarios en varias lineas
esto si mola
"""


#salida de informacion
print("salida de informacion en python")

#entrada de informacion
nombre = input("Cual es tu nombre? ") #un input es una funcion que permite al usuario ingresar datos por teclado y siempre devuelve un string
print("Hola ", nombre ," bienvenido a python")

#tipos de variables en python
#str "todo lo que este entre comillas es un string"
#int 1,2,3,4,5,6,7,8,9
#float 1.2, 3.4, 5.6
#bool True, False
variable1 = "Hola soy un string"
variable2 = 10.5
print(type(variable1))
print(type(variable2))

#las variables son sensibles a mayusculas y minusculas
Variable1 = "Hola soy un string"
vAriable2 = 10.5
print(Variable1)
print(vAriable2)

nombre=None

def nombrar(nom:str)-> True:
    pass

#las variables de python son flexibles y no es necesario declarar su tipo de dato, python lo hace automaticamente

nombre = "Hector"
print(nombre)
nombre = True
print(nombre)
nombre = 100
print(nombre)

#reglas de nombres de variables en python
#nombres de variables y funciones van en minusculas
#nombres de clases van con la primera letra en mayuscula
#nombre de variables de tipo constante van en mayusculas VALOR_PI=3.1434554

#DECLARACION DE VARIABLES
#NO SE PUEDE
#Numero antes de una letra en el nombre de la variable  -----> 10valor="ana"
#espacios entre nombre de la variable  -----> nombre variable="ana"
#cuenta bancaria= 1512312315


#SE PUEDE
nombre10="Maria"
#camel case o   snake case
cuenta_bancaria= 1512312315
cuentaCorrienteCerrado = 1512312313

#Cating o casteo o inferirencia de tipos de datos
numero1 = "100"
numero2 = 200
suma = int(numero1) + numero2
print("la suma es ",suma)
#se puede hacer casteo de int a float y de float a int, pero no se puede hacer casteo de str a int o float
#str(aqui va el numero)  int(aqui va la letra)  float(aqui va la letra)  bool(aqui va la letra)