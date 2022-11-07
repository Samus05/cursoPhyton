'''Ejercicio 2
Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.
'''
p1=float(input("calificacion del primer parcial"))
p2=float(input("calificacion del segundo parcial"))
p3=float(input("calificacion del tercer parcial"))
Ep=float(input("calificacion examen parcial"))
ef=float(input("calificacion examen final"))

Promedio=(p1+p2+p3)/3
promedioFinal=(Promedio+ Ep*2 + ef*3)/6 

print(Promedio)
print(promedioFinal)

print("el promedio de las practicas es: \n",Promedio,"\n","el promedio final es:\n {}".format(promedioFinal))

'''Ejercicio 1
Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas'''

vocal=input("Escribe una vocal en minuscula: ")
letra=input("Escribe un letra en mayuscula: ")

print(vocal.upper(),letra.lower())

'''Ejercicio 2
Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:
Te llamas: <nombre>
Tu edad es: <edad>
Eres: <sexo>
'''
nombre=input("ingresa tu nombre: ")
edad=int(input("ingresa tu edad"))
sexo=input("ingresa tu sexo")


print("Te llamas:{} \nTu edad es: {}\nEres: {}".format(nombre,edad,sexo))