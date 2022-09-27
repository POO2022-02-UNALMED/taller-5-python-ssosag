from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0
    nPeces = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.nPeces = 1

    @classmethod
    def cantidadPeces(clc):
        return clc.nPeces

    def crearSalmon(self, nombre, edad, genero):
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.salmones += 1
        return salmon

    def crearBacalao(self, nombre, edad, genero):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.bacalaos += 1
        return bacalao

    @classmethod
    def getListado(clc):
        return clc._listado

    @classmethod
    def setListado(clc, listado):
        clc._listado = listado

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self,color):
        self._colorEscamas = color

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self,aletas):
        self._cantidadAletas= aletas
