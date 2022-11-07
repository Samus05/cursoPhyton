'''Ejercicio 1
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.'''


palabra=input("Escribe la primer palabra: ")
palabra2=input("Escribe la segunda palabra: ")

if palabra[-3:]==palabra2[-3:]:
    print("RIMA")
elif palabra[-2:]==palabra2[-2:]:
    print("RIMA UN POCO")
else:
    print("NO RIMA")


'''Ejercicio 2
Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul.
 Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a 
 ninguno de los candidatos disponibles, indicar “Opción errónea”.
Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula'''

candidato=input("Elija por que candidato quiere votar\nA candidato rojo\nB candidato verde\nC candidato azul\n...: ")

if candidato.upper()=="A" or candidato.upper()=="B" or candidato.upper()=="C":
    if candidato.upper()=="A":
        print("votaste por el partido rojo")
    elif candidato.upper()=="B":
        print("votaste por le candidato verde")
    else:
        print("votaste por le candidato azul")
else:
    print("opcion no reconocida")
    