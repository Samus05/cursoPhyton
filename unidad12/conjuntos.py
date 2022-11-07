#conjunto={} *sin la estructura de un diccionartio {:}
#conjunto=set([])
#conjunto=set(()) *sel poner set() lo inicializa como un conjunto
conjunto={1,2,3,4,5,6,7,8,9}
print(type(conjunto))
conjunto=set([1,2,3,4,5,6,7,8,9])
print(type(conjunto))
conjunto=set((1,2,3,4,5,6,7,8,9))
print(type(conjunto))


#Metodos de conjunto
conjunto={1,1,2,2,3,4,5}
lista=[1,1,2,3,4,4]
print(lista)
print(conjunto)
#al imprimir los conjuntos no muetran los datos repetidos

conjunto={1,2,3,4,5,6,7,8,9}
print(conjunto)
print(conjunto.pop())