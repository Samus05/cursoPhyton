'''En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario,
 se debe mostrar un mensaje diciendo que ese pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}'''

capitales={"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", 
"Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", 
"España": "Madrid"}

print(capitales)
pais=input("escribe el pais que deseas conocer su capital: ")

letra=pais.title() in capitales
print(letra)

if letra==True:
	print(capitales[pais.title()])
else:
	print("el pais no se encuentra en el diccionario")
	print(pais.capitalize())

'''
Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número; el programa debe imprimir el jugador al que hace referencia ese número
{
    1 : "Casillas", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa"
}
'''
jugadores={ 1 : "Casillas", 15 : "Ramos",3 : "Pique", 5 : "Puyol",11 : "Capdevila", 14 : "Xabi Alonso",16 : "Busquets", 8 : "Xavi Hernandez",18 : "Pedrito", 6 : "Iniesta",7 : "Villa"}
numero=int(input('Dame un numero de un jugador del barcelona: '))
valida=numero in jugadores
print(valida)

if valida==True:
	print('el jugador con el numero {} es '.format(numero),jugadores[numero])
else:
	print('el numero no pertenece a ningun jugador del barcelona')