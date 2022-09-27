from gestion.zona import Zona

class Zoologico:
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def agregarzonas(self, zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        total = 0
        for i in self._zonas:
            total += i.cantidadAnimales()
        return total

    def getNombre(self):
        return self._nombre

    def setNombre(self,nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion

    def setNombre(self,ubicacion):
        self._ubicacion = ubicacion

    def getZonas(self):
        return self._zonas

    def setZonas(self,zonas):
        self._zonas = zonas