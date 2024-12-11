from nodoDoble import NodoDoble

class ListaDoble:

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
        
    def primero(self):
        return self._cabeza

    def ultimo(self):
        return self._cola

    def agregarPrimero(self,dato):
        nodo = NodoDoble(dato)
        if self.isEmpty():
            self._cabeza = nodo
            self._cola = nodo
        
        else:
            nodo.setSiguiente(self._cabeza)
            self._cabeza.setAnterior(nodo)
            self._cabeza = nodo
        
        self._tamaño += 1
    
    def agregarUltimo(self,dato):
        nodo = NodoDoble(dato)
        if self.isEmpty():
            self._cabeza = nodo
            self._cola = nodo
        
        else:
            self._cola.setSiguiente(nodo)
            nodo.setAnterior(self._cola)
            self._cola = nodo

        self._tamaño += 1

    def eliminarPrimero(self):
        if self.isEmpty():
            return None
        
        else:
            temporal = self._cabeza
            self._cabeza = temporal.getSiguiente()
            temporal.setSiguiente(None)
            self._cabeza.setAnterior(None)
            self._tamaño -= 1
            return temporal.getDato()

    def eliminarUltimo(self):
        if self.isEmpty():
            return None

        else:
            temporal = self._cola
            self._cola = temporal.getAnterior()
            self._cola.setSiguiente(None)
            temporal.setAnterior(None)
            self._tamaño -= 1
            return temporal.getDato()

    def eliminar(self,nodo):
        if nodo == self._cabeza:
            return self.eliminarPrimero()
        
        elif nodo == self._cola:
            return self.eliminarUltimo()

        else:
            temporal = nodo
            temporalS = temporal.getSiguiente()
            temporalA = temporal.getAnterior()
            temporalS.setAnterior(temporalA)
            temporalA.setSiguiente(temporalS)
            temporal.setAnterior(None)
            temporal.setSiguiente(None)
            self._tamaño -= 1
            return temporal.getDato()
    
    def agregarAntes(self,nodo,dato):
        if nodo == self._cabeza:
            self.agregarPrimero(dato)
        
        else:
            nuevoNodo = NodoDoble(dato)
            nodoAnterior = nodo.getAnterior()
            nodoAnterior.setSiguiente(nuevoNodo)
            nuevoNodo.setAnterior(nodoAnterior)
            nuevoNodo.setSiguiente(nodo)
            nodo.setAnterior(nuevoNodo)
            self._tamaño += 1
    
    def agregarDespues(self,nodo,dato):
        if nodo == self._cola:
            self.agregarUltimo(dato)
        
        else:
            nuevoNodo = NodoDoble(dato)
            nodoSiguiente = nodo.getSiguiente()
            nodoSiguiente.setAnterior(nuevoNodo)
            nodo.setSiguiente(nuevoNodo)
            nuevoNodo.setAnterior(nodo)
            nuevoNodo.setSiguiente(nodoSiguiente)
            self._tamaño += 1