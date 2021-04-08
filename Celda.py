from tkinter import *
from tkinter import messagebox
class Celda:

	def __init__(self,label,terreno,marcas):
		self.label = label
		self.terreno = terreno
		self.marcas = marcas

	def mostrarValor(self,ventanaDatos):
		ventanaDatos.destroy()
		messagebox.showinfo("Valor",str(self.terreno))

	def cambiarValor(self,valor,ventanaDatos):
		ventanaDatos.destroy()
		self.terreno = valor
		self.setColor()

	def setMarcas(self, lista):
		if lista["V"] != 0:
			self.marcas["V"] = "V"

		if lista["O"] != 0:
			self.marcas["O"] = "O"
		else:
			self.marcas["O"] = 0

		if lista["X"] != 0:
			self.marcas["X"] = "X"
		else:
			self.marcas["X"] = 0
		x = ""
		self.label.configure(text=str([x+key for key,i in lista.items() if i!=0]))

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

	def bloquearCelda(self,ventanaDatos):
		ventanaDatos.destroy()
		self.label.configure(background="black")

	def setLabel(self,color):
		self.label.configure(background=color)