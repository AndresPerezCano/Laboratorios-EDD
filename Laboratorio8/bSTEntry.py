class BSTEntry:
    
    def __init__(self, dato, clave):
        self._dato = dato
        self._clave = clave

    def getDato(self):
        return self._dato

    def getKey(self):
        return self._clave
    
    def setDato(self,dato):
        self._dato = dato

    def setKey(self,clave):
        self._clave = clave