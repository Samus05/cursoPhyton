'''Ejercicio 1
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos.
Llamar a la clase Calculadora.

Ejercicio 2
Escribir una clase que se llame Areas(). A partir de un constructor se deben pasar los valores de Base y Altura. Luego, se debe calcular area de un cuadrado, triangulo y pentagono'''
import math
class Calculadora():
    def __init__(self):
        self.cifra1=int(input("El primer numero entero es: "))
        self.cifra2=int(input("el segundo numero entero es: "))
    
    def suma(self):
        self.suma = self.cifra1 + self.cifra2
        return "El resultado de la suma es: {}".format(self.suma)
    
    @property
    def getSuma(self):
        return "El resultado de la suma es: "+str(self.suma)
    
    def resta(self):
        self.resta=self.cifra1-self.cifra2
        return "el resultyado de la resta es : ",self.resta
    def multi(self):
        self.multi=self.cifra1*self.cifra2
        return "El resultado de la multiplicaion es: ",self.multi
    def div(self):
        self.div=self.cifra1/self.cifra2
        return "El resultado de la division es :",self.div

#calculadora=Calculadora()
#calculadora.suma()
#print(calculadora.getSuma)


class Areas():
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def areaCuadrado(self):
        self.areaCuadrado=self.base*self.base
        return self.areaCuadrado
    def areaTriangulo(self):
        self.areaTriagulo=(self.base*self.altura)/2
        return self.areaTriagulo
    def areaPentagono(self):
        self.apotema=self.base/(2*math.tan(3.1416/5))
        self.areaPentagono=((self.base*5)*self.apotema)/2
        return self.areaPentagono

areas=Areas(int(input("ingrese la base: ")),int(input("ingresa la altura: ")))
print(areas.areaCuadrado())
print(areas.areaTriangulo())
print(areas.areaPentagono())

