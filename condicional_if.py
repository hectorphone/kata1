"""
a=10
b=100

print(a<b)#False
print(a>b)#True
print(a==b)#False
print(a!=b)#True
"""
#condicional
#if a > b:
#    print("'a' es mayor que 'b'")

"""
if a > b:
    print("a es mayor que b")
else:
    print("a es menor o igual que b")
"""
"""
dia = "Viernes"

if dia == "Martes":
    print("Hoy es martes")  
elif dia == "Miércoles":
    print("Hoy es miércoles")
elif dia == "Jueves":
    print("Hoy es jueves")
elif dia == "Viernes":
    print("Hoy es viernes")
else:
    print("No se sabe que día es hoy")
"""
usurio=None
password=None

usuario = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

#Hectorphone@gmail.com y hector1234 credenciales correctas
#son operadores logicos and, or, not
if usuario == "Hectorphone@gmail.com" and password == "hector1234":
    print("Bienvenido al sistema")
else:
    print("Usuario o contraseña incorrectos")