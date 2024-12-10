from listaDoble import ListaDoble

if __name__ == "__main__":

    listaDoble = ListaDoble()

    listaDoble.agregarPrimero(1)
    listaDoble.agregarUltimo(2)
    listaDoble.agregarUltimo(4)
    listaDoble.agregarUltimo(6)
    listaDoble.agregarUltimo(8)
    listaDoble.agregarUltimo(10)
    listaDoble.agregarUltimo(12)
    listaDoble.agregarUltimo(14)
    listaDoble.agregarUltimo(16)
    listaDoble.agregarUltimo(18)
    listaDoble.agregarUltimo(20)

    nodoDoble = listaDoble.primero()
    indice = listaDoble.tamaño()

    while indice > 0:
        print(nodoDoble.getDato())
        nodoDoble = nodoDoble.getSiguiente()
        indice -= 1

    listaDoble.eliminarPrimero()
    listaDoble.eliminarUltimo()
    nodo10 = listaDoble.primero()

    while nodo10.getDato() != 10:
        nodo10 = nodo10.getSiguiente()

    listaDoble.eliminar(nodo10)
    print("___________________________________________________________________________________________________________________________________________")
    subIndice = listaDoble.tamaño()
    subNodoDoble = listaDoble.primero()
    
    while subIndice > 0:
        print(subNodoDoble.getDato())
        subNodoDoble = subNodoDoble.getSiguiente()
        subIndice -= 1