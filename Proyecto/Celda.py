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

	def calcular(self,agente,puntoFX,puntoFY,costoAnterior):
		self.distancia = abs(self.puntoX-puntoFX)+abs(self.puntoY-puntoFY)
		if costoAnterior != 0:
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
		"""
		if lista["O"] != 0:
			self.marcas["O"] = "O"
		else:
			self.marcas["O"] = 0

		if "X" in lista:
			if lista["X"] != 0:
				self.marcas["X"] = "X"
			else:
				self.marcas["X"] = 0
		"""
		if self.marcas["H"] == "H":
			lista["H"] = "H"
		if self.marcas["M"] == "M":
			lista["M"] = "M"
		if self.marcas["O"] == "O":
			lista["O"] = "O"
		if self.marcas["K"] == "K":
			lista["K"] = "K"
		if self.marcas["T"] == "T":
			lista["T"] = "T"
		if self.marcas["S"] == "S":
			lista["S"] = "S"
		if self.marcas["P"] == "P":
			lista["P"] = "P"
		
		x = ""
		if bool(lista):
			self.label.configure(text=str([x+key for key,i in lista.items() if i!=0]))
		else: self.label.configure(text="")


	def quitaMarcas(self):
		lista = {}
		self.marcas["V"] = 0
		self.marcas["A"] = 0
		self.marcas["C"] = 0
		if self.marcas["H"] == "H":
			lista["H"] = "H"
		if self.marcas["M"] == "M":
			lista["M"] = "M"
		if self.marcas["O"] == "O":
			lista["O"] = "O"
		if self.marcas["K"] == "K":
			lista["K"] = "K"
		if self.marcas["T"] == "T":
			lista["T"] = "T"
		if self.marcas["S"] == "S":
			lista["S"] = "S"
		if self.marcas["P"] == "P":
			lista["P"] = "P"

		x = ""
		if bool(lista):
			self.label.configure(text=str([x+key for key,i in lista.items() if i!=0]))
		else: self.label.configure(text="")


	def establecerPunto(self,ventanaDatos,letra):
		ventanaDatos.destroy()
		self.marcas[letra] = letra
		self.label.configure(text="['{}']".format(self.marcas[letra]))

	def descubrirCelda(self,ventanaDatos):
		ventanaDatos.destroy()
		self.setColor()

	def setColor(self):
		if self.terreno == 0:
			self.label.configure(background="black", borderwidth=2, relief="solid")
		elif self.terreno == 1:
			self.label.configure(background="pink", borderwidth=2, relief="solid")
		elif self.terreno == 2:
			self.label.configure(background="blue", borderwidth=2, relief="solid")
		elif self.terreno == 3:
			self.label.configure(background="yellow", borderwidth=2, relief="solid")
		elif self.terreno == 4:
			self.label.configure(background="green", borderwidth=2, relief="solid")

	def bloquearCelda(self,ventanaDatos):
		ventanaDatos.destroy()
		self.label.configure(background="black")

	def limpiaDatos(self):
		self.distancia = 0
		self.costo = 0
		self.sumaDC = 0

	def setLabel(self,color):
		self.label.configure(background=color)