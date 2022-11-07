class Animales():
    def __init__(self, nombre):
        self.nombre =nombre
    @property
    def Nombre(self):
        print("metodo get")
        return self.nombre
class Perro(Animales):
    def __init__ (self,nombre, sonido):
        super().__init__(nombre)
        self.sonido=sonido

perro=Perro("Firulais", "Guaau")

print(perro.Nombre)
