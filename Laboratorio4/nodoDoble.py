class NodoDoble:

    def __init__(self,dato=None):
        self._dato = dato
        self._siguiente = None
        self._anterior = None

    def setDato(self,dato):
        self._dato = dato

    def setSiguiente(self,siguiente):
        self._siguiente = siguiente

    def setAnterior(self,anterior):
        self._anterior = anterior
    
    def getDato(self):
        return self._dato 
    
    def getSiguiente(self):
        return self._siguiente
    
    def getAnterior(self):
        return self._anterior
    