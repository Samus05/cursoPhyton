'''Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas,
 color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno'''

class Fabrica():
    def __init__(self,llantas,color,precio):
        self.llantas=llantas
        self.color=color
        self.precio=precio

class Moto(Fabrica):
    def caracteristicas(self):
        print("el numero de llantas es: ",self.llantas,"\nel color de la Moto es: ",self.color,"\nel precio de la moto es: ",self.precio)


class Carro(Fabrica):
    def caracteristicas(self):
        print("el numero de llantas es: ",self.llantas,"\nel color del carro es: ",self.color,"\nel precio del carro es: ",self.precio)
    
#fabrica=Fabrica()
moto=Moto(2,'azul','99000')
moto.caracteristicas()
