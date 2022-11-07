from email.errors import MalformedHeaderDefect
from turtle import color


class FabricaConsolas():
    def __init__(self, marca, color):
        self.marca=marca
        self.color=color
        print('el objeto {} ha sido creado'.format(self.marca))
    def __str__(self):
        return 'El objeto es {} '.format(self.marca)
    
    def __del__(self):
        print('el objeto {} ha sido destruido'.format(self.marca))


consola=FabricaConsolas('xbox', 'blanco')
print(consola.marca)
print(consola)