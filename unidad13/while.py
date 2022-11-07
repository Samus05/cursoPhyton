i=0
while i<=5:
    print(i)
    i+=1
'''Ejercicio 1
Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero
Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).'''
i=1
tabla=int(input('escribe el numero entre el 1 y 9 para ver su tabla de multiplicar: '))
while i<=10:
    print('{} x {} = {}'.format(tabla,i,tabla*i))
    i+=1
edad=int(input('escribe tu edad: '))
i=1
while i<=edad:
    print(i)
    i+=1