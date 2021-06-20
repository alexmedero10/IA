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
        self.HL = []
        self.HP = []
        self.HT = []
        self.ML = []
        self.MP = []
        self.MT = []
        self.PL = []
        self.PP = []
        self.PT = []
        self.cuenta = 0

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
            label="Descubir mapa", command=self.mapa.descubrirMapa)
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
                              "V": 0, "A": 0, "C": 0, "H": 0, "M": 0, "O": 0, "K": 0, "T": 0, "S": 0, "P": 0}, i, j)
                linea.setColor()
                linea.label.grid(row=i, column=j, sticky=S+N+E+W)
                self.mapa.laberinto[i][j] = linea

        self.pedirPuntos()

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

    def pedirPuntos(self):
        # Para usar los establecidos por el programa y solo pedir agentes
        objetos = ['H', 'M', 'O']
        # Preguntar por todos los puntos
        #objetos = ['K', 'T', 'S', 'P', 'H', 'M', 'O']
        for i in range(len(objetos)):
            self.ponerInicio(objetos[i])

    def ponerInicio(self, letra):
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

        ventanaDatos.resizable(1, 1)
        ventanaDatos.geometry('380x300')
        ventanaDatos.configure(background="dark turquoise")

        d1 = StringVar()
        Entry(ventanaDatos, justify="center",
              textvariable=d1).grid(row=0, column=0)

        d2 = StringVar()
        Entry(ventanaDatos, justify="center",
              textvariable=d2).grid(row=0, column=1)

        Button(ventanaDatos, text="Establecer", command=lambda: establecerPuntos(
            int(d1.get()), int(d2.get()), letra)).grid(row=0, column=2)

        def establecerPuntos(d1, d2, letra):
            self.mapa.laberinto[d1][d2].establecerPunto(ventanaDatos, letra)
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
                self.humano.setPosicion(d1, d2)
                # Checa que pueda iniciar en esa celda si no los pide otra vez
                if self.humano.dificultad[self.mapa.laberinto[d1][d2].terreno] == 0:
                    messagebox.showinfo(
                        "Error", "Agente no puede iniciar en esa posicion")
                    self.ponerInicio(letra)
            elif letra == 'M':
                self.mono.setPosicion(d1, d2)
                if self.mono.dificultad[self.mapa.laberinto[d1][d2].terreno] == 0:
                    messagebox.showinfo(
                        "Error", "Agente no puede iniciar en esa posicion")
                    self.ponerInicio(letra)
            elif letra == 'O':
                self.pulpo.setPosicion(d1, d2)
                if self.pulpo.dificultad[self.mapa.laberinto[d1][d2].terreno] == 0:
                    messagebox.showinfo(
                        "Error", "Agente no puede iniciar en esa posicion")
                    self.ponerInicio(letra)
                else:
                    self.iniciarAlgoritmo()

    def iniciarAlgoritmo(self):
        agentes = [self.humano, self.mono, self.pulpo]
        objetivos = [[self.puntoLlaveX, self.puntoLlaveY], [
            self.puntoTemploX, self.puntoTemploY], [self.puntoPiedrasX, self.puntoPiedrasY]]

        for i in range(len(agentes)):
            posInicial = agentes[i].posicionX
            posFinal = agentes[i].posicionY
            costoCelda = 0
            for j in range(len(objetivos)):
                costoAnterior = -1
                costoAlPortal = -1
                # Checamos que el agente pueda llegar a la celda objetivo
                if agentes[i].dificultad[self.mapa.laberinto[objetivos[j][0]][objetivos[j][1]].terreno] != 0:
                    agentes[i].setPosicion(posInicial, posFinal)
                    costoAnterior = self.algoritmo(
                        agentes[i], objetivos[j][0], objetivos[j][1], costoCelda)
                # Si no puede llegar al objetivo no podria llegar al portal desde ese objetivo
                if costoAnterior != -1:
                    # Checamos que el agente pueda llegar a la celda del portal
                    if agentes[i].dificultad[self.mapa.laberinto[self.puntoPortalX][self.puntoPortalY].terreno] != 0:
                        agentes[i].setPosicion(
                            objetivos[j][0], objetivos[j][1])
                        costoAlPortal = self.algoritmo(
                            agentes[i], self.puntoPortalX, self.puntoPortalY, costoAnterior)
                # Se le inserta el costo al objetivo y al portal
                agentes[i].setCostos([costoAnterior, costoAlPortal])

            self.imprimirCostos(agentes[i])
        self.asignarMision()

    def algoritmo(self, agente, posX, posY, costoCelda):
        abiertos = PriorityQueue()
        cerrados = []
        consulta = []
        puntoX = agente.posicionX
        puntoY = agente.posicionY

        dirX = [0, 0, -1, 1]
        dirY = [1, -1, 0, 0]

        # Se calculan los valores para el nodo inicial
        self.mapa.laberinto[puntoX][puntoY].calcular(
            agente, posX, posY, costoCelda)
        # Se mete a los nodos abiertos
        abiertos.put([self.mapa.laberinto[puntoX][puntoY].sumaDC, [
                     self.mapa.laberinto[puntoX][puntoY].puntoX, self.mapa.laberinto[puntoX][puntoY].puntoY]])
        # Se mete a los nodos que ya ha estado en abiertos o cerrados
        consulta.append(self.mapa.laberinto[puntoX][puntoY])

        # Mientras haya nodos abiertos hacer el algoritmo
        while not abiertos.empty():
            # Se obtiene el nodo con valor h más pequeño y se saca de abiertos
            h, celdaActual = abiertos.get()
            # print(celdaActual)
            celdaActual = self.mapa.laberinto[celdaActual[0]][celdaActual[1]]
            # Se marca el nodo como cerrado y se mete a cerrados
            celdaActual.setMarcas({"A": 0, "C": 1, "V": 1})
            cerrados.append(celdaActual)
            # El agente se mueve a ese nodo

            if self.cuenta == 0:
                self.HL.append([celdaActual.puntoX, celdaActual.puntoY])
            if self.cuenta == 1:
                self.HP.append([celdaActual.puntoX, celdaActual.puntoY])
            if self.cuenta == 2:
                self.HT.append([celdaActual.puntoX, celdaActual.puntoY])
            if self.cuenta == 3:
                self.ML.append([celdaActual.puntoX, celdaActual.puntoY])
            if self.cuenta == 4:
                self.MP.append([celdaActual.puntoX, celdaActual.puntoY])
            if self.cuenta == 5:
                self.MT.append([celdaActual.puntoX, celdaActual.puntoY])
            if self.cuenta == 6:
                self.PL.append([celdaActual.puntoX, celdaActual.puntoY])
            if self.cuenta == 7:
                self.PP.append([celdaActual.puntoX, celdaActual.puntoY])
            if self.cuenta == 8:
                self.PT.append([celdaActual.puntoX, celdaActual.puntoY])

            agente.mover(self.mapa, celdaActual.puntoX, celdaActual.puntoY)
            puntoX = agente.posicionX
            puntoY = agente.posicionY
            costoCelda = self.mapa.laberinto[puntoX][puntoY].sumaDC

            for i in range(4):
                x = puntoX+dirX[i]
                y = puntoY+dirY[i]
                if(x >= 0 and x < len(self.mapa.laberinto) and y >= 0 and y < len(self.mapa.laberinto[0])):
                    # Verificar que el nodo no lo hayamos metido a abiertos o cerrados
                    if self.mapa.laberinto[x][y] not in consulta:
                        # Verificar que el agente se pueda mover a esa casilla
                        if agente.dificultad[self.mapa.laberinto[x][y].terreno] != 0:
                            self.mapa.laberinto[x][y].calcular(
                                agente, posX, posY, costoCelda)
                            abiertos.put([self.mapa.laberinto[x][y].sumaDC, [
                                         self.mapa.laberinto[x][y].puntoX, self.mapa.laberinto[x][y].puntoY]])
                            consulta.append(self.mapa.laberinto[x][y])

            # Si ya vimos al nodo destino, acabar el algortimo
            if self.mapa.laberinto[posX][posY] in consulta:
                # Se marca como visitado y se limpian los registros
                self.mapa.laberinto[posX][posY].calcular(
                    agente, posX, posY, costoCelda)
                self.mapa.laberinto[posX][posY].setMarcas({"V": 1, "A": 1})
                celdaObjetivo = self.mapa.laberinto[posX][posY].sumaDC

                while not abiertos.empty():
                    try:
                        abiertos.get(False)
                    except Empty:
                        continue
                    abiertos.task_done()
                cerrados.clear()
                consulta.clear()
                self.mapa.borrarMarcas()
                self.mapa.limpiarDatos()
                self.cuenta += 1
                return celdaObjetivo

    def asignarMision(self):
        # Donde se van a agregar la tarea de cada agente
        # 0 es de la llave, 1 del templo y 2 de las piedras
        totalMisiones = []
        # Tiene el costo, y las tareas de cada agente para obtener el costo
        misiones = {}
        total = 0
        # Probamos todas las combinaciones para sacar el costo total minimo
        for i in range(len(self.humano.costos)):
            if self.humano.costos[i][1] == -1:
                continue
            total = self.humano.costos[i][1]
            totalMisiones.append(i)
            for j in range(len(self.mono.costos)):
                if self.mono.costos[j][1] == -1:
                    continue
                total += self.mono.costos[j][1]
                totalMisiones.append(j)
                for k in range(len(self.pulpo.costos)):
                    if self.pulpo.costos[k][1] == -1:
                        continue
                    if i == j or i == k or j == k:
                        continue
                    # Costo total
                    total += self.pulpo.costos[k][1]
                    totalMisiones.append(k)
                    # Se guarda una copia, si no se pone [:] la lista se sigue modificando
                    misiones[total] = totalMisiones[:]
                    totalMisiones.pop()
                    total -= self.pulpo.costos[k][1]
                totalMisiones.pop()
                total -= self.mono.costos[j][1]
            totalMisiones.pop()
            total -= self.humano.costos[i][1]

        # Se ordenan para sacar la menor
        misionesOrdenadas = sorted(misiones)
        if len(misionesOrdenadas) == 0:
            print("No hay solucion")
        else:
            print("Costo total: ", misionesOrdenadas[0])
            misionesFinales = misiones[misionesOrdenadas[0]]
            agentes = [self.humano, self.mono, self.pulpo]
            objetivos = ["Llave", "Templo", "Piedras"]
            for i in range(len(misionesFinales)):
                print(type(agentes[i]).__name__)
                print(objetivos[misionesFinales[i]])
                if type(agentes[i]).__name__ == "Humano":
                    if objetivos[misionesFinales[i]] == "Llave":
                        print("Camino: ", self.HL)
                    elif objetivos[misionesFinales[i]] == "Templo":
                        print("Camino: ", self.HT)
                    elif objetivos[misionesFinales[i]] == "Piedras":
                        print("Camino: ", self.HP)
                if type(agentes[i]).__name__ == "Mono":
                    if objetivos[misionesFinales[i]] == "Llave":
                        print("Camino: ", self.ML)
                    elif objetivos[misionesFinales[i]] == "Templo":
                        print("Camino: ", self.MT)
                    elif objetivos[misionesFinales[i]] == "Piedras":
                        print("Camino: ", self.MP)
                if type(agentes[i]).__name__ == "Pulpo":
                    if objetivos[misionesFinales[i]] == "Llave":
                        print("Camino: ", self.PL)
                    elif objetivos[misionesFinales[i]] == "Templo":
                        print("Camino: ", self.PT)
                    elif objetivos[misionesFinales[i]] == "Piedras":
                        print("Camino: ", self.PP)
                print("Costo a {}: {}".format(
                    objetivos[misionesFinales[i]], agentes[i].costos[misionesFinales[i]][0]))
                print("Costo a portal: {}".format(
                    agentes[i].costos[misionesFinales[i]][1]))
            print("")
        self.acabarApp()

    def imprimirCostos(self, agente):
        nombres = ["Llave", "Templo", "Piedras"]
        for i in range(3):
            print("Costo {} a {}: {}".format(
                type(agente).__name__, nombres[i], agente.costos[i][0]))
            print("Costo {} a {} y portal: {}".format(
                type(agente).__name__, nombres[i], agente.costos[i][1]))

        print("")
        """
        print("Caminos:")
        print("HL:", self.HL)
        print("HP:", self.HP)
        print("HT:", self.HT)
        print("ML:", self.ML)
        print("MP:", self.MP)
        print("MT:", self.MT)
        print("PL:", self.PL)
        print("PP:", self.PP)
        print("PT:", self.PT)
        """

    def marcarCaminoOptimo(self, camino):

        #Prioridad (Abajo,Arriba,Derecha,Izquierda)
        # Como es una pila la prioridad va a quedar volteada
        #Prioridad (Izquierda,Derecha,Arriba,Abajo)
        dirX = [1, -1, 0, 0]
        dirY = [0, 0, 1, -1]

        for i in range(4):
            costoAnterior = self.mapa.laberinto[camino[-1]
                                                [0]][camino[-1][1]].sumaDC
            x = camino[-1][0]+dirX[i]
            y = camino[-1][1]+dirY[i]
            # Checa si la celda a la que se quiere mover esta dentro de los limtes
            if(x >= 0 and x < len(self.mapa.laberinto) and y >= 0 and y < len(self.mapa.laberinto[0])):
                # Checa si esta en la lista de cerrados y si su costo es menor a la celda anterior
                if(self.mapa.laberinto[x][y].marcas["C"] != 0 and self.mapa.laberinto[x][y].sumaDC <= costoAnterior):
                    camino.append([x, y])
                    self.mapa.laberinto[x][y].setColorOptimo()
                    # Hasta que llegue al inicio se detiene
                    if(self.mapa.laberinto[x][y].marcas["I"] == 0):
                        # print(camino[-1])
                        return self.marcarCaminoOptimo(camino)
                    else:
                        return camino

    def acabarApp(self):
        messagebox.showinfo("Terminó el programa", "Fin")
        r = messagebox.askquestion("Reiniciar", "Reiniciar?")
        if r == "yes":
            self.pedirPuntos()


app = App()
