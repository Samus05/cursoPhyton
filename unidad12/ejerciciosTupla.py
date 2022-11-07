'''Ejercicios
Ejercicio 1
Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla'''

import string


meses=('Enero','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic')
mes=int(input('escribe el numero del mes que quieres: '))
if mes<=12:
    print(meses[mes-1])
else:
    print('Escribe un numero entre el 1 y 12 ')

'''Ejercicio 2
Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa'''

alfabeto=string.ascii_uppercase
tuplaAlfabeto=(alfabeto)
print(len(tuplaAlfabeto))
numeroLetra=int(input('Ingresa el numero de la latra que quieres entre 1 y 26: '))
if numeroLetra<=26:
    print(tuplaAlfabeto[numeroLetra-1])
else:
    print('Ingresa el numero de la latra que quieres entre 1 y 26')
