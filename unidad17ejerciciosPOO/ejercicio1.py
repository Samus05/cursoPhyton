'''Ejercicio 1
Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.'''

class Alumno():
    def __init__(self, nombre, nota):
        self.nombre= nombre
        self.nota= nota

    @property
    def calificacion(self):
        return "La nota de {} es: {}".format(self.nombre, self.nota)
    
    @property
    def status(self):
        if self.nota>=6:
            return " Aprobado "
        else:
            return " Reprobado"

alumno=Alumno("Gerson",10)

print(alumno.calificacion)
print(alumno.status)
    
