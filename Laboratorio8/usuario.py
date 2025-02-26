class Usuario:
    def __init__(self,nombre=None,id=None):
        self._nombre = nombre
        self._id = id
        self._key = self.sumaDigitos()
        
    def setNombre(self, n):
        self._nombre = n

    def setId(self, id):
        self._id = id
    
    def setKey(self, key):
        self._key = key

    def getNombre(self):
        return self._nombre 

    def getId(self):
        return self._id

    def getKey(self):
        return self._key

    def sumaDigitos(self):
        return sum(int(digit) for digit in str(self._id))
    
    def __str__(self):
        return f"{self.getNombre()}/{self.getId()}"
