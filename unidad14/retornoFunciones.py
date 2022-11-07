def entero():
    print('Este es un dato entero: ')
    return 33


def decimal ():
    print('este es un dato decimal: ')
    return 3.14


def frase():
    return "mi nombre es samuel"

def asignacion():
    return 1,2,3,4,5


print(entero())
print(decimal())
print(frase())

a,b,c,d,e = asignacion()

print(a)
print(e)