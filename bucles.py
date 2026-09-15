#while se repite en bloque de codigo mientras la condicion sea verdadera
"""
seguir = True

while seguir:
    print("esto es el bucle while")
    fin = input("Desea salir del bucle? (s/n): ")
    if fin == "n":
        seguir = False
        print("esto se acabo")


#while con else
nombre = "Juana"
while nombre == "Maria":
    print("hola ", nombre)
else:
    print("nombre no es Maria")
"""


x=0
while x < 100:
    
    x += 1
    print(x)

#se repite mientras se cumpla en numero de iteraciones definidas
#dentro del propio for variable range(inicio, final(el numero dado menos uno, salto(opcional)))

for iteracion in range(1,21):
    print(iteracion)


#realizar un programa que muestre segun la opcion +(suma), -(resta), *(multiplicacion), /(division) 
#de dos numeros ingresados por el teclado , nos pedira ingrese el primer numero, ingrese el segundo,
#ingrese la operacion, el programa debe para solo si al final de la operacion escribo la palabra salir
