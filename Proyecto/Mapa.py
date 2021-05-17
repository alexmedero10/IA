class Mapa:
	
	def __init__(self):
		self.laberinto = []

	def bloquearMapa(self):
		for i in range(len(self.laberinto)):
			for celda in self.laberinto[i]:
				celda.setLabel("black")

	def descubrirMapa(self):
		for i in range(len(self.laberinto)):
			for celda in self.laberinto[i]:
				celda.setColor()

	def borrarMarcas(self):
		for i in range(len(self.laberinto)):
			for celda in self.laberinto[i]:
				celda.quitaMarcas()

	def limpiarDatos(self):
		for i in range(len(self.laberinto)):
			for celda in self.laberinto[i]:
				celda.limpiaDatos()

	def setLaberinto(self, laberinto):
		self.laberinto = laberinto
