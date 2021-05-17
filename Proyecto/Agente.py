class Agente:

	def __init__(self):
		self.posicionX = 0
		self.posicionY = 0
		self.costos = []

	def mover(self,mapa,puntoX,puntoY):
		self.posicionX = puntoX
		self.posicionY = puntoY

	def setSensores(self,sensores):
		self.sensores = sensores

	def setVueltas(self,vueltas):
		self.vueltas = vueltas

	def setMovimientos(self,movimientos):
		self.movimientos = movimientos

	def setPosicion(self,x,y):
		self.posicionX = x
		self.posicionY = y

	def setCostos(self,costos):
		self.costos.append(costos)


class Humano(Agente):
	def __init__(self):
		self.dificultad = {0:0,1:1,2:2,3:3,4:4}
		super().__init__()

class Mono(Agente):
	def __init__(self):
		self.dificultad = {0:0,1:2,2:4,3:3,4:1}
		super().__init__()

class Pulpo(Agente):
	def __init__(self):
		self.dificultad = {0:0,1:2,2:1,3:0,4:3}
		super().__init__()