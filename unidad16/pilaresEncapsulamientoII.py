class A():
    def __init__(self):
        self._contador=0
        self._cuenta=0
    def incrementar(self):
        self._contador+=1
    def cuenta(self):
        return self._contador
#al poner los atributos con solo un guion bajo etsamos indicando que esta encapsulado, sin embargo, si podremos seguir accediendo a ellos y modificando su valor // auue esto no es un apractica correcta ya que se utilizan metodos get y set

#esto de abajo esta mal y es solo para ejmplificar a pesar de que funciona
a=A()
print(a.cuenta)
a.cuenta=20
print(a.cuenta)   