from tkinter import *
from tkinter import messagebox
class Celda:

	def __init__(self,label,terreno,marcas,X,Y):
		self.label = label
		self.terreno = terreno
		self.marcas = marcas
		self.puntoX = X
		self.puntoY = Y
		self.distancia = 0
		self.costo = 0
		self.sumaDC = 0

	def calcular(self,agente,puntoFX,puntoFY,costoAnterior,mapa):
		self.distancia = abs(self.puntoX-puntoFX)+abs(self.puntoY-puntoFY)
		if mapa.laberinto[self.puntoX][self.puntoY].marcas['I'] != 'I':
			self.costo = agente.dificultad[self.terreno]+costoAnterior
		self.sumaDC = self.distancia + self.costo
		#Se marca el nodo como abierto
		self.setMarcas({"O":1})

	def mostrarValor(self,ventanaDatos):
		ventanaDatos.destroy()
		messagebox.showinfo("Valor",str(self.terreno))

	def cambiarValor(self,valor,ventanaDatos):
		ventanaDatos.destroy()
		self.terreno = valor
		self.setColor()

	def setMarcas(self, lista):
		if "V" in lista:
			if lista["V"] != 0:
				self.marcas["V"] = "V"

		if "O" in lista:
			if lista["O"] != 0:
				self.marcas["O"] = "O({})".format(self.sumaDC)
				lista["O"] = self.marcas["O"]
			else:
				self.marcas["O"] = 0

		if "C" in lista:
			if lista["C"] != 0:
				if lista["C"] == 2:
					self.marcas["C"] = "C({})".format(self.sumaDC)
				else:
					self.marcas["C"] = "C({})".format(self.sumaDC)
				lista["C"] = self.marcas["C"]

		if "X" in lista:
			if lista["X"] != 0:
				self.marcas["X"] = "X"
			else:
				self.marcas["X"] = 0

		if self.marcas["I"] == "I":
			lista["I"] = "I"
		if self.marcas["F"] == "F":
			lista["F"] = "F"
		if self.marcas["V"] == "V":
			lista["V"] = "V"

		x = ""
		self.label.configure(text=str([x+i for key,i in lista.items() if i!=0]))

	def quitarMarcas(self):
		self.marcas = {"V":0,"O":0,"I":0,"X":0,"F":0}
		self.label.configure(text="")

	def establecerInicio(self,ventanaDatos):
		ventanaDatos.destroy()
		self.marcas["I"] = "I"
		self.marcas["X"] = "X"
		self.label.configure(text="['{}','{}']".format(self.marcas["I"],self.marcas["X"]))
		self.setColor()

	def establecerFin(self,ventanaDatos):
		ventanaDatos.destroy()
		self.marcas["F"] = "F"
		self.label.configure(text="['{}']".format(self.marcas["F"]))
		self.setColor()

	def descubrirCelda(self,ventanaDatos):
		ventanaDatos.destroy()
		self.setColor()

	def setColor(self):
		if self.terreno == 0:
			self.label.configure(background="gray", borderwidth=2, relief="solid")
		elif self.terreno == 1:
			self.label.configure(background="green", borderwidth=2, relief="solid")
		elif self.terreno == 2:
			self.label.configure(background="blue", borderwidth=2, relief="solid")
		elif self.terreno == 3:
			self.label.configure(background="orange", borderwidth=2, relief="solid")
		elif self.terreno == 4:
			self.label.configure(background="darkgreen", borderwidth=2, relief="solid")
		elif self.terreno == 5:
			self.label.configure(background="purple", borderwidth=2, relief="solid")
		elif self.terreno == 6:
			self.label.configure(background="white", borderwidth=2, relief="solid")
		elif self.terreno == 8:
			self.label.configure(background="cyan", borderwidth=2, relief="solid")
		elif self.terreno == 9:
			self.label.configure(background="brown", borderwidth=2, relief="solid")

	def setColorOptimo(self):
		self.label.configure(background="white", borderwidth=2, relief="solid")

	def bloquearCelda(self,ventanaDatos):
		ventanaDatos.destroy()
		self.label.configure(background="black")

	def checarFinal(self):
		if self.marcas["F"] == "F":
			return 1

	def setLabel(self,color):
		self.label.configure(background=color)