'''Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad).
 Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante).
 Una ultima llamada Estudiante, que tenga como atributos su nombre y edad.
 El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.'''

class Universidad():
    def __init__(self):
        self.nombre="IPN"
class Carrera():
    def carrera(self):
        self.especialidad="ESFM"

class Estudiante(Universidad,Carrera):
    def estudiante (self):

        self.nombreEst="Sam Loz"
        self.edad=10

        print("el estudiante {} estudia en la universidad {} con especialidad {} y tiene {} años".format(self.nombreEst,self.nombre,self.especialidad,self.edad))

#class Persona(Universidad,Carrera,Estudiante):
#   def datos (self):
#       print("el estudiante {} estudia en la universidad {} con especialidad {} y tiene {} años".format(self.nombreEst,self.nombre,self.especialidad,self.edad))

persona=Estudiante()
persona.carrera()
persona.estudiante()