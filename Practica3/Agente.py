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
				mapa.laberinto[self.posicionX][self.posicionY+1].setMarcas({"V":0,"O":0,"X":0})
		if self.posicionY > 0:
				mapa.laberinto[self.posicionX][self.posicionY-1].setMarcas({"V":0,"O":0,"X":0})
		if self.posicionX > 0:
				mapa.laberinto[self.posicionX-1][self.posicionY].setMarcas({"V":0,"O":0,"X":0})
		if self.posicionX+1 < len(mapa.laberinto):
				mapa.laberinto[self.posicionX+1][self.posicionY].setMarcas({"V":0,"O":0,"X":0})


	def setSensores(self,sensores):
		self.sensores = sensores

	def setVueltas(self,vueltas):
		self.vueltas = vueltas

	def setMovimientos(self,movimientos):
		self.movimientos = movimientos

	def setPosicion(self,x,y):
		self.posicionX = x
		self.posicionY = y


class Mono(Agente):
	def __init__(self):
		self.dificultad = {0:0,1:2,2:4,3:3,4:1}

class Pulpo(Agente):
	def __init__(self):
		self.dificultad = {0:0,1:2,2:1,3:0,4:3}