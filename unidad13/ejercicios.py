'''Ejercicios
Ejercicio 1
Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras
Ejercicio 2
Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares'''

tupla=(1,2,3,4,5,6,7,8,9,10)
print(tupla)
n1=int(input('escribe el primer numero: '))
n2=int(input('escribe el segundo numero: '))
if n1<n2:
    for i in range(n1,n2+1):
        print(i)
        i+=1
else:
    for j in range(n2,n1+1):
        print(n1)
        n1-=1

tupla=(1,2,3,4,5,6,7,8,9,10)
print(tupla)
n1=int(input('escribe el primer numero: '))
n2=int(input('escribe el segundo numero: '))
if n1<n2:
    for i in range(n1,n2+1):
        if i%2==0:
            continue
        print(i)
        i+=1
else:
    for j in range(n2,n1+1):
        if j%2==0:
            n1-=1
            continue
        print(n1-1)
        n1-=1