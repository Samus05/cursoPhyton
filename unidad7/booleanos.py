from operator import truediv


verdadero= True
falso=False
print(type(verdadero))
print(type(falso))

#operadores comparativos
num1=100
num2=500
print("num1={} y num2={}".format(str(num1),str(num2)))
print("es num1>num2: ",num1>num2)
print("es num2>num1: ",num2>num1)
print("es num1 diferente de  num2: ", num1!=num2)
print("es num1 mayor igual a num2: ",num1>=num2)
print("es num1 menor igual que num2:",num1<=num2)
print("es num1 igual a num2:",num1==num2)

cadena="hola"
cadena1="hola sam"
print("cadena={} \n cadena1={}".format(cadena,cadena1))
print("cadena es mas grande que cadena1: ",cadena>cadena1)

#operadores logicos
print('operadores "logicos"')
print(100==100 and 8<9)
print(50!=100 or 1==1)
print(not 50==50)

#metodos booleanos

cadena="Estoy mostrando los metodos booleanos para las strings"
print(cadena.startswith("E"),cadena.endswith("s"), cadena.islower(), cadena.find("E"))
