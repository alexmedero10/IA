class Agente:

	def __init__(self):
		self.posicionX = 0
		self.posicionY = 0

	def mover(self,mapa,puntoX,puntoY):
		self.posicionX = puntoX
		self.posicionY = puntoY
		self.usarSensores(mapa)

	def usarSensores(self,mapa):
		if self.posicionY+1 < len(mapa.laberinto[self.posicionY]):
			mapa.laberinto[self.posicionX][self.posicionY+1].setColor()
		if self.posicionY > 0:
			mapa.laberinto[self.posicionX][self.posicionY-1].setColor()
		if self.posicionX > 0:
			mapa.laberinto[self.posicionX-1][self.posicionY].setColor()
		if self.posicionX+1 < len(mapa.laberinto):
			mapa.laberinto[self.posicionX+1][self.posicionY].setColor()

	def quitarMarcas(self,mapa):
		if self.posicionY+1 < len(mapa.laberinto[self.posicionY]):
				mapa.laberinto[self.posicionX][self.posicionY+1].quitarMarcas()
		if self.posicionY > 0:
				mapa.laberinto[self.posicionX][self.posicionY-1].quitarMarcas()
		if self.posicionX > 0:
				mapa.laberinto[self.posicionX-1][self.posicionY].quitarMarcas()
		if self.posicionX+1 < len(mapa.laberinto):
				mapa.laberinto[self.posicionX+1][self.posicionY].quitarMarcas()


	def setSensores(self,sensores):
		self.sensores = sensores

	def setVueltas(self,vueltas):
		self.vueltas = vueltas

	def setMovimientos(self,movimientos):
		self.movimientos = movimientos

	def setPosicion(self,x,y):
		self.posicionX = x
		self.posicionY = y


class Humano(Agente):
	def __init__(self):
		self.dificultad = {0:0,1:2,2:4,3:3,4:1}
		super().__init__()

class Mono(Agente):
	def __init__(self):
		self.dificultad = {0:0,1:2,2:4,3:3,4:1}
		super().__init__()

class Pulpo(Agente):
	def __init__(self):
		self.dificultad = {0:0,1:2,2:1,3:0,4:3}
		super().__init__()