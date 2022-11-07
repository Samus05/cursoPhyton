'''Ejercicios
Ejercicio 1
Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio
Ejercicio 2
Escribir una función que reciba una muestra de números en una lista y devuelva su medida.'''


def areaCuadrado(base, altura):
    areaC=base*altura
    return areaC

def areaCirculo(radio):
    areaCir=3.1416*(radio**2)
    return areaCir

#print(areaCuadrado(int(input("Ingresa las medidas de dos lados del cuadrado: ")),int(input("Ingresa las medidas de dos lados del cuadrado: "))))
#print(areaCirculo(int(input("ingresa el radio del circulo"))))

def muestra(*datos):
    print(len(datos))
    return len(datos)

print(muestra(1,5,7,9,4,6))