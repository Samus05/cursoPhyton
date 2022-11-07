class A():
    def primera(self):
        return "Clase A metodo primera"
class B():
    def segunda(self):
        return "Clase B metodo segunda"

class C(A,B):
    pass

c=C()
print(c.primera())