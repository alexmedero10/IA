class Agente:
    sensores = {}
    vueltas = {}
    movimientos = {}
    posicionX = 0
    posicionY = 0
    puntaje = 0
    pasos = 0
    vista = "R"

    def voltearIzquierda(self, mapa):
        if self.vueltas["L"] == 1:
            if self.vista == "R":
                self.vista = "U"
            elif self.vista == "U":
                self.vista = "L"
            elif self.vista == "L":
                self.vista = "D"
            elif self.vista == "D":
                self.vista = "R"
            self.quitarMarcas(mapa)
            if self.sensores["R"] == 1:
                self.setSensores({"L": 0, "R": 0, "U": 1, "D": 0})
                self.setMovimientos({"F": 1, "B": 0, "L": 0, "R": 0})
            elif self.sensores["U"] == 1:
                self.setSensores({"L": 1, "R": 0, "U": 0, "D": 0})
                self.setMovimientos({"F": 0, "B": 0, "L": 1, "R": 0})
            elif self.sensores["L"] == 1:
                self.setSensores({"L": 0, "R": 0, "U": 0, "D": 1})
                self.setMovimientos({"F": 0, "B": 1, "L": 0, "R": 0})
            elif self.sensores["D"] == 1:
                self.setSensores({"L": 0, "R": 1, "U": 0, "D": 0})
                self.setMovimientos({"F": 0, "B": 0, "L": 0, "R": 1})

            self.usarSensores(mapa)
            self.pasos += 1

    def voltearDerecha(self, mapa):
        if self.vueltas["R"] == 1:
            if self.vista == "R":
                self.vista = "D"
            elif self.vista == "D":
                self.vista = "L"
            elif self.vista == "L":
                self.vista = "U"
            elif self.vista == "U":
                self.vista = "R"
            self.quitarMarcas(mapa)
            if self.sensores["R"] == 1:
                self.setSensores({"L": 0, "R": 0, "U": 0, "D": 1})
                self.setMovimientos({"F": 0, "B": 1, "L": 0, "R": 0})
            elif self.sensores["D"] == 1:
                self.setSensores({"L": 1, "R": 0, "U": 0, "D": 0})
                self.setMovimientos({"F": 0, "B": 0, "L": 1, "R": 0})
            elif self.sensores["L"] == 1:
                self.setSensores({"L": 0, "R": 0, "U": 1, "D": 0})
                self.setMovimientos({"F": 1, "B": 0, "L": 0, "R": 0})
            elif self.sensores["U"] == 1:
                self.setSensores({"L": 0, "R": 1, "U": 0, "D": 0})
                self.setMovimientos({"F": 0, "B": 0, "L": 0, "R": 1})

            self.usarSensores(mapa)
            self.pasos += 1

    def mover(self, mapa, direccion):
        if direccion == "R":
            if self.movimientos["R"] == 1:
                if self.posicionY+1 < len(mapa.laberinto[self.posicionY]):
                    if self.dificultad[mapa.laberinto[self.posicionX][self.posicionY+1].terreno] != 0:
                        self.quitarMarcas(mapa)
                        mapa.laberinto[self.posicionX][self.posicionY+1].setColor()
                        mapa.laberinto[self.posicionX][self.posicionY +
                                                       1].setMarcas({"V": 0, "O": 0, "X": 1})
                        mapa.laberinto[self.posicionX][self.posicionY].setMarcas(
                            {"V": 1, "O": 0, "X": 0})
                        self.puntaje += self.dificultad[mapa.laberinto[self.posicionX]
                                                        [self.posicionY+1].terreno]
                        self.pasos += 1
                        self.posicionY = self.posicionY+1
        elif direccion == "L":
            if self.movimientos["L"] == 1:
                if self.posicionY > 0:
                    if self.dificultad[mapa.laberinto[self.posicionX][self.posicionY-1].terreno] != 0:
                        self.quitarMarcas(mapa)
                        mapa.laberinto[self.posicionX][self.posicionY-1].setColor()
                        mapa.laberinto[self.posicionX][self.posicionY -
                                                       1].setMarcas({"V": 0, "O": 0, "X": 1})
                        mapa.laberinto[self.posicionX][self.posicionY].setMarcas(
                            {"V": 1, "O": 0, "X": 0})
                        self.puntaje += self.dificultad[mapa.laberinto[self.posicionX]
                                                        [self.posicionY-1].terreno]
                        self.pasos += 1
                        self.posicionY = self.posicionY-1
        elif direccion == "F":
            if self.movimientos["F"] == 1:
                if self.posicionX > 0:
                    if self.dificultad[mapa.laberinto[self.posicionX-1][self.posicionY].terreno] != 0:
                        self.quitarMarcas(mapa)
                        mapa.laberinto[self.posicionX -
                                       1][self.posicionY].setColor()
                        mapa.laberinto[self.posicionX -
                                       1][self.posicionY].setMarcas({"V": 0, "O": 0, "X": 1})
                        mapa.laberinto[self.posicionX][self.posicionY].setMarcas(
                            {"V": 1, "O": 0, "X": 0})
                        self.puntaje += self.dificultad[mapa.laberinto[self.posicionX-1]
                                                        [self.posicionY].terreno]
                        self.pasos += 1
                        self.posicionX = self.posicionX-1
        elif direccion == "B":
            if self.movimientos["B"] == 1:
                if self.posicionX+1 < len(mapa.laberinto):
                    if self.dificultad[mapa.laberinto[self.posicionX+1][self.posicionY].terreno] != 0:
                        self.quitarMarcas(mapa)
                        mapa.laberinto[self.posicionX +
                                       1][self.posicionY].setColor()
                        mapa.laberinto[self.posicionX +
                                       1][self.posicionY].setMarcas({"V": 0, "O": 0, "X": 1})
                        mapa.laberinto[self.posicionX][self.posicionY].setMarcas(
                            {"V": 1, "O": 0, "X": 0})
                        self.puntaje += self.dificultad[mapa.laberinto[self.posicionX+1]
                                                        [self.posicionY].terreno]
                        self.pasos += 1
                        self.posicionX = self.posicionX+1

    def usarSensores(self, mapa):
        if self.sensores["R"] == 1:
            if self.posicionY+1 < len(mapa.laberinto[self.posicionY]):
                mapa.laberinto[self.posicionX][self.posicionY+1].setColor()
                if self.dificultad[mapa.laberinto[self.posicionX][self.posicionY+1].terreno] != 0:
                    mapa.laberinto[self.posicionX][self.posicionY +
                                                   1].setMarcas({"O": 1})
        if self.sensores["L"] == 1:
            if self.posicionY > 0:
                mapa.laberinto[self.posicionX][self.posicionY-1].setColor()
                if self.dificultad[mapa.laberinto[self.posicionX][self.posicionY-1].terreno] != 0:
                    mapa.laberinto[self.posicionX][self.posicionY -
                                                   1].setMarcas({"O": 1})
        if self.sensores["U"] == 1:
            if self.posicionX > 0:
                mapa.laberinto[self.posicionX-1][self.posicionY].setColor()
                if self.dificultad[mapa.laberinto[self.posicionX-1][self.posicionY].terreno] != 0:
                    mapa.laberinto[self.posicionX -
                                   1][self.posicionY].setMarcas({"O": 1})
        if self.sensores["D"] == 1:
            if self.posicionX+1 < len(mapa.laberinto):
                mapa.laberinto[self.posicionX+1][self.posicionY].setColor()
                if self.dificultad[mapa.laberinto[self.posicionX+1][self.posicionY].terreno] != 0:
                    mapa.laberinto[self.posicionX +
                                   1][self.posicionY].setMarcas({"O": 1})

    def quitarMarcas(self, mapa):
        if self.sensores["R"] == 1:
            if self.posicionY+1 < len(mapa.laberinto[self.posicionY]):
                if self.dificultad[mapa.laberinto[self.posicionX][self.posicionY+1].terreno] != 0:
                    mapa.laberinto[self.posicionX][self.posicionY +
                                                   1].setMarcas({"V": 0, "O": 0, "X": 0})
        if self.sensores["L"] == 1:
            if self.posicionY > 0:
                if self.dificultad[mapa.laberinto[self.posicionX][self.posicionY-1].terreno] != 0:
                    mapa.laberinto[self.posicionX][self.posicionY -
                                                   1].setMarcas({"V": 0, "O": 0, "X": 0})
        if self.sensores["U"] == 1:
            if self.posicionX > 0:
                if self.dificultad[mapa.laberinto[self.posicionX-1][self.posicionY].terreno] != 0:
                    mapa.laberinto[self.posicionX -
                                   1][self.posicionY].setMarcas({"V": 0, "O": 0, "X": 0})
        if self.sensores["D"] == 1:
            if self.posicionX+1 < len(mapa.laberinto):
                if self.dificultad[mapa.laberinto[self.posicionX+1][self.posicionY].terreno] != 0:
                    mapa.laberinto[self.posicionX +
                                   1][self.posicionY].setMarcas({"V": 0, "O": 0, "X": 0})

    def setSensores(self, sensores):
        self.sensores = sensores

    def setVueltas(self, vueltas):
        self.vueltas = vueltas

    def setMovimientos(self, movimientos):
        self.movimientos = movimientos

    def setPosicion(self, x, y):
        self.posicionX = x
        self.posicionY = y


class Humano(Agente):
    def __init__(self):
        self.dificultad = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 5}


class Mono(Agente):
    def __init__(self):
        self.dificultad = {0: 0, 1: 2, 2: 4, 3: 3, 4: 1, 5: 5, 6: 0}


class Pulpo(Agente):
    def __init__(self):
        self.dificultad = {0: 0, 1: 2, 2: 1, 3: 0, 4: 3, 5: 2, 6: 0}


class PieGrande(Agente):
    def __init__(self):
        self.dificultad = {0: 15, 1: 4, 2: 0, 3: 0, 4: 4, 5: 5, 6: 3}


class AgenteP2(Agente):
    def __init__(self):
        self.dificultad = {0: 0, 1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
