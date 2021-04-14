class Agente:
	sensores = {}
	vueltas = {}
	movimientos = {}
	posicionX = 0
	posicionY = 0
	vista = "Arriba"

	def voltear(self):
		if self.vueltas["R"] == 1:
			mapa.laberinto[self.posicionX][self.posicionY].setMarcas({"V":0,"O":1,"X":0})
		if self.vueltas["L"] == 1:
			mapa.laberinto[self.posicionX][self.posicionY].setMarcas({"V":0,"O":1,"X":0})

	def mover(self,mapa,direccion):
		if direccion == "R":
			if self.movimientos["R"] == 1:
				if self.posicionY+1 < len(mapa.laberinto[self.posicionY]):
					mapa.laberinto[self.posicionX][self.posicionY+1].setMarcas({"V":0,"O":0,"X":1})
					mapa.laberinto[self.posicionX][self.posicionY].setMarcas({"V":1,"O":0,"X":0})
					self.posicionY = self.posicionY+1
		elif direccion == "L":
			if self.movimientos["L"] == 1:
				if self.posicionY > 0:
					mapa.laberinto[self.posicionX][self.posicionY-1].setMarcas({"V":0,"O":0,"X":1})
					mapa.laberinto[self.posicionX][self.posicionY].setMarcas({"V":1,"O":0,"X":0})
					self.posicionY = self.posicionY-1
		elif direccion == "F":
			if self.movimientos["F"] == 1:
				if self.posicionX > 0:
					mapa.laberinto[self.posicionX-1][self.posicionY].setMarcas({"V":0,"O":0,"X":1})
					mapa.laberinto[self.posicionX][self.posicionY].setMarcas({"V":1,"O":0,"X":0})
					self.posicionX = self.posicionX-1
		elif direccion == "B":
			if self.movimientos["B"] == 1:
				if self.posicionX+1 < len(mapa.laberinto):
					mapa.laberinto[self.posicionX+1][self.posicionY].setMarcas({"V":0,"O":0,"X":1})
					mapa.laberinto[self.posicionX][self.posicionY].setMarcas({"V":1,"O":0,"X":0})
					self.posicionX = self.posicionX+1
		


	def usarSensores(self,mapa):
		if self.sensores["R"] == 1:
			if self.posicionY+1 < len(mapa.laberinto[self.posicionY]):
				mapa.laberinto[self.posicionX][self.posicionY+1].setColor()
				mapa.laberinto[self.posicionX][self.posicionY+1].setMarcas({"V":0,"O":1,"X":0})
		if self.sensores["L"] == 1:
			if self.posicionY > 0:
				mapa.laberinto[self.posicionX][self.posicionY-1].setColor()
				mapa.laberinto[self.posicionX][self.posicionY-1].setMarcas({"V":0,"O":1,"X":0})
		if self.sensores["U"] == 1:
			if self.posicionX > 0:
				mapa.laberinto[self.posicionX-1][self.posicionY].setColor()
				mapa.laberinto[self.posicionX-1][self.posicionY].setMarcas({"V":0,"O":1,"X":0})
		if self.sensores["D"] == 1:
			if self.posicionX+1 < len(mapa.laberinto):
				mapa.laberinto[self.posicionX+1][self.posicionY].setColor()
				mapa.laberinto[self.posicionX+1][self.posicionY].setMarcas({"V":0,"O":1,"X":0})

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
		self.dificultad = {}

class Mono(Agente):
	def __init__(self):
		self.dificultad = {}

class Pulpo(Agente):
	def __init__(self):
		self.dificultad = {}

class PieGrande(Agente):
	def __init__(self):
		self.dificultad = {}