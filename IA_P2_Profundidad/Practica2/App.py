from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from io import open
from Celda import *
from Mapa import *
from Agente import *
import time
from collections import defaultdict


class App:
    mapa = Mapa()
    agente = Agente()
    puntoX = 0
    puntoY = 0

    def __init__(self):
        self.root = Tk()
        self.root.title("Laberinto")
        self.root.geometry('500x500')
        self.root.resizable(1, 1)

        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(
            label="Crear tablero", command=self.pedirArchivo)
        self.filemenu.add_separator()
        self.filemenu.add_command(
            label="Bloquear mapa", command=self.mapa.bloquearMapa)
        self.filemenu.add_separator()
        self.filemenu.add_command(
            label="Bloquear celda", command=lambda: self.pedirCelda(1))
        self.filemenu.add_separator()
        self.filemenu.add_command(
            label="Descubir celda", command=lambda: self.pedirCelda(2))
        self.filemenu.add_separator()
        self.filemenu.add_command(
            label="Mostrar valor", command=lambda: self.pedirCelda(3))
        self.filemenu.add_separator()
        self.filemenu.add_command(
            label="Cambiar valor", command=lambda: self.pedirCelda(4))

        self.menubar.add_cascade(label="ACTIONS", menu=self.filemenu)

        self.filemenu2 = Menu(self.menubar, tearoff=0)
        self.filemenu2.add_command(
            label="Escoger agente", command=self.escogerAgente)
        self.filemenu2.add_separator()
        self.filemenu2.add_command(
            label="Profundidad", command=lambda: self.algoritmo(1))
        self.filemenu2.add_separator()
        self.filemenu2.add_command(
            label="Anchura", command=lambda: self.algoritmo(2))
        self.filemenu2.add_separator()
        self.filemenu2.add_command(
            label="A*", command=lambda: self.algoritmo(3))

        # self.filemenu2.add_separator()
        # self.filemenu2.add_command(label="Establece inicio",command=lambda:self.ponerInicio)

        self.menubar.add_cascade(label="INICIAR", menu=self.filemenu2)

        # self.root.bind("<Right>", self.right)
        # self.root.bind("<Left>", self.left)
        # self.root.bind("<Up>", self.up)
        # self.root.bind("<Down>", self.down)
        # self.root.bind("<z>", self.tleft)
        # self.root.bind("<x>", self.tright)

        self.root.mainloop()

    def abrirArchivo(self, file):
        fichero = open(file, "r")
        # CREA LA LISTA DEL MAPA
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
                linea = Celda(Label(self.root, text=""), self.mapa.laberinto[i][j], {
                              "V": 0, "O": 0, "I": 0, "X": 0, "F": 0})
                linea.setColor()
                linea.label.grid(row=i, column=j, sticky=S+N+E+W)
                self.mapa.laberinto[i][j] = linea
        # self.mapa.bloquearMapa()

    def pedirArchivo(self):
        file_path = filedialog.askopenfilename()
        self.abrirArchivo(file_path)

    def pedirCelda(self, opcion):
        self.root.deiconify()
        ventanaDatos = Toplevel()
        ventanaDatos.title("Laberinto")
        ventanaDatos.resizable(1, 1)
        ventanaDatos.geometry('380x300')
        ventanaDatos.configure(background="dark turquoise")

        d1 = StringVar()
        Entry(ventanaDatos, justify="center",
              textvariable=d1).grid(row=0, column=0)

        d2 = StringVar()
        Entry(ventanaDatos, justify="center",
              textvariable=d2).grid(row=0, column=1)

        if opcion == 1:
            Button(ventanaDatos, text="Crear", command=lambda: self.mapa.laberinto[int(
                d1.get())][int(d2.get())].bloquearCelda(ventanaDatos)).grid(row=0, column=2)
        elif opcion == 2:
            Button(ventanaDatos, text="Crear", command=lambda: self.mapa.laberinto[int(
                d1.get())][int(d2.get())].descubrirCelda(ventanaDatos)).grid(row=0, column=2)
        elif opcion == 3:
            Button(ventanaDatos, text="Crear", command=lambda: self.mapa.laberinto[int(
                d1.get())][int(d2.get())].mostrarValor(ventanaDatos)).grid(row=0, column=2)
        elif opcion == 4:
            d3 = StringVar()
            Entry(ventanaDatos, justify="center",
                  textvariable=d3).grid(row=1, column=0)
            Button(ventanaDatos, text="Crear", command=lambda: self.mapa.laberinto[int(d1.get())][int(
                d2.get())].cambiarValor(int(d3.get()), ventanaDatos)).grid(row=0, column=2)
        elif opcion == 5:
            def establecerPuntos(d1, d2, d3, d4):
                self.mapa.laberinto[d1][d2].establecerInicio(ventanaDatos)
                self.mapa.laberinto[d3][d4].establecerFin(ventanaDatos)
                self.puntoX = d1
                self.puntoY = d2

            d3 = StringVar()
            Entry(ventanaDatos, justify="center",
                  textvariable=d3).grid(row=1, column=0)

            d4 = StringVar()
            Entry(ventanaDatos, justify="center",
                  textvariable=d4).grid(row=1, column=1)
            Button(ventanaDatos, text="Establecer", command=lambda: establecerPuntos(
                int(d1.get()), int(d2.get()), int(d3.get()), int(d4.get()))).grid(row=0, column=2)

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
        ventanaDatos.resizable(1, 1)
        ventanaDatos.geometry('380x300')
        ventanaDatos.configure(background="dark turquoise")
        opcion = IntVar()

        def seleccionar():
            if opcion.get() == 1:
                self.agente = Humano()
            elif opcion.get() == 2:
                self.agente = Mono()
            elif opcion.get() == 3:
                self.agente = Pulpo()
            elif opcion.get() == 4:
                self.agente = PieGrande()
            self.escogerTipo()
            ventanaDatos.destroy()

        Radiobutton(ventanaDatos, text="Humano", variable=opcion,
                    value=1, command=seleccionar).grid(row=0, column=0)
        Radiobutton(ventanaDatos, text="Mono", variable=opcion,
                    value=2, command=seleccionar).grid(row=1, column=0)
        Radiobutton(ventanaDatos, text="Pulpo", variable=opcion,
                    value=3, command=seleccionar).grid(row=2, column=0)
        Radiobutton(ventanaDatos, text="Pie grande", variable=opcion,
                    value=4, command=seleccionar).grid(row=3, column=0)

    def escogerTipo(self):
        self.root.deiconify()
        ventanaDatos = Toplevel()
        ventanaDatos.title("Escoge tipo")
        ventanaDatos.resizable(1, 1)
        ventanaDatos.geometry('380x300')
        ventanaDatos.configure(background="dark turquoise")
        opcion2 = IntVar()

        def seleccionar():
            if opcion2.get() == 1:
                self.agente.setVueltas({"L": 1, "R": 0})
            elif opcion2.get() == 2:
                self.agente.setVueltas({"L": 1, "R": 1})
            elif opcion2.get() == 3:
                self.agente.setVueltas({"L": 0, "R": 0})
                self.agente.setMovimientos({"F": 1, "B": 1, "L": 1, "R": 1})
            self.escogerSensores()
            ventanaDatos.destroy()

        Radiobutton(ventanaDatos, text="Agente 1", variable=opcion2,
                    value=1, command=seleccionar).grid(row=0, column=0)
        Radiobutton(ventanaDatos, text="Agente 2", variable=opcion2,
                    value=2, command=seleccionar).grid(row=1, column=0)
        Radiobutton(ventanaDatos, text="Agente 3", variable=opcion2,
                    value=3, command=seleccionar).grid(row=2, column=0)

    def escogerSensores(self):
        self.root.deiconify()
        ventanaDatos = Toplevel()
        ventanaDatos.title("Escoge sensores")
        ventanaDatos.resizable(1, 1)
        ventanaDatos.geometry('380x300')
        ventanaDatos.configure(background="dark turquoise")
        opcion3 = IntVar()

        def seleccionar():
            if opcion3.get() == 1:
                self.root.deiconify()
                ventanaDatos2 = Toplevel()
                ventanaDatos2.title("Escoge sensores")
                ventanaDatos2.resizable(1, 1)
                ventanaDatos2.geometry('380x300')
                ventanaDatos2.configure(background="dark turquoise")
                opcion4 = IntVar()

                def seleccionar2():
                    if opcion4.get() == 1:
                        self.agente.setSensores(
                            {"L": 0, "R": 1, "U": 0, "D": 0})
                        self.agente.setMovimientos(
                            {"F": 0, "B": 0, "L": 0, "R": 1})
                        self.ponerInicio()
                    elif opcion4.get() == 2:
                        self.agente.setSensores(
                            {"L": 0, "R": 0, "U": 1, "D": 0})
                        self.agente.setMovimientos(
                            {"F": 1, "B": 0, "L": 0, "R": 0})
                        self.ponerInicio()
                    elif opcion4.get() == 3:
                        self.agente.setSensores(
                            {"L": 1, "R": 0, "U": 0, "D": 0})
                        self.agente.setMovimientos(
                            {"F": 0, "B": 0, "L": 1, "R": 0})
                        self.ponerInicio()
                    elif opcion4.get() == 4:
                        self.agente.setSensores(
                            {"L": 0, "R": 0, "U": 0, "D": 1})
                        self.agente.setMovimientos(
                            {"F": 0, "B": 1, "L": 0, "R": 0})
                        self.ponerInicio()
                    ventanaDatos2.destroy()
                Radiobutton(ventanaDatos2, text="Derecha", variable=opcion4,
                            value=1, command=seleccionar2).grid(row=0, column=0)
                Radiobutton(ventanaDatos2, text="Arriba", variable=opcion4,
                            value=2, command=seleccionar2).grid(row=1, column=0)
                Radiobutton(ventanaDatos2, text="Izquierda", variable=opcion4,
                            value=3, command=seleccionar2).grid(row=2, column=0)
                Radiobutton(ventanaDatos2, text="Abajo", variable=opcion4,
                            value=4, command=seleccionar2).grid(row=3, column=0)
            elif opcion3.get() == 2:
                self.agente.setSensores({"L": 1, "R": 1, "U": 1, "D": 1})
                self.ponerInicio()

            ventanaDatos.destroy()

        Radiobutton(ventanaDatos, text="Un sensor", variable=opcion3,
                    value=1, command=seleccionar).grid(row=0, column=0)
        Radiobutton(ventanaDatos, text="Cuatro sensores", variable=opcion3,
                    value=2, command=seleccionar).grid(row=1, column=0)

    def ponerInicio(self, opcion):
        self.root.deiconify()
        ventanaDatos = Toplevel()
        ventanaDatos.title("Laberinto")
        ventanaDatos.resizable(1, 1)
        ventanaDatos.geometry('380x300')
        ventanaDatos.configure(background="dark turquoise")

        d1 = StringVar()
        Entry(ventanaDatos, justify="center",
              textvariable=d1).grid(row=0, column=0)

        d2 = StringVar()
        Entry(ventanaDatos, justify="center",
              textvariable=d2).grid(row=0, column=1)

        d3 = StringVar()
        Entry(ventanaDatos, justify="center",
              textvariable=d3).grid(row=1, column=0)

        d4 = StringVar()
        Entry(ventanaDatos, justify="center",
              textvariable=d4).grid(row=1, column=1)
        Button(ventanaDatos, text="Establecer", command=lambda: establecerPuntos(
            int(d1.get()), int(d2.get()), int(d3.get()), int(d4.get()))).grid(row=0, column=2)

        def establecerPuntos(d1, d2, d3, d4):
            self.mapa.laberinto[d1][d2].establecerInicio(ventanaDatos)
            self.mapa.laberinto[d3][d4].establecerFin(ventanaDatos)
            puntoX = d1
            puntoY = d2
            self.agente.setPosicion(d1, d2)
            self.agente.usarSensores(self.mapa)
            if self.mapa.laberinto[d1][d2].checarFinal():
                self.acabarApp()
            if opcion == 1:
                self.profundidad()
            elif opcion == 2:
                self.anchura()
            elif opcion == 3:
                self.a_estrella()

    def right(self):
        self.agente.mover(self.mapa, "R")
        if self.mapa.laberinto[self.agente.posicionX][self.agente.posicionY].checarFinal():
            self.acabarApp()
        else:
            self.agente.usarSensores(self.mapa)

    def left(self):
        self.agente.mover(self.mapa, "L")
        if self.mapa.laberinto[self.agente.posicionX][self.agente.posicionY].checarFinal():
            self.acabarApp()
        else:
            self.agente.usarSensores(self.mapa)

    def up(self):
        self.agente.mover(self.mapa, "F")
        if self.mapa.laberinto[self.agente.posicionX][self.agente.posicionY].checarFinal():
            self.acabarApp()
        else:
            self.agente.usarSensores(self.mapa)

    def down(self):
        self.agente.mover(self.mapa, "B")
        if self.mapa.laberinto[self.agente.posicionX][self.agente.posicionY].checarFinal():
            self.acabarApp()
        else:
            self.agente.usarSensores(self.mapa)

    def tleft(self, event):
        self.agente.voltearIzquierda(self.mapa)

    def tright(self, event):
        self.agente.voltearDerecha(self.mapa)

    def acabarApp(self):
        messagebox.showinfo("LLegó a la meta", "Costo: {}\nPasos: {}".format(
            self.agente.puntaje, self.agente.pasos))
        r = messagebox.askquestion("Reiniciar", "Reiniciar?")
        if r == "yes":
            self.escogerAgente()

    def algoritmo(self, opcion):
        self.agente = AgenteP2()
        self.agente.setVueltas({"L": 0, "R": 0})
        self.agente.setSensores({"L": 1, "R": 1, "U": 1, "D": 1})
        self.agente.setMovimientos({"F": 1, "B": 1, "L": 1, "R": 1})
        self.ponerInicio(opcion)

    def profundidad(self):
        pila = []
    	#Metemos la posicion la posicion inicial
        pila.append([self.agente.posicionX,self.agente.posicionY])

        #Prioridad (Abajo,Arriba,Derecha,Izquierda)
        #Como es una pila la prioridad va a quedar volteada
        #Prioridad (Izquierda,Derecha,Arriba,Abajo)
        dirX = [1,-1,0,0]
        dirY = [0,0,1,-1]

        while len(pila) > 0:
            posx,posy = pila.pop()
            print([posx,posy])
            self.agente.setPosicion(posx,posy)
            #Se marca la celda como visitada
            self.mapa.laberinto[posx][posy].setMarcas({"V":1})
            #Comprueba que no sea el final
            if(self.mapa.laberinto[posx][posy].marcas["F"] == "F"):
                self.acabarApp()
                return

            for i in range(4):
                x = posx+dirX[i]
                y = posy+dirY[i]
                #Checa si la celda a la que se quiere mover esta dentro de los limtes
                if(x>=0 and x<len(self.mapa.laberinto) and y>=0 and y<len(self.mapa.laberinto[0])):
                	#Checa si la celda no esta visitada y si no es pared
                    if(self.mapa.laberinto[x][y].marcas["V"] != "V" and self.mapa.laberinto[x][y].terreno != 0):
                        pila.append([x,y])


    def anchura(self):
        cola = []
        #Metemos la posicion inicial
        cola.append([self.agente.posicionX,self.agente.posicionY])

        #Prioridad (Abajo,Arriba,Derecha,izquierda)
        dirX = [1,-1,0,0]
        dirY = [0,0,1,-1]

        while len(cola) > 0:
            posx,posy = cola.pop(0)
            print([posx,posy])
            self.agente.setPosicion(posx,posy)
            self.mapa.laberinto[posx][posy].setMarcas({"V":1})
            if(self.mapa.laberinto[posx][posy].marcas["F"] == "F"):
                self.acabarApp()
                return
            for i in range(4):
                x = posx+dirX[i]
                y = posy+dirY[i]
                #Checa si la celda a la que se quiere mover esta dentro de los limtes
                if(x>=0 and x<len(self.mapa.laberinto) and y>=0 and y<len(self.mapa.laberinto[0])):
                	#Checa si la celda no esta visitada y si no es pared
                    if(self.mapa.laberinto[x][y].marcas["V"] != "V" and self.mapa.laberinto[x][y].terreno != 0):
                        cola.append([x,y])

    def a_estrella(self):
        self.pedirCelda(5)


app = App()