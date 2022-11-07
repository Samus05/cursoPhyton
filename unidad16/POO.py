class FabricaConsolas():
    def __init__(self, marca, *colores, **modelos):
        self.colores=colores
        self.marca=marca
        self.modelos=modelos
consola=FabricaConsolas('nintendo','negro','blanco','rojo', gameboy=1000, nes=500, superNintendo=2000)
print(consola.marca)
print(consola.colores)
print(consola.modelos)
#atributo temporal fuera de la clase
consola.edicion='digital'
print(consola.edicion)