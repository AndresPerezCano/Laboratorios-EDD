from direccion import Direccion
from fecha import Fecha
from usuario import Usuario
from listaSimple import ListaSimple

if __name__ == "__main__":

    print("___________________________________________________________________________________________________________________________________________")
     
    listaUsuarios = ListaSimple()

    usuario1 = Usuario("Alberto-Guzman","1252535343",Fecha(1,3,2000),"Envigado",3454434,"aguzman@unal.edu.co",Direccion("kr74","Medellin","4T-35","Boston"))
    usuario2 = Usuario("Marta-Gonzales","3345345535",Fecha(31,12,1985),"Medellin",2536378,"mgonzales@unal.edu.co",Direccion("cll65","Medellin","3-29","Robledo","Balcones-de-la-Quinta","405"))
    usuario3 = Usuario("Alizon-Peña","2342342343",Fecha(23,1,2024),"Guatape",3674685,"apeña@unal.edu.co",Direccion("tr45","Medellin","4S-73","Poblado"))
    usuario4 = Usuario("Alfredo-Ospina","3735737263",Fecha(15,7,2015),"Rionegro",3213105,"aospina@unal.edu.co",Direccion("kr23","Envigado","8-10","SanJuan","Mirador","503"))
    usuario5 = Usuario("Susana-Duque","3645274482",Fecha(4,8,2006),"El Carmen de Viboral",3750024,"sduque@unal.edu.co",Direccion("cll5","Medellin","4S-69", "Poblado","UrbColina", "1023"))
    
    listaUsuarios.agregarPrimero(usuario1)
    listaUsuarios.agregarUltimo(usuario2)
    listaUsuarios.agregarUltimo(usuario3)
    listaUsuarios.agregarUltimo(usuario4)
    listaUsuarios.agregarUltimo(usuario5)

    nodo = listaUsuarios.primero()
    indice = listaUsuarios.tamaño()

    while indice > 0:
        print(nodo.getDato())
        nodo = nodo.getSiguiente()
        indice -= 1
    print("___________________________________________________________________________________________________________________________________________")
    print("Usuario 1:")
    nombre1 = input("Ingrese un nombre: ")
    id1 = input("ingrese un id: ")
    fechaNacimiento1 = input("Ingrese una fecha de nacimiento(d/m/a):")
    ciudadNacimiento1 = input("Ingrese una ciudad de nacimiento: ")
    tel1 = input("Ingrese un telefono: ")
    email1 = input("Ingrese un email: ")
    dir1 = input("Ingrese una direccion(Ciudad/Calle/Nomenclatura/Barrio/Edificio/Apto): ")
    dia1, mes1, año1 = fechaNacimiento1.split("/")

    if len(dir1.split("/")) == 6:
        ciudad1,calle1,nomenclatura1,barrio1,edificio1,apto1 = dir1.split("/")

    elif len(dir1.split("/")) == 5:
        ciudad1,calle1,nomenclatura1,barrio1,edificio1 = dir1.split("/")
        apto1=None
        
    elif len(dir1.split("/")) == 4:
        ciudad1,calle1,nomenclatura1,barrio1 = dir1.split("/")
        edificio1=None
        apto1=None

    usuarioOne = Usuario(nombre1,id1,Fecha(int(dia1),int(mes1),int(año1)),ciudadNacimiento1,tel1,email1,Direccion(calle1,ciudad1,nomenclatura1,barrio1,edificio1,apto1))
    listaUsuarios.agregarPrimero(usuarioOne)
    print("___________________________________________________________________________________________________________________________________________")
    print("Usuario 2:")
    nombre2 = input("Ingrese un nombre: ")
    id2 = input("ingrese un id: ")
    fechaNacimiento2 = input("Ingrese una fecha de nacimiento(d/m/a):")
    ciudadNacimiento2 = input("Ingrese una ciudad de nacimiento: ")
    tel2 = input("Ingrese un telefono: ")
    email2 = input("Ingrese un email: ")
    dir2 = input("Ingrese una direccion(Ciudad/Calle/Nomenclatura/Barrio/Edificio/Apto): ")
    dia2, mes2, año2 = fechaNacimiento2.split("/")

    if len(dir2.split("/")) == 6:
        ciudad2,calle2,nomenclatura2,barrio2,edificio2,apto2 = dir2.split("/")

    elif len(dir2.split("/")) == 5:
        ciudad2,calle2,nomenclatura2,barrio2,edificio2 = dir2.split("/")
        apto2=None
        
    elif len(dir2.split("/")) == 4:
        ciudad2,calle2,nomenclatura2,barrio2 = dir2.split("/")
        edificio2=None
        apto2=None

    usuarioTwo = Usuario(nombre2,id2,Fecha(int(dia2),int(mes2),int(año2)),ciudadNacimiento2,tel2,email2,Direccion(calle2,ciudad2,nomenclatura2,barrio2,edificio2,apto2))

    listaUsuarios.agregarUltimo(usuarioTwo)
    print("___________________________________________________________________________________________________________________________________________")
    subNodo = listaUsuarios.primero()
    subIndice = listaUsuarios.tamaño()

    while subIndice > 0:
        print(subNodo.getDato())
        subNodo = subNodo.getSiguiente()
        subIndice -= 1

