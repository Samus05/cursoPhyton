class A ():
    def __init__(self, cuenta=0):
        self._cuenta=cuenta
        self._contador=0
   
    @property
    def cuenta(self):
        print('metodo get :)')
        return self._cuenta

    @cuenta.setter
    def cuenta(self, cuenta):
        print('metodo set :)')
        self._cuenta=cuenta

    @property
    def contador(self):
        return self._contador

a=A()
print(a.cuenta)
print(a.contador)

a.cuenta=10
#print(a.cuenta)