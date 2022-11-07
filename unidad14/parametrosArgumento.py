def suma ():
    num1=5
    num2=4
    suma=num1+num2
    return suma

#print(suma())

def sum (num1,num2):
    suma=num1+num2
    return suma

#print(sum(15,14))
#print(sum(13,12))


#variables globales

def valores():
    global num1
    global num2
    num1=100
    num2=50
    resultado=num1+num2
    return resultado



#print(valores() )
valores()
resta=num1-num2
#print(resta)

#parametro valor que le vamos a asignar a la funciona al crerla
#argumento es un valor que se le asigna a un parametro al mandar llamar a la funcion

def argumento (*dato):
    
    for i in dato:
        print(i)
    return type(dato)

print(argumento(5,'hola', 3.14))