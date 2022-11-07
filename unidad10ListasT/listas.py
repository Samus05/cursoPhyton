#lista =[] /// pueden ser homogeneas y heterogeneas ie del mismo tipo de datos o diferentes tipos de datos
lista= ['python',120,'nombre',4.14,6.28]
print(type(lista))
print(lista[3])
print(len(lista))
lista[0]='sam'
print(lista)

#metodos lista
lista=[1,2,3,4,5,6,7,8]
#append agrega un elemento al final de la lista
lista.append(33)
print(lista)
#clear liempia la lista
lista.clear()
print(lista)
lista.insert(2,88)
print(lista)

print(lista.count(88))