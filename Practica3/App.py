from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from queue import PriorityQueue
from io import open
from Celda import *
from Mapa import *
from Agente import *

class App:

	def __init__(self):
		self.mapa = Mapa()
		self.agente = Agente()
		self.puntoX = 0
		self.puntoY = 0
		self.puntoFX = 0
		self.puntoFY = 0
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
		self.filemenu.add_command(label="Descubir mapa",command=self.mapa.descubrirMapa)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Bloquear celda",command=lambda:self.pedirCelda(1))
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Descubir celda",command=lambda:self.pedirCelda(2))
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Mostrar valor",command=lambda:self.pedirCelda(3))
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Cambiar valor",command=lambda:self.pedirCelda(4))

		self.menubar.add_cascade(label="ACTIONS",menu=self.filemenu)


		self.filemenu2 = Menu(self.menubar,tearoff=0)
		self.filemenu2.add_command(label="Escoger agente",command=self.escogerAgente)
		#self.filemenu2.add_separator()
		#self.filemenu2.add_command(label="Establece inicio",command=lambda:self.ponerInicio)

		self.menubar.add_cascade(label="INICIAR",menu=self.filemenu2)

		self.root.mainloop()

	def abrirArchivo(self, file):
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
		for i in range(len(self.mapa.laberinto)):
			self.root.rowconfigure(i, weight=1)

		for j in range(len(self.mapa.laberinto[0])):
			self.root.columnconfigure(j, weight=1)

		for i in range(len(self.mapa.laberinto)):
			for j in range(len(self.mapa.laberinto[i])):
				linea = Celda(Label(self.root,text=""),self.mapa.laberinto[i][j],{"V":0,"O":0,"C":0,"I":0,"X":0,"F":0},i,j)
				linea.setColor()
				linea.label.grid(row=i,column=j,sticky=S+N+E+W)
				self.mapa.laberinto[i][j] = linea

	def pedirArchivo(self):
		file_path = filedialog.askopenfilename()
		self.abrirArchivo(file_path)

	def pedirCelda(self, opcion):
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
		
		if opcion == 1:
			Button(ventanaDatos,text="Crear",command=lambda:self.mapa.laberinto[int(d1.get())][int(d2.get())].bloquearCelda(ventanaDatos)).grid(row=0,column=2)
		elif opcion == 2:
			Button(ventanaDatos,text="Crear",command=lambda:self.mapa.laberinto[int(d1.get())][int(d2.get())].descubrirCelda(ventanaDatos)).grid(row=0,column=2)
		elif opcion == 3:
			Button(ventanaDatos,text="Crear",command=lambda:self.mapa.laberinto[int(d1.get())][int(d2.get())].mostrarValor(ventanaDatos)).grid(row=0,column=2)
		elif opcion == 4:
			d3 = StringVar()
			Entry(ventanaDatos,justify="center",textvariable=d3).grid(row=1,column=0)
			Button(ventanaDatos,text="Crear",command=lambda:self.mapa.laberinto[int(d1.get())][int(d2.get())].cambiarValor(int(d3.get()),ventanaDatos)).grid(row=0,column=2)


	def escogerAgente(self):
		if self.mapa.laberinto == []:
			self.pedirArchivo()
		if type(self.agente).__name__ != "Agente":
			agente = Agente()
			self.mapa.borrarMarcas()
			self.mapa.bloquearMapa()

		self.root.deiconify()
		ventanaDatos = Toplevel()
		ventanaDatos.title("Escoge agente")
		ventanaDatos.resizable(1,1)
		ventanaDatos.geometry('380x300')
		ventanaDatos.configure(background="dark turquoise")
		opcion = IntVar()
		def seleccionar():
			if opcion.get() == 2:
				self.agente = Mono()
			elif opcion.get() == 3:
				self.agente = Pulpo()
			self.ponerInicio()
			ventanaDatos.destroy() 

		Radiobutton(ventanaDatos,text="Mono",variable=opcion,value=2,command=seleccionar).grid(row=1,column=0)
		Radiobutton(ventanaDatos,text="Pulpo",variable=opcion,value=3,command=seleccionar).grid(row=2,column=0)

	def ponerInicio(self):
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

		d3 = StringVar()
		Entry(ventanaDatos,justify="center",textvariable=d3).grid(row=1,column=0)

		d4 = StringVar()
		Entry(ventanaDatos,justify="center",textvariable=d4).grid(row=1,column=1)
		Button(ventanaDatos,text="Establecer",command=lambda:establecerPuntos(int(d1.get()),int(d2.get()),int(d3.get()),int(d4.get()))).grid(row=0,column=2)

		def establecerPuntos(d1,d2,d3,d4):
				self.mapa.laberinto[d1][d2].establecerInicio(ventanaDatos)
				self.mapa.laberinto[d3][d4].establecerFin(ventanaDatos)
				self.puntoX = d1
				self.puntoY = d2
				self.puntoFX = d3
				self.puntoFY = d4
				if self.agente.dificultad[self.mapa.laberinto[d1][d2].terreno] == 0:
					messagebox.showinfo("Error","Agente no puede iniciar en esa posicion")
					self.acabarApp()
					return
				if self.mapa.laberinto[d1][d2].checarFinal():
					self.acabarApp()
					return

				self.mapa.bloquearMapa()
				self.agente.setPosicion(d1,d2)
				self.agente.usarSensores(self.mapa)
				self.algoritmo(self.puntoFX,self.puntoFY)


	def algoritmo(self,posX,posY):
		abiertos = PriorityQueue()
		cerrados = []
		consulta = []
		puntoX = self.agente.posicionX
		puntoY = self.agente.posicionY
		costoCelda = 0

		dirX = [0,0,-1,1]
		dirY = [1,-1,0,0]
		
		#Se calculan los valores para el nodo inicial
		self.mapa.laberinto[puntoX][puntoY].calcular(self.agente,self.puntoFX,self.puntoFY,costoCelda,self.mapa)
		#Se mete a los nodos abiertos
		abiertos.put([self.mapa.laberinto[puntoX][puntoY].sumaDC,[self.mapa.laberinto[puntoX][puntoY].puntoX,self.mapa.laberinto[puntoX][puntoY].puntoY]])
		#Se mete a los nodos que ya ha estado en abiertos o cerrados
		consulta.append(self.mapa.laberinto[puntoX][puntoY])

		#Mientras haya nodos abiertos hacer el algoritmo
		while not abiertos.empty():
			#Se obtiene el nodo con valor h más pequeño y se saca de abiertos
			h,celdaActual = abiertos.get()
			#print(celdaActual)
			celdaActual = self.mapa.laberinto[celdaActual[0]][celdaActual[1]]
			#Se marca el nodo como cerrado y se mete a cerrados
			if celdaActual.marcas['I'] == 'I':
				celdaActual.setMarcas({"O":0,"C":2,"V":1})
			else:
				celdaActual.setMarcas({"O":0,"C":1,"V":1})
			cerrados.append(celdaActual)
			#El agente se mueve a ese nodo
			self.agente.mover(self.mapa,celdaActual.puntoX,celdaActual.puntoY)
			puntoX = self.agente.posicionX
			puntoY = self.agente.posicionY
			costoCelda = self.mapa.laberinto[puntoX][puntoY].costo

			for i in range(4):
				x = puntoX+dirX[i]
				y = puntoY+dirY[i]
				if(x >= 0 and x < len(self.mapa.laberinto) and y >= 0 and y < len(self.mapa.laberinto[0])):
					#Verificar que el nodo no lo hayamos metido a abiertos o cerrados
					if self.mapa.laberinto[x][y] not in consulta:
						#Verificar que el agente se pueda mover a esa casilla
						if self.agente.dificultad[self.mapa.laberinto[x][y].terreno] != 0:
							self.mapa.laberinto[x][y].calcular(self.agente,self.puntoFX,self.puntoFY,costoCelda,self.mapa)
							abiertos.put([self.mapa.laberinto[x][y].sumaDC,[self.mapa.laberinto[x][y].puntoX,self.mapa.laberinto[x][y].puntoY]])
							consulta.append(self.mapa.laberinto[x][y])

			#Si ya vimos al nodo destino, acabar el algortimo
			if self.mapa.laberinto[posX][posY] in consulta:
				#Se marca como visitado y se limpian los registros
				self.mapa.laberinto[posX][posY].calcular(self.agente,posX,posY,costoCelda,self.mapa)
				self.mapa.laberinto[posX][posY].setMarcas({"V":1,"O":1,"C":0})
				#Se saca el camino optimo desde el final
				camino = [[posX,posY]]
				print(camino)
				self.mapa.laberinto[camino[-1][0]][camino[-1][1]].setColorOptimo()
				camino = self.marcarCaminoOptimo(camino)
				print("CAMINO")
				camino.reverse()
				print(camino)
				while not abiertos.empty():
					try:
						abiertos.get(False)
					except Empty:
						continue
					abiertos.task_done()
				cerrados.clear()
				consulta.clear() 
				self.acabarApp()

	def marcarCaminoOptimo(self, camino):

		#Prioridad (Abajo,Arriba,Derecha,Izquierda)
		#Como es una pila la prioridad va a quedar volteada
		#Prioridad (Izquierda,Derecha,Arriba,Abajo)
		dirX = [1,-1,0,0]
		dirY = [0,0,1,-1]

		for i in range(4):
			costoAnterior = self.mapa.laberinto[camino[-1][0]][camino[-1][1]].sumaDC
			x = camino[-1][0]+dirX[i]
			y = camino[-1][1]+dirY[i]
			#Checa si la celda a la que se quiere mover esta dentro de los limtes
			if(x>=0 and x<len(self.mapa.laberinto) and y>=0 and y<len(self.mapa.laberinto[0])):
				#Checa si esta en la lista de cerrados y si su costo es menor a la celda anterior
				if(self.mapa.laberinto[x][y].marcas["C"] != 0 and self.mapa.laberinto[x][y].sumaDC <= costoAnterior):
					camino.append([x,y])
					self.mapa.laberinto[x][y].setColorOptimo()
					#Hasta que llegue al inicio se detiene
					if(self.mapa.laberinto[x][y].marcas["I"] == 0):
						#print(camino[-1])
						return self.marcarCaminoOptimo(camino)
					else:
						return camino

	def acabarApp(self):
		messagebox.showinfo("LLegó a la meta","Fin")
		r = messagebox.askquestion("Reiniciar","Reiniciar?")
		if r == "yes":
			self.escogerAgente()


app = App()