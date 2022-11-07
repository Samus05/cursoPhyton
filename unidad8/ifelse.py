edad=5
if edad>=18:
    print("eres mayor de edad")
else:
    print("Tu no eres mayor de edad")

#Elif
letra=input("escribe una vocal: ")

if letra.lower()=="a"or letra.lower=="e" or letra.lower=="i" or letra.lower=="o" or letra.lower=="u":
    if letra.lower()=="a":
        print("esta vocal es la A")
    elif letra.lower()=="e":
        print("esta es la letra E")
    elif letra.lower()=="i":
        print("esta es la letra I")
    elif letra.lower()=="o":
        print("esta es la letra O")
    else:
        print("esta es la letra U")
else:
    print("esta no es una vocal")