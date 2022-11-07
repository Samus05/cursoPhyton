'''Ejercicio 1
Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0
Ejercicio 2
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
 y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.'''




def numero():
    num1=int(input('Ingresa dos numeros: \nEl primer numero: '))
    num2=int(input('El segundo numero: '))
    if num1>num2:
        return 1
    elif num2>num1:
        return -1
    elif num1==num2:
        return 0
    else:
        print("ingrese dos numeros validos")
#print(numero())

def factura():
    valor=float(input('Ingrese el valor de la factura: '))
    iva=(input('Ingrese el porcentaje de iva a aplicar: '))
    
    print(len(iva))
    if len(iva)== 0:
        valor*=1.21
        return valor
    else:
        valor*=(1+((float(iva)/100)))
        return valor

print(factura())