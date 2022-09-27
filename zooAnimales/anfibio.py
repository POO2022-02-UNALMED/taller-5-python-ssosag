from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0
    nAnfibios = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio.nAnfibios += 1

    @classmethod
    def cantidadAnfibios(clc):
        return clc.nAnfibios

    def crearRana(nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.ranas += 1
        return rana

    def crearSalamandra(nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio.salamandras += 1
        return salamandra

    @classmethod
    def getListado(clc):
        return clc._listado

    @classmethod
    def setListado(clc, listado):
        clc._listado = listado

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self,color):
        self._colorPiel = color

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self,venenoso):
        self._venenoso = venenoso