from ast import Pow


a=int(input("introduce el valor de X cuadrada: "))
b=int(input("introduce el valor de X: "))
c=int(input("introduce el valor de la constante: "))

if ((b*(-1))+ ((b**2-(4*a*c))))<0:
    print("no se puede realizar")
else:
    resultado=((b*(-1))+ ((b**2-(4*a*c))**0.5))/(2*a)
    print("el resultado es: ")
    print("X1 = "+str(resultado))
    resultado=((b*(-1))- ((b**2-(4*a*c))**0.5))/(2*a)
    print("X2 = "+str(resultado))
