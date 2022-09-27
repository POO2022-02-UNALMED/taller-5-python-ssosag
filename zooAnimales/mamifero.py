from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0
    nMamiferos = 0

    def __init__(self, nombre, edad, habitat, genero, zona, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.nMamiferos += 1

    @classmethod
    def cantidadMamiferos(clc):
        return Mamifero.nMamiferos

    def crearCaballo(self, nombre, edad, genero, zona):
        caballo = Mamifero(nombre, edad, 'pradera', genero, zona, True, 4)
        Mamifero.caballos += 1
        return caballo

    def crearLeon(self, nombre, edad, genero, zona):
        leon = Mamifero(nombre, edad, 'selva', genero, zona, True, 4)
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