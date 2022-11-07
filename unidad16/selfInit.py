'''class FrabricaConsolas():
    marca = "XBOX"

    def cosntruirSwitch(self):
        self.marca = "Nintendo"
        self.color = "rojo"

consola=FrabricaConsolas()
consola.cosntruirSwitch()

print(consola.marca,consola.color)'''


class FabricaConsolas():
    def __init__(self, marca, color):
        self.marca=marca
        self.color=color
       

consola=FabricaConsolas('xbox','blanco')

print(consola.marca,consola.color)

