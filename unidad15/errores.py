while True:
    try:
        edad=int(input("Ingresa tu edad: "))
        print("tu edad es :",edad)
        break
    except:
        print("ingresaste un valor erroneo")
    finally:
        print("FIN")

while True:
    try:
        edad=int(input("Ingresa tu edad: "))
        break
    except ValueError:
        print(ValueError)