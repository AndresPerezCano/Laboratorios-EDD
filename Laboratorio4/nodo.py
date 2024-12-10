class Nodo:
    
    def __init__(self,dato=None):
        self._dato = dato
        self._siguiente = None
    
    def setDato(self,dato):
        self._dato = dato

    def getDato(self):
        return self._dato
    
    def setSiguiente(self,siguiente):
        self._siguiente = siguiente
    
    def getSiguiente(self):
        return self._siguiente
    
