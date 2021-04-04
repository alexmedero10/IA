class Mapa:
	
	def __init__(self):
		self.laberinto = []

	def bloquearMapa(self):
		for i in range(len(self.laberinto)):
			for celda in self.laberinto[i]:
				celda.setLabel("black")

	def mostrarValor(self):
		#MOSTRAR VALOR
		fila = int(input("Fila: "))
		columna = int(input("Columna: "))
		print(self.laberinto[fila][columna])

	def cambiarValor(self):
		#CAMBIAR VALOR
		fila = int(input("Fila: "))
		columna = int(input("Columna: "))
		terreno = int(input("Nuevo terreno: "))
		self.laberinto[fila][columna] = terreno

	def setLaberinto(self, laberinto):
		self.laberinto = laberinto
