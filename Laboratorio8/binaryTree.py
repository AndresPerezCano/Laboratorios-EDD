from queue import Queue
from nodoDoble import NodoDoble
class BinaryTree:
    
    def __init__(self):
        self._root = None
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False
    
    def isRoot(self, nodo):
        if nodo == self._root:
            return True
        else:
            return False
    
    def isInternal(self, nodo):
        if hasLeft(nodo) or hasRight(nodo):
            return True
        else: 
            return False

    def hasLeft(self, nodo):
        if nodo.getAnterior() != None:
            return True
        else:
            return False

    def hasRight(self, nodo):
        if nodo.getSiguiente() != None:
            return True
        else:
            return False

    def depth(self, nodo):
        if self.isRoot(nodo):
            return 0

        else:
            return 1 + self.depth(parent(nodo))

    def height(self, nodo):
        if not(self.isInternal(nodo)):
            return 0

        else:
            h = 0
            h = max(self.height(self.left(nodo)),self.height(self.right(nodo)))
            return 1 + h
    
    def root(self):
        return self._root

    def left(self, nodo):
        return nodo.getAnterior()

    def right(self, nodo):
        return nodo.getSiguiente()

    def parent(self, nodo):
        if self.isRoot(nodo):
            return None

        else:
            q = Queue()
            q.enqueue(self._root)

        while not(q.isEmpty()):
            temp = q.dequeue()
            
            if self.left(temp) == nodo or self.right(temp) == nodo:
                return temp
            
            if self.hasLeft(temp):
                q.enqueue(self.left(temp))
            
            if self.hasRight(temp):
                q.enqueue(self.right(temp))
        return None
        
    def addRoot(self,dato):
        self._root = NodoDoble(dato)
        self._size = 1

    def insertLeft(self, nodo, dato):
        left = NodoDoble(dato)
        nodo.setAnterior(left)
        self._size += 1
    
    def insertRight(self, nodo, dato):
        right = NodoDoble(dato)
        nodo.setSiguiente(right)
        self._size += 1 
    
    def remove(self, nodo):
        p = self.parent(nodo)
        if self.hasLeft(nodo) or self.hasRight(nodo):
            if self.hasLeft(nodo):
                child = self.left(nodo)
            else:
                child = self.right(nodo)
            
            if self.left(p) == nodo:
                p.setAnterior(child)
            else:
                p.setSiguiente(child)
            
            nodo.setAnterior(None)
            nodo.setSiguiente(None)
        else:
            if self.left(p) == nodo:
                p.setAnterior(None)
            else:
                p.setSiguiente(None)
        self._size -= 1

