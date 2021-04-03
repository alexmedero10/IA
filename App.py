from tkinter import *
from tkinter import messagebox
from Celda import *
from Mapa import *

class App():
	lista = []

	def __init__(self):
		self.root = Tk()
		self.root.title("Laberinto")
		self.root.geometry('500x500')
		self.root.resizable(1,1)

		self.menubar = Menu(self.root)
		self.root.config(menu=self.menubar)

		self.filemenu = Menu(self.menubar,tearoff=0)
		self.filemenu.add_command(label="ALL BLOCKED",command=self.bloquearMapa)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Crear tablero",command=self.pedirArchivo)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Bloquear celda",command=self.pedirCeldaBloquear)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Descubir celda",command=self.pedirCeldaDescubir)

		self.menubar.add_cascade(label="ACTIONS",menu=self.filemenu)

		self.root.mainloop()


	def crearTablero(self,file,ventanaDatos):
		ventanaDatos.destroy();
		Mapa.mapa.clear()
		Mapa.marcas.clear()
		Mapa.abrirArchivo(Mapa,str(file.get()));
		
		for i in self.root.grid_slaves():
			i.grid_remove()
			print(i.grid_info())

		self.lista.clear()
		for i in range(len(Mapa.mapa)):
			self.root.rowconfigure(i, weight=1)

		for j in range(len(Mapa.mapa[0])):
			self.root.columnconfigure(j, weight=1)

		for i in range(len(Mapa.mapa)):
			linea = []
			for j in range(len(Mapa.mapa[i])):
				linea.append(Label(self.root,text="{},{}".format(i,j)))
				if Mapa.mapa[i][j] == 0:
					linea[j].configure(background="blue", borderwidth=2, relief="solid")
				elif Mapa.mapa[i][j] == 1:
					linea[j].configure(background="red", borderwidth=2, relief="solid")
				if Mapa.mapa[i][j] == 2:
					linea[j].configure(background="green", borderwidth=2, relief="solid")
				if Mapa.mapa[i][j] == 3:
					linea[j].configure(background="pink", borderwidth=2, relief="solid")
				if Mapa.mapa[i][j] == 4:
					linea[j].configure(background="orange", borderwidth=2, relief="solid")
				linea[j].grid(row=i,column=j,sticky=S+N+E+W)
			self.lista.append(linea)

	def bloquearMapa(self):
		for i in range(len(Mapa.mapa)):
			linea = []
			for j in range(len(Mapa.mapa[i])):
				linea.append(Label(self.root,text="{},{}".format(i,j)))
				linea[j].configure(background="black", borderwidth=2, relief="solid")
				linea[j].grid(row=i,column=j,sticky=S+N+E+W)
			self.lista.append(linea)

	def pedirArchivo(self):
		self.root.deiconify()
		ventanaDatos = Toplevel()
		ventanaDatos.title("Laberinto")
		ventanaDatos.resizable(1,1)
		ventanaDatos.geometry('380x300')
		ventanaDatos.configure(background="dark turquoise")

		d1 = StringVar()
		Entry(ventanaDatos,justify="center",textvariable=d1).grid(row=0,column=0)
		
		Button(ventanaDatos,text="Crear",command=lambda:self.crearTablero(d1,ventanaDatos)).grid(row=0,column=2)

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
		
		Button(ventanaDatos,text="Crear",command=lambda:self.bloquearCelda(d1,d2,ventanaDatos)).grid(row=0,column=2)

	def bloquearCelda(self,n,m,ventanaDatos):
		ventanaDatos.destroy()
		try:
			n = int(n.get())
			m = int(m.get())
		except ValueError:
			messagebox.showerror("Error!","Inserte numeros mayores a 0")
			return

		if n <= 0 or m <= 0:
			messagebox.showerror("Error!","Inserte numeros mayores a 0")
			self.pedirDatos()
			return

		self.lista[n][m].configure(background="black")
		
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
		
		Button(ventanaDatos,text="Crear",command=lambda:self.descubrirCelda(d1,d2,ventanaDatos)).grid(row=0,column=2)

	def descubrirCelda(self,n,m,ventanaDatos):
		ventanaDatos.destroy()
		try:
			n = int(n.get())
			m = int(m.get())
		except ValueError:
			messagebox.showerror("Error!","Inserte numeros mayores a 0")
			return

		if n <= 0 or m <= 0:
			messagebox.showerror("Error!","Inserte numeros mayores a 0")
			self.pedirDatos()
			return

		if Mapa.mapa[n][m] == 0:
			self.lista[n][m].configure(background="blue", borderwidth=2, relief="solid")
		elif Mapa.mapa[n][m] == 1:
			self.lista[n][m].configure(background="red", borderwidth=2, relief="solid")
		if Mapa.mapa[n][m] == 2:
			self.lista[n][m].configure(background="green", borderwidth=2, relief="solid")
		if Mapa.mapa[n][m] == 3:
			self.lista[n][m].configure(background="pink", borderwidth=2, relief="solid")
		if Mapa.mapa[n][m] == 4:
			self.lista[n][m].configure(background="orange", borderwidth=2, relief="solid")

app = App()