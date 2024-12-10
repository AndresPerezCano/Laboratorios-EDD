from listaSimple import ListaSimple

if __name__ == "__main__":
    
    listaSimple = ListaSimple()
    listaSimple.agregarPrimero(1)
    listaSimple.agregarUltimo(2)
    listaSimple.agregarUltimo(4)
    listaSimple.agregarUltimo(6)
    listaSimple.agregarUltimo(8)
    listaSimple.agregarUltimo(10)
    listaSimple.agregarUltimo(12)
    listaSimple.agregarUltimo(14)
    listaSimple.agregarUltimo(16)
    listaSimple.agregarUltimo(18)
    listaSimple.agregarUltimo(20)

    nodo = listaSimple.primero()
    indice = listaSimple.tamaño()

    while indice > 0:
        print(nodo.getDato())
        nodo = nodo.getSiguiente()
        indice -= 1

    listaSimple.eliminarPrimero()
    listaSimple.eliminarUltimo()
    nodo10 = listaSimple.primero()

    while nodo10.getDato() != 10:
        nodo10 = nodo10.getSiguiente()
    listaSimple.eliminar(nodo10)
    print("___________________________________________________________________________________________________________________________________________")
    subIndice = listaSimple.tamaño()
    subNodo = listaSimple.primero()
    while subIndice > 0:
        print(subNodo.getDato())
        subNodo = subNodo.getSiguiente()
        subIndice -= 1


