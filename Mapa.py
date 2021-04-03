from io import open

class Mapa():
	mapa = []
	marcas = []

	def abrirArchivo(self, archivo):
		fichero = open(archivo,"r")
		#CREA LA LISTA DEL MAPA
		while True:
			linea = fichero.readline()
			if not linea:
				break
			linea.rstrip("\n")
			linea = list(linea.split())
			self.mapa.append([int(x) for x in linea])

		#CREA LA LISTA DE MARCAS DE CADA POSICION
		for lista in self.mapa:
			lista_marcas = []
			for i in range(len(lista)):
				#SE PODRIA CREAR UN OBJETO CELDA EN LUGAR DE UN DICCIONARIO
				lista_marcas.append({"V":0,"O":0,"I":0,"X":0})
			self.marcas.append(lista_marcas)
		fichero.close()

	def mostrarValor(self):
		#MOSTRAR VALOR
		fila = int(input("Fila: "))
		columna = int(input("Columna: "))
		print(self.mapa[fila][columna])

	def cambiarValor(self):
		#CAMBIAR VALOR
		fila = int(input("Fila: "))
		columna = int(input("Columna: "))
		terreno = int(input("Nuevo terreno: "))
		self.mapa[fila][columna] = terreno
