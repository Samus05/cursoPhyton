class FabricaVideojuegos ():
    marca = "XBOX"
    color = "Blanco"
    edicion = "digital"
    alamacenamiento = "1TB"

    def actualizar(self , mensaje):
        return mensaje

    def reproducirNetflix(self):
        print("Estas viendo netflix")

consola = FabricaVideojuegos()
consola.marca
consola.color
consola.edicion

print(consola.actualizar("version 1.1"))
consola.reproducirNetflix()