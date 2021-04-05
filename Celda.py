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

	def descubrirCelda(self,ventanaDatos):
		ventanaDatos.destroy()
		self.setColor()

	def setColor(self):
		if self.terreno == 0:
			self.label.configure(background="blue", borderwidth=2, relief="solid")
		elif self.terreno == 1:
			self.label.configure(background="red", borderwidth=2, relief="solid")
		elif self.terreno == 2:
			self.label.configure(background="green", borderwidth=2, relief="solid")
		elif self.terreno == 3:
			self.label.configure(background="pink", borderwidth=2, relief="solid")
		elif self.terreno == 4:
			self.label.configure(background="orange", borderwidth=2, relief="solid")

	def bloquearCelda(self,ventanaDatos):
		ventanaDatos.destroy()
		self.label.configure(background="black")

	def setLabel(self,color):
		self.label.configure(background=color)
