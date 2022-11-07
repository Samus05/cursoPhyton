'''Ejercicio 1
Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal'''
variable=input("Escribe una letra: ")
variable=variable.lower()

if variable=="a" or variable=="e" or variable=="i" or variable=="o" or variable=="u":
    print("ES VOCAL")
else:
    print("NO ES VOVAL")

numero=input("escribe un numero: ")
print(type(numero))
numero=int(numero)
#print(numero)
if numero>=0:
    print(numero)
else:
    numero=numero*-1
    print(numero)