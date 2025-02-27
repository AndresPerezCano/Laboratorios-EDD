from bSTEntry import BSTEntry
from nodoDoble import NodoDoble
from usuario import Usuario
from binaryTree import BinaryTree
class BinarySearchTree(BinaryTree):
 
    def find(self,k):
        return self.searchTree(k,self._root)
    
    def searchTree(self,k, nodo):
        if nodo != None:
            u = nodo.getDato()
            if k == u.getKey():
                return nodo
        
            else:
             
                if k < u.getKey():
                    return self.searchTree(k,nodo.getAnterior())

                else:
                    return self.searchTree(k,nodo.getSiguiente())
        
        else:
            print("No se encuentra")

    def insert(self, dato, key):
        o = BSTEntry(dato,key)
        if  self.isEmpty():
            self.addRoot(o)
        
        else:
            self.addEntry(self._root,o)
            self._size += 1

    def addEntry(self, nodo, o):
        temp = nodo.getDato()
        nD = NodoDoble(o)
        if o.getKey() < temp.getKey():
            
            if self.hasLeft(nodo):
                self.addEntry(self.left(nodo),o)

            else:
                nodo.setAnterior(nD)

        else:
            if self.hasRight(nodo):
                self.addEntry(self.right(nodo),o)
            
            else:
                nodo.setSiguiente(nD)

    def remove(self,key):
        v = self.find(key)
        temp = v.getDato()
        if self.hasLeft(v) and self.hasRight(v):
            w = self.predecesor(v)
            v.setDato(w.getDato())
            super().remove(w)
        
        else:
            super().remove(v)
    
        return temp

    def predecesor(self, v):
        temp = v.getAnterior()
        return self.maxNode(temp)

    def maxNode(self, temp):
        if self.hasRight(temp):
            return self.maxNode(self.right(temp))

        else:
            return temp
    
    def print_tree(self):
        self._print_tree(self._root, 0)

    def _print_tree(self, node, level):
        if node is not None:
            # Primero imprimimos el hijo derecho (más profundo), luego el nodo, luego el hijo izquierdo
            self._print_tree(node.getSiguiente(), level + 1)
            print("   " * level + f"({node.getDato().getDato()})")
            self._print_tree(node.getAnterior(), level + 1)
        
    def min(self,T,nodo):
        if T.hasLeft(nodo):
            return self.min(T,T.left(nodo))
        else:
            return nodo.getDato().getDato()

    def max(self,T,nodo):
        if T.hasRight(nodo):
            return self.max(T,T.right(nodo))
        else:
            return nodo.getDato().getDato()

    def inorder(self,T,nodo):
        if T.hasLeft(nodo):
            self.inorder(T,T.left(nodo))
        print(f"{nodo.getDato().getKey()}({nodo.getDato().getDato()})  ",end="")
        if T.hasRight(nodo):
            self.inorder(T,T.right(nodo))

if __name__ == "__main__":
    #"""
    #Primer Punto
    ABB1 = BinarySearchTree()
    ABB1.insert(5,5)
    ABB1.insert(2,2)
    ABB1.insert(1,1)
    ABB1.insert(3,3)
    ABB1.insert(7,7)
    ABB1.insert(10,10)
    ABB1.insert(9,9)
    ABB1.insert(12,12)
    ABB1.insert(11,11)
    ABB1.insert(0,0)
    ABB1.print_tree()

    print("__________________________________________________________________________________________________________________________")
    #Eliminar elementos
    ABB1.remove(12)
    ABB1.remove(5)
    ABB1.print_tree()
    print("__________________________________________________________________________________________________________________________")
    #buscar el nodo
    print(ABB1.find(7).getDato().getDato())
    print(ABB1.find(9).getDato().getDato())
    print("__________________________________________________________________________________________________________________________")
    
    #Valor maximo y minimo
    print("Valor con la clave más grande: ",ABB1.max(ABB1,ABB1._root))
    print("Valor con la clave más pequeña: ",ABB1.min(ABB1,ABB1._root))
    print("__________________________________________________________________________________________________________________________")
    #recorrido inorder
    ABB1.inorder(ABB1,ABB1._root)

    """
    #Segundo punto
    usuario1 = Usuario("Juan", 10101013)
    usuario2 = Usuario("Pablo", 10001011)
    usuario3 = Usuario("Maria", 10101015)
    usuario4 = Usuario("Ana", 1010000)
    usuario5 = Usuario("Diana", 10111105)
    usuario6 = Usuario("Mateo", 10110005)
    usuario7 = Usuario("Andres", 11111000)
    usuario8 = Usuario("Camilo", 111110600)

    #Agregar elementos
    ABB = BinarySearchTree()
    ABB.insert(usuario1,usuario1.getKey())
    ABB.insert(usuario2,usuario2.getKey())
    ABB.insert(usuario3,usuario3.getKey())
    ABB.insert(usuario4,usuario4.getKey())
    ABB.insert(usuario5,usuario5.getKey())
    ABB.insert(usuario6,usuario6.getKey())
    ABB.insert(usuario7,usuario7.getKey())
    ABB.insert(usuario8,usuario8.getKey())
    
    ABB.print_tree()
    print("__________________________________________________________________________________________________________________________")
    #Eliminar elementos
    ABB.remove(usuario8.getKey())
    ABB.remove(usuario3.getKey())
    ABB.print_tree()
    print("__________________________________________________________________________________________________________________________")
    #buscar el nodo
    print(ABB.find(usuario4.getKey()))
    print(ABB.find(usuario4.getKey()).getDato().getDato())
    print("__________________________________________________________________________________________________________________________")
    
    #Valor maximo y minimo
    print("Valor con la clave más grande: ",ABB.max(ABB,ABB._root))
    print("Valor con la clave más pequeña: ",ABB.min(ABB,ABB._root))
    print("__________________________________________________________________________________________________________________________")
    #recorrido inorder
    ABB.inorder(ABB,ABB._root)
    """