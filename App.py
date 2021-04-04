from tkinter import *
from tkinter import messagebox
from io import open
from Celda import *
from Mapa import *

class App:
	lista = []
	mapa = Mapa()

	def __init__(self):
		self.root = Tk()
		self.root.title("Laberinto")
		self.root.geometry('500x500')
		self.root.resizable(1,1)

		self.menubar = Menu(self.root)
		self.root.config(menu=self.menubar)

		self.filemenu = Menu(self.menubar,tearoff=0)
		self.filemenu.add_command(label="Crear tablero",command=self.pedirArchivo)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Bloquear mapa",command=self.mapa.bloquearMapa)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Bloquear celda",command=self.pedirCeldaBloquear)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Descubir celda",command=self.pedirCeldaDescubir)

		self.menubar.add_cascade(label="ACTIONS",menu=self.filemenu)
		self.root.mainloop()

	def abrirArchivo(self, file,ventanaDatos):
		ventanaDatos.destroy()
		fichero = open(file,"r")
		#CREA LA LISTA DEL MAPA
		laberinto = []
		while True:
			linea = fichero.readline()
			if not linea:
				break
			linea.rstrip("\n")
			linea = list(linea.split())
			laberinto.append([int(x) for x in linea])

		self.mapa.setLaberinto(laberinto)
		fichero.close()
		self.crearTablero()

	def crearTablero(self):

		for i in self.root.grid_slaves():
			i.grid_remove()
			print(i.grid_info())

		self.lista.clear()
		for i in range(len(self.mapa.laberinto)):
			self.root.rowconfigure(i, weight=1)

		for j in range(len(self.mapa.laberinto[0])):
			self.root.columnconfigure(j, weight=1)

		for i in range(len(self.mapa.laberinto)):
			for j in range(len(self.mapa.laberinto[i])):
				linea = Celda(Label(self.root,text="{},{}".format(i,j)),self.mapa.laberinto[i][j],{"V":0,"O":0,"I":0,"X":0})
				if self.mapa.laberinto[i][j] == 0:
					linea.label.configure(background="blue", borderwidth=2, relief="solid")
				elif self.mapa.laberinto[i][j] == 1:
					linea.label.configure(background="red", borderwidth=2, relief="solid")
				if self.mapa.laberinto[i][j] == 2:
					linea.label.configure(background="green", borderwidth=2, relief="solid")
				if self.mapa.laberinto[i][j] == 3:
					linea.label.configure(background="pink", borderwidth=2, relief="solid")
				if self.mapa.laberinto[i][j] == 4:
					linea.label.configure(background="orange", borderwidth=2, relief="solid")
				linea.label.grid(row=i,column=j,sticky=S+N+E+W)
				self.mapa.laberinto[i][j] = linea


	def pedirArchivo(self):
		self.root.deiconify()
		ventanaDatos = Toplevel()
		ventanaDatos.title("Laberinto")
		ventanaDatos.resizable(1,1)
		ventanaDatos.geometry('380x300')
		ventanaDatos.configure(background="dark turquoise")

		d1 = StringVar()
		Entry(ventanaDatos,justify="center",textvariable=d1).grid(row=0,column=0)
		
		Button(ventanaDatos,text="Crear",command=lambda:self.abrirArchivo(str(d1.get()),ventanaDatos)).grid(row=0,column=2)

	def pedirCeldaBloquear(self):
		self.root.deiconify()
		ventanaDatos = Toplevel()
		ventanaDatos.title("Laberinto")
		ventanaDatos.resizable(1,1)
		ventanaDatos.geometry('380x300')
		ventanaDatos.configure(background="dark turquoise")

		d1 = StringVar()
		Entry(ventanaDatos,justify="center",textvariable=d1).grid(row=0,column=0)

		d2 = StringVar()
		Entry(ventanaDatos,justify="center",textvariable=d2).grid(row=0,column=1)
		
		Button(ventanaDatos,text="Crear",command=lambda:self.mapa.laberinto[int(d1.get())][int(d2.get())].bloquearCelda(ventanaDatos)).grid(row=0,column=2)

		
	def pedirCeldaDescubir(self):
		self.root.deiconify()
		ventanaDatos = Toplevel()
		ventanaDatos.title("Laberinto")
		ventanaDatos.resizable(1,1)
		ventanaDatos.geometry('380x300')
		ventanaDatos.configure(background="dark turquoise")

		d1 = StringVar()
		Entry(ventanaDatos,justify="center",textvariable=d1).grid(row=0,column=0)

		d2 = StringVar()
		Entry(ventanaDatos,justify="center",textvariable=d2).grid(row=0,column=1)
		
		Button(ventanaDatos,text="Crear",command=lambda:self.mapa.laberinto[int(d1.get())][int(d2.get())].descubrirCelda(ventanaDatos)).grid(row=0,column=2)


app = App()