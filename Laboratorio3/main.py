from direccion import Direccion
from fecha import Fecha
from usuario import Usuario
from agenda import Agenda

if __name__ == "__main__":

    agenda = Agenda(5)
    usuario1 = Usuario("Alberto-Guzman","1252535343",Fecha(1,3,2000),"Envigado",3454434,"aguzman@unal.edu.co",Direccion("kr74","Medellin","4T-35","Boston"))
    usuario2 = Usuario("Marta-Gonzales","3345345535",Fecha(31,12,1985),"Medellin",2536378,"mgonzales@unal.edu.co",Direccion("cll65","Medellin","3-29","Robledo","Balcones-de-la-Quinta","405"))
    usuario3 = Usuario("Alizon-Peña","2342342343",Fecha(23,1,2024),"Guatape",3674685,"apeña@unal.edu.co",Direccion("tr45","Medellin","4S-73","Poblado"))
    usuario4 = Usuario("Alfredo-Ospina","3735737263",Fecha(15,7,2015),"Rionegro",3213105,"aospina@unal.edu.co",Direccion("kr23","Envigado","8-10","SanJuan","Mirador","503"))
    usuario5 = Usuario("Susana-Duque","3645274482",Fecha(4,8,2006),"El Carmen de Viboral",3750024,"sduque@unal.edu.co",Direccion("cll5","Medellin","4S-69", "Poblado","UrbColina", "1023"))
    
    agenda.agregar(usuario1)
    agenda.agregar(usuario2)
    agenda.agregar(usuario3)
    agenda.agregar(usuario4)
    agenda.agregar(usuario5)

    #print(agenda.agregar(usuario1))
    #print(agenda.agregar(usuario2))
    #print(agenda.agregar(usuario3))
    #print(agenda.agregar(usuario4))
    #print(agenda.agregar(usuario5))
    "________________________________________________________________________________________"
   
    #print(agenda.buscar(3645274482))

    id = input("Ingrese una ID: ")
    if agenda.buscar(id) == -1:
        print(agenda.buscar(id), "No existe un usuario con esa ID")
    else:
        print(agenda.buscar(id))

    "___________________________________________________________________________________________"
    agenda.toFile("Laboratorio3/Agenda.txt")
    
