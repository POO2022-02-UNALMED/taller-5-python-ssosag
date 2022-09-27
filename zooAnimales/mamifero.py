from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0
    nMamiferos = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.nMamiferos += 1

    @classmethod
    def cantidadMamiferos(clc):
        return Mamifero.nMamiferos

    def crearCaballo(self, nombre, edad, genero):
        caballo = Mamifero(nombre, edad, 'pradera', genero, True, 4)
        Mamifero.caballos += 1
        return caballo

    def crearLeon(self, nombre, edad, genero):
        leon = Mamifero(nombre, edad, 'selva', genero, True, 4)
        Mamifero.leones += 1
        return leon

    def getPelaje(self):
        return self._pelaje

    def setPelaje(self,pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._patas

    def setPatas(self,patas):
        self._patas = patas

    @classmethod
    def getListado(clc):
        return clc._listado

    @classmethod
    def setListado(self,listado):
        self._listado = listado