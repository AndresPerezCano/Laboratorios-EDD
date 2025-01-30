from listaSimple import ListaSimple
class Stack:
    
    def __init__(self):
        self._lista = ListaSimple()

    def size(self):
        return self._lista.tamaño()

    def isEmpty(self):
        return self._lista.isEmpty()

    def push(self, dato):
        self._lista.agregarPrimero(dato)

    def pop(self):
        return self._lista.eliminarPrimero()

    def top(self):
        return self._lista.primero()

if __name__ == "__main__":

    pila = Stack()
    pila.push(10)
    pila.push(8)
    pila.push(6)
    pila.push(4)
    pila.push(2)
    
    i = pila.size()
    while i > 0:
        print(pila.pop(),end=" ")
        i -= 1



