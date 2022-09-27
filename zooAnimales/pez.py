from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0
    nPeces = 0

    def __init__(self, nombre, edad, habitat, genero, zona, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.nPeces = 1

    @classmethod
    def cantidadPeces(clc):
        return clc.nPeces

    def crearSalmon(self, nombre, edad, genero, zona):
        salmon = Pez(nombre, edad, "oceano", genero, zona, "rojo", 6)
        Pez.salmones += 1
        return salmon

    def crearBacalao(self, nombre, edad, genero, zona):
        bacalao = Pez(nombre, edad, "oceano", genero, zona, "gris", 6)
        Pez.bacalaos += 1
        return bacalao

    @classmethod
    def getListado(clc):
        return clc._listado

    @classmethod
    def setListado(clc, listado):
        clc._listado = listado

    def getColorEscama(self):
        return self._colorEscamas

    def setColorEscama(self,color):
        self._colorEscamas = color

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self,aletas):
        self._cantidadAletas= aletas
