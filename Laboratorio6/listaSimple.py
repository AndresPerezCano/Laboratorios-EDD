from nodo import Nodo

class ListaSimple:

    def __init__(self):
        self._cabeza = None
        self._cola = None
        self._tamaño = 0

    def tamaño(self):
        return self._tamaño

    def isEmpty(self):
        if self._tamaño == 0:
            return True

        else:
            return False
        
    def setTamaño(self,tamaño):
        self._tamaño = tamaño
    
    def primero(self):
        return self._cabeza

    def ultimo(self):
        return self._cola

    def agregarPrimero(self,dato):
        nodo = Nodo(dato)
        if self.isEmpty():
            self._cabeza = nodo
            self._cola = nodo
        
        else:
            nodo.setSiguiente(self._cabeza)
            self._cabeza = nodo
        self._tamaño += 1
    
    def agregarUltimo(self,dato):
        nodo = Nodo(dato)
        if self.isEmpty():
            self._cabeza = nodo
            self._cola = nodo
        
        else:
            self._cola.setSiguiente(nodo)
            self._cola = nodo
        
        self._tamaño += 1

    def eliminarPrimero(self):
        if not self.isEmpty():
            temporal = self._cabeza
            self._cabeza = temporal.getSiguiente()
            temporal.setSiguiente(None)
            self._tamaño -= 1
            return temporal.getDato()
        
        else:
            return None

    def eliminarUltimo(self):
        if self._tamaño == 1:
            self.eliminarPrimero()

        else:
            temporal = self._cola
            anterior = self._cabeza
            while(anterior.getSiguiente() != self._cola):
                anterior = anterior.getSiguiente() 
            
            anterior.setSiguiente(None) 
            self._cola = anterior
            self._tamaño -= 1
            return temporal.getDato()
        
    def eliminar(self,nodo):
        if nodo == self._cabeza:
            return self.eliminarPrimero()
        
        elif nodo == self._cola:
            return self.eliminarUltimo()

        else:
            nodoAnterior = self._cabeza
            nodoSiguiente = nodo.getSiguiente()

            while nodoAnterior.getSiguiente() != nodo:
                nodoAnterior = nodoAnterior.getSiguiente()
            
            nodoAnterior.setSiguiente(nodoSiguiente)
            nodo.setSiguiente(None)
            self._tamaño -= 1
            return nodo.getDato()









