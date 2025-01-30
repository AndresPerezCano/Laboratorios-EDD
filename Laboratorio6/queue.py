from listaSimple import ListaSimple
class Queue:

    def __init__(self):
        self._lista = ListaSimple()

    def size(self):
        return self._lista.tamaño()

    def isEmpty(self):
        return self._lista.isEmpty()
 
    def enqueue(self, dato):
        self._lista.agregarUltimo(dato)

    def dequeue(self):
        return self._lista.eliminarPrimero()

    def first(self):
        return self._lista.primero()

if __name__ == "__main__":

    cola = Queue()
    cola.enqueue(2)
    cola.enqueue(4)
    cola.enqueue(6)
    cola.enqueue(8)
    cola.enqueue(10)
    
    i = cola.size()
    while i > 0:
        print(cola.dequeue(),end=" ")
        i -= 1