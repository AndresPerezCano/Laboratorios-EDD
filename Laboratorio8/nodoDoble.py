class NodoDoble:

    def __init__(self,dato=None):
        self._dato = dato
        self.siguiente = None
        self.anterior = None

    def setDato(self,dato):
        self._dato = dato

    def setSiguiente(self,siguiente):
        self.siguiente = siguiente

    def setAnterior(self,anterior):
        self.anterior = anterior
    
    def getDato(self):
        return self._dato 
    
    def getSiguiente(self):
        return self.siguiente
    
    def getAnterior(self):
        return self.anterior
    