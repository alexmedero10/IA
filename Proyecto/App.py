from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from queue import PriorityQueue
from io import open
from Celda import *
from Mapa import *
from Agente import *

arbol = [[2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 4, 4, 4, 4, 4],
			 [2, 0, 0, 0, 2, 2, 0, 0, 2, 2, 4, 4, 4, 4, 4],
			 [2, 0, 3, 0, 3, 2, 0, 0, 2, 2, 4, 4, 4, 4, 4],
			 [2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4],
			 [2, 2, 3, 3, 2, 2, 1, 2, 2, 2, 4, 4, 4, 4, 4],
			 [2, 4, 4, 4, 4, 2, 1, 0, 0, 2, 4, 4, 4, 0, 0],
			 [2, 4, 4, 4, 4, 2, 2, 1, 2, 0, 2, 2, 2, 2, 2],
			 [2, 1, 1, 1, 1, 1, 1, 1, 2, 0, 1, 1, 2, 2, 2],
			 [2, 1, 1, 1, 1, 1, 1, 1, 2, 0, 1, 1, 2, 2, 2],
			 [2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2],
			 [2, 2, 2, 1, 2, 2, 2, 2, 2, 0, 0, 0, 1, 1, 1],
			 [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 0, 2, 2],
			 [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1],
			 [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1],
			 [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1]]

class TreeNode:
	def __init__(self,data,costo, distancia, h):
		self.data = data
		self.costo = costo
		self.distancia = distancia
		self.h = h
		self.children = []
		self.parent = None


	def add_child(self,child):
		child.parent = self
		self.children.append(child)

	def get_level(self):
		level = 0
		p = self.parent
		while p:
			level += 1
			p = p.parent

		return level

	def print_tree(self):
		spaces = ' ' * self.get_level() * 3
		prefix = spaces + "|__" if self.parent else ""
		print(prefix + str(self.data), self.costo)
		if self.children:
			for child in self.children:
				child.print_tree()


class App:

	def __init__(self):
		self.mapa = Mapa()
		self.humano = Humano()
		self.mono = Mono()
		self.pulpo = Pulpo()
		self.puntoLlaveX = 11
		self.puntoLlaveY = 0
		self.puntoTemploX = 7
		self.puntoTemploY = 10
		self.puntoPiedrasX = 4
		self.puntoPiedrasY = 7
		self.puntoPortalX = 10
		self.puntoPortalY = 6
		"""
		self.puntoLlaveX = 14
		self.puntoLlaveY = 13
		self.puntoTemploX = 6
		self.puntoTemploY = 7
		self.puntoPiedrasX = 2
		self.puntoPiedrasY = 14
		self.puntoPortalX = 10
		self.puntoPortalY = 6
		"""
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
				linea = Celda(Label(self.root,text=""),self.mapa.laberinto[i][j],{"V":0,"A":0,"C":0,"H":0,"M":0,"O":0,"K":0,"T":0,"S":0,"P":0},i,j)
				linea.setColor()
				linea.label.grid(row=i,column=j,sticky=S+N+E+W)
				self.mapa.laberinto[i][j] = linea

		self.pedirPuntos()

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

	def pedirPuntos(self):
		#Para usar los establecidos por el programa y solo pedir agentes
		objetos = ['H','M','O']
		noPedidos = ['K','T','S','P']
		puntos = [[self.puntoLlaveX,self.puntoLlaveY],[self.puntoTemploX,self.puntoTemploY],[self.puntoPiedrasX,self.puntoPiedrasY],[self.puntoPortalX,self.puntoPortalY]]
		#Preguntar por todos los puntos
		#objetos = ['K','T','S','P','H','M','O']
		for i in range(len(objetos)):
			self.ponerInicio(objetos[i])

		for i in range(len(noPedidos)):
			self.mapa.laberinto[puntos[i][0]][puntos[i][1]].establecerPuntoNoPedidos(noPedidos[i])
	
	def ponerInicio(self,letra):
		self.root.deiconify()
		ventanaDatos = Toplevel()
		if letra == 'K':
			ventanaDatos.title("Llave")
		elif letra == 'T':
			ventanaDatos.title("Templo")
		elif letra == 'S':
			ventanaDatos.title("Piedras magicas")
		elif letra == 'P':
			ventanaDatos.title("Portal")
		elif letra == 'H':
			ventanaDatos.title("Humano")
		elif letra == 'M':
			ventanaDatos.title("Mono")
		elif letra == 'O':
			ventanaDatos.title("Pulpo")

		ventanaDatos.resizable(1,1)
		ventanaDatos.geometry('380x300')
		ventanaDatos.configure(background="dark turquoise")

		d1 = StringVar()
		Entry(ventanaDatos,justify="center",textvariable=d1).grid(row=0,column=0)

		d2 = StringVar()
		Entry(ventanaDatos,justify="center",textvariable=d2).grid(row=0,column=1)

		Button(ventanaDatos,text="Establecer",command=lambda:establecerPuntos(int(d1.get()),int(d2.get()),letra)).grid(row=0,column=2)

		def establecerPuntos(d1,d2,letra):
				self.mapa.laberinto[d1][d2].establecerPunto(ventanaDatos,letra)
				if letra == 'K':
					self.puntoLlaveX = d1
					self.puntoLlaveY = d2
				elif letra == 'T':
					self.puntoTemploX = d1
					self.puntoTemploY = d2
				elif letra == 'S':
					self.puntoPiedrasX = d1
					self.puntoPiedrasY = d2
				elif letra == 'P':
					self.puntoPortalX = d1
					self.puntoPortalY = d2
				elif letra == 'H':
					self.humano.setPosicion(d1,d2)
					#Checa que pueda iniciar en esa celda si no los pide otra vez
					if self.humano.dificultad[self.mapa.laberinto[d1][d2].terreno] == 0:
						messagebox.showinfo("Error","Agente no puede iniciar en esa posicion")
						self.ponerInicio(letra)
				elif letra == 'M':
					self.mono.setPosicion(d1,d2)
					if self.mono.dificultad[self.mapa.laberinto[d1][d2].terreno] == 0:
						messagebox.showinfo("Error","Agente no puede iniciar en esa posicion")
						self.ponerInicio(letra)
				elif letra == 'O':
					self.pulpo.setPosicion(d1,d2)
					if self.pulpo.dificultad[self.mapa.laberinto[d1][d2].terreno] == 0:
						messagebox.showinfo("Error","Agente no puede iniciar en esa posicion")
						self.ponerInicio(letra)
					else:
						self.iniciarAlgoritmo()
		
	def iniciarAlgoritmo(self):
		agentes = [self.humano,self.mono,self.pulpo]
		objetivos = [[self.puntoLlaveX,self.puntoLlaveY],[self.puntoTemploX,self.puntoTemploY],[self.puntoPiedrasX,self.puntoPiedrasY]]
		padres = []

		for i in range(len(agentes)):
			posInicial = agentes[i].posicionX
			posFinal = agentes[i].posicionY
			costoCelda = 0
			distanciaCelda = 0
			distanciaCelda2 = 0
			h = 0
			hObjetivo = 0
			hPortal = 0

			for j in range(len(objetivos)):
				costoAnterior = -1
				costoAlPortal = -1
				optimoObjetivo = []
				optimoPortal = []
				#Checamos que el agente pueda llegar a la celda objetivo
				if agentes[i].dificultad[self.mapa.laberinto[objetivos[j][0]][objetivos[j][1]].terreno] != 0:
					agentes[i].setPosicion(posInicial,posFinal)
					distanciaCelda = abs(abs(posInicial-objetivos[j][0])+abs(posFinal-objetivos[j][1]))
					h = distanciaCelda
					optimoObjetivo, costoAnterior, hObjetivo = self.algoritmo(agentes[i],objetivos[j][0],objetivos[j][1],costoCelda,distanciaCelda,h)
					#print(optimoObjetivo,costoAnterior)
				#Si no puede llegar al objetivo no podria llegar al portal desde ese objetivo
				if costoAnterior != -1:
					#Checamos que el agente pueda llegar a la celda del portal
					if agentes[i].dificultad[self.mapa.laberinto[self.puntoPortalX][self.puntoPortalY].terreno] != 0:
						agentes[i].setPosicion(objetivos[j][0],objetivos[j][1])
						distanciaCelda2 = abs(abs(objetivos[j][0]-self.puntoPortalX)+abs(objetivos[j][1]-self.puntoPortalY))
						h = distanciaCelda2
						optimoPortal, costoAlPortal,hPortal = self.algoritmo(agentes[i],self.puntoPortalX,self.puntoPortalY,costoCelda,distanciaCelda2,h)
						#print(optimoPortal,costoAlPortal)
				#Se le inserta el costo al objetivo y al portal
				agentes[i].setCostos([costoAnterior,costoAlPortal])
				agentes[i].setH([hObjetivo,hPortal])
				agentes[i].setOptimo([optimoObjetivo,optimoPortal])
				
			self.imprimirCostos(agentes[i])
		self.asignarMision()

	def algoritmo(self,agente,posX,posY,costoCelda,distanciaCelda,h):
		padre = TreeNode([agente.posicionX,agente.posicionY],costoCelda,distanciaCelda, h)
		arbol[agente.posicionX][agente.posicionY] = padre
		abiertos = PriorityQueue()
		abiertos.put([costoCelda,padre.data])
		consulta = [padre.data]

		dirX = [0,0,-1,1]
		dirY = [1,-1,0,0]

		while not abiertos.empty():
			nodo = abiertos.get()
			costoNodo = nodo[0]
			nodoPosicion = nodo[1]
			nodoActual = arbol[nodoPosicion[0]][nodoPosicion[1]]

			for i in range(4):
				x = nodoPosicion[0]+dirX[i]
				y = nodoPosicion[1]+dirY[i]
				if(x >= 0 and x < len(self.mapa.laberinto) and y >= 0 and y < len(self.mapa.laberinto[0])):
					#Verificar que el nodo no lo hayamos metido a abiertos o cerrados
					if [x,y] not in consulta:
						#Verificar que el agente se pueda mover a esa casilla
						if agente.dificultad[self.mapa.laberinto[x][y].terreno] != 0:
							distancia = abs(abs(x-posX)+abs(y-posY))
							costo = agente.dificultad[self.mapa.laberinto[x][y].terreno]+costoNodo
							nuevoNodo = TreeNode([x,y],costo,distancia,costo+distancia)
							arbol[x][y] = nuevoNodo
							nodoActual.add_child(nuevoNodo)
							abiertos.put([nuevoNodo.costo,nuevoNodo.data])
							consulta.append(nuevoNodo.data)
							if nuevoNodo.data == [posX,posY]:
								optimo = []
								costo = nuevoNodo.costo
								h = nuevoNodo.h
								while nuevoNodo.parent != None:
									optimo.append([nuevoNodo.data,nuevoNodo.distancia])
									nuevoNodo = nuevoNodo.parent
								optimo.append([nuevoNodo.data,nuevoNodo.distancia])
								return optimo,costo,h
		return [],-1,-1

	def asignarMision(self):
		#Donde se van a agregar la tarea de cada agente
		#0 es de la llave, 1 del templo y 2 de las piedras
		totalMisiones = []
		#Tiene el costo, y las tareas de cada agente para obtener el costo
		misiones = {}
		total = 0
		#Probamos todas las combinaciones para sacar el costo total minimo
		for i in range(len(self.humano.costos)):
			if self.humano.costos[i][1] == -1:
				continue
			total = self.humano.costos[i][1]+self.humano.costos[i][0]
			totalMisiones.append(i)
			for j in range(len(self.mono.costos)):
				if self.mono.costos[j][1] == -1:
					continue
				total += self.mono.costos[j][1]+self.humano.costos[i][0]
				totalMisiones.append(j)
				for k in range(len(self.pulpo.costos)):
					if self.pulpo.costos[k][1] == -1:
						continue
					if i==j or i==k or j==k:
						continue
					#Costo total
					total += self.pulpo.costos[k][1]+self.humano.costos[i][0]
					totalMisiones.append(k)
					#Se guarda una copia, si no se pone [:] la lista se sigue modificando
					misiones[total] = totalMisiones[:]
					totalMisiones.pop()
					total -= self.pulpo.costos[k][1]
				totalMisiones.pop()
				total -= self.mono.costos[j][1]
			totalMisiones.pop()
			total -= self.humano.costos[i][1]

		#Se ordenan para sacar la menor
		misionesOrdenadas = sorted(misiones)
		if len(misionesOrdenadas) == 0:
			print("No hay solucion")
		else:
			print("Costo total: ",misionesOrdenadas[0])
			misionesFinales = misiones[misionesOrdenadas[0]]
			agentes = [self.humano,self.mono,self.pulpo]
			objetivos = ["Llave","Templo","Piedras"]
			colores = ["purple","red","brown"]
			for i in range(len(misionesFinales)):
				print(type(agentes[i]).__name__)
				print(objetivos[misionesFinales[i]])
				print("Costo a {}: {} {}".format(objetivos[misionesFinales[i]],agentes[i].costos[misionesFinales[i]][0],agentes[i].h[misionesFinales[i]][0]))
				print("Recorrido a {}: {}".format(objetivos[misionesFinales[i]],agentes[i].optimo[misionesFinales[i]][0]))
				self.pintar(agentes[i].optimo[misionesFinales[i]][0],colores[i])
				print("Costo a portal: {} {}".format(agentes[i].costos[misionesFinales[i]][1]+agentes[i].costos[misionesFinales[i]][0],agentes[i].h[misionesFinales[i]][1]+agentes[i].h[misionesFinales[i]][0]))
				print("Recorrido a Portal desde {}: {}".format(objetivos[misionesFinales[i]],agentes[i].optimo[misionesFinales[i]][1]))
				self.pintar(agentes[i].optimo[misionesFinales[i]][1],colores[i])
			print("")
		self.acabarApp()

	def pintar(self,camino,color):
		for celda in camino:
			self.mapa.laberinto[celda[0][0]][celda[0][1]].caminoOptimo(color)

	def imprimirCostos(selfa,agente):
		nombres = ["Llave","Templo","Piedras"]
		for i in range(3):
			print("Costo {} a {}: {}".format(type(agente).__name__,nombres[i],agente.costos[i][0]))
			print("Costo {} a {} y portal: {}".format(type(agente).__name__,nombres[i],agente.costos[i][1]+agente.costos[i][0]))
		print("")

	def acabarApp(self):
		messagebox.showinfo("Terminó el programa","Fin")
		r = messagebox.askquestion("Reiniciar","Reiniciar?")
		if r == "yes":
			self.pedirPuntos()


app = App()