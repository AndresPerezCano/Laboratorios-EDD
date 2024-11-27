class Direccion:

    def __init__(self):
        self._calle = None
        self._ciudad = None
        self._nomenclatura = None
        self._edificio = None
        self._barrio = None
        self._apto = None
    
    def setCalle(self, c):
        self._calle = c
        
    def setNomenclatura(self, n):
        self._nomenclatura = n

    def setBarrio(self, b):
        self._barrio = b

    def setCiudad(self, ci):
        self._ciudad = ci

    def setEdificio(self, e):
        self._edificio = e

    def setApto(self, a):
        self._apto = a

    def getCalle(self):
        return self._calle
        
    def getNomenclatura(self):
        return self._nomenclatura

    def getBarrio(self):
        return self._barrio

    def getCiudad(self):
        return self._ciudad

    def getEdificio(self):
        return self._edificio

    def getApto(self):
        return self._apto
        
    def __str__(self):
        return f"{self._ciudad} {self._calle} {self._nomenclatura} {self._barrio} {self._edificio} {self._apto}"
        