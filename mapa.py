from io import open

archivo = input("Nombre del archivo: ")
fichero = open(archivo,"r")

mapa = []
marcas = []
#CREA LA LISTA DEL MAPA
while True:
	linea = fichero.readline()
	if not linea:
		break
	linea.rstrip("\n")
	linea = list(linea.split())
	mapa.append([int(x) for x in linea])

#CREA LA LISTA DE MARCAS DE CADA POSICION
for lista in mapa:
	lista_marcas = []
	for i in range(len(lista)):
		#SE PODRIA CREAR UN OBJETO CELDA EN LUGAR DE UN DICCIONARIO
		lista_marcas.append({"V":0,"O":0,"I":0,"X":0})
	marcas.append(lista_marcas)

#MOSTRAR VALOR
fila = int(input("Fila: "))
columna = int(input("Columna: "))
print(mapa[fila][columna])

#CAMBIAR VALOR
fila = int(input("Fila: "))
columna = int(input("Columna: "))
terreno = int(input("Nuevo terreno: "))
mapa[fila][columna] = terreno

fila = int(input("Fila: "))
columna = int(input("Columna: "))
print(mapa[fila][columna])


fichero.close()