class Animales():
    def habla(self):
        print("Yo soy un animal")
    
    def descripcion(self):
        print('Yo soy un {}'.format(self.animal))

class Gato(Animales):
    pass

class Perro(Animales):
    def __init__(self , animal):
        self.animal =animal


gato = Gato()
animal=Animales()
animal.habla()
gato.habla()


perro=Perro("Perro")
perro.descripcion()
