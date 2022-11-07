class Animales():

    def __init__(self , mensaje):
        self.mensaje=mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo hago guaoo")

class Pez(Animales):
    def hablar(self):
        print("Yo solo nado")

perro=Perro("wauWau")
perro.hablar()

animal=Animales("los animales no hablan")
animal.hablar()

pez=Pez("nada")
pez.hablar()