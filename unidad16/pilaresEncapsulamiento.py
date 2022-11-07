class A():
    def __init__(self):
        self.contador=0
    def incrmenetar(self):
        self.contador+=1
    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self.__contador=0
    def incrmenetar(self):
        self.__contador+=1
    def cuenta(self):
        return self.__contador

print('objeto A')
a = A()
print(a.cuenta())
a.incrmenetar()
print(a.cuenta())
print("objetoB")
b =B()
print(b.cuenta())
b.incrmenetar()
print(b.cuenta())
#Esta linea nos dara error porque el atributo __contador esta encapsulado en la clase B y solo puede ser usado en la clase B a diferencia de la clase A que tiene atributos publicos
print(b.__contador)
