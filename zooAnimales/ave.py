from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0
    nAves = 0

    def __init__(self, nombre, edad, habitat, genero, zona, colorPlumas):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorPlumas = colorPlumas
        Ave.nAves += 1

    @classmethod
    def cantidadAves(clc):
        return Ave.nAves

    def crearHalcon(self, nombre, edad, genero, zona):
        halcon = Ave(nombre, edad, 'montanas', genero, zona, 'cafe glorioso')
        Ave.halcones += 1
        return halcon

    def crearAguila(self, nombre, edad, genero, zona):
        aguila = Ave(nombre, edad, 'montanas', genero, zona, 'blanco y amarillo')
        Ave.aguilas += 1
        return aguila

    @classmethod
    def getListado(clc):
        return clc._listado

    @classmethod
    def setListado(clc, listado):
        clc._listado = listado

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self,color):
        self._colorPlumas = color