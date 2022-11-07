'''Ejercicios
Ejercicio 1
Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas

Ejercicio 2
Escribir una función que reciba un número entero positivo y devuelva su factorial.'''
lista = []

def agregar ():
    i=1
    while i<=10:
        lista.append(int(input("ingresa un numero: ")))
        i+=1
    print("esta es tu lista: \n", lista)



def orden ():
    par=[]
    inpar=[]
    for j in range(1,10):
        numero=lista[j-1]%2
        print(numero)
        if numero==0:
            par.append(lista[j-1])
        else:
            inpar.append(lista[j-1])
        
    print("Esta es tu lista de numeros pares: \n", par)
    print("Esta es tu lista de numero inpares: \n", inpar)


#ejercicio2
def factorial():
    numero=int(input("Escribe un numero entero: "))
    factorial=1
    i=1
    while i <= numero:
        factorial=factorial*i
        i+=1
    print("el factorial de {} es {}".format(numero,factorial))






#agregar()
#orden()
#factorial()




#print(lista)