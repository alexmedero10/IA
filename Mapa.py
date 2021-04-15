class Mapa:
	
	def __init__(self):
		self.laberinto = []

	def bloquearMapa(self):
		for i in range(len(self.laberinto)):
			for celda in self.laberinto[i]:
				celda.setLabel("black")

	def borrarMarcas(self):
		for i in range(len(self.laberinto)):
			for celda in self.laberinto[i]:
				celda.quitarMarcas()

	def setLaberinto(self, laberinto):
		self.laberinto = laberinto
