class Animal:

    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales += 1

    def totalPorTipo(self):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio

        cadena = "Mamiferos: " + Mamifero.cantidadMamiferos() + "\n" + \
        "Aves: " + Ave.cantidadAves() + "\n" +\
        "Reptiles: " + Reptil.cantidadReptiles() + "\n" +\
        "Peces: " + Pez.cantidadPeces() + "\n" +\
        "Anfibios: " + Anfibio.cantidadAnfibios()
	    
        return cadena

    def toString(self):
        cadena = 'Mi nombre es ' + self._nombre + ', tengo una edad de' + str(self._edad)\
        + ', habito en ' + self._habitat + ' y mi genero es ' + self._genero
        if (self._zona != None):
            cadenaCompleta = cadena + ', la zona en la que me ubico es ' + self._zona.getNombre() + ', en el ' + self._zona.getZoo.getNombre()
            return cadenaCompleta
        
        return cadena

    def getNombre(self):
        return self._nombre

    def setNombre(self,nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self,edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self,habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self,genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setNombre(self,zona):
        self._zona = zona

    @classmethod
    def getTotalAnimales(clc):
        return clc._totalAnimales

    @classmethod
    def setTotalAnimales(clc,total):
        clc._totalAnimales = total
