from stack import Stack
from queue import Queue
from usuario import Usuario
from fecha import Fecha
from direccion import Direccion
class TurnoUsuario:

    def __init__(self):
        self._registro = Queue()
        self._usuarioAtendidos = Stack()

    def registrar(self, dato):
        self._registro.enqueue(dato)

    def atenderSiguiente(self):
        temporal = self._registro.dequeue()
        self._usuarioAtendidos.push(temporal)

    def toFile(self):
        archivo1 = open("Laboratorio6/usuariospendientes.txt","w")
        i = self._registro.size()
        while i > 0:
            usuario = self._registro.dequeue()
            archivo1.write(f"{usuario.getNombre()} {usuario.getId()}\n" )
            i -= 1
        archivo1.close()

        archivo2 = open("Laboratorio6/usuariosatendidos.txt","w")
        i = self._usuarioAtendidos.size()
        while i > 0:
            usuario = self._usuarioAtendidos.pop()
            archivo2.write(f"{usuario.getNombre()} {usuario.getId()}\n" )
            i -= 1
        archivo2.close()

if __name__ == "__main__":
    turnoUsuario = TurnoUsuario()
    usuario1 = Usuario("Alberto-Guzman","1252535343",Fecha(1,3,2000),"Envigado",3454434,"aguzman@unal.edu.co",Direccion("kr74","Medellin","4T-35","Boston"))
    usuario2 = Usuario("Marta-Gonzales","3345345535",Fecha(31,12,1985),"Medellin",2536378,"mgonzales@unal.edu.co",Direccion("cll65","Medellin","3-29","Robledo","Balcones-de-la-Quinta","405"))
    usuario3 = Usuario("Alizon-Peña","2342342343",Fecha(23,1,2024),"Guatape",3674685,"apeña@unal.edu.co",Direccion("tr45","Medellin","4S-73","Poblado"))
    usuario4 = Usuario("Alfredo-Ospina","3735737263",Fecha(15,7,2015),"Rionegro",3213105,"aospina@unal.edu.co",Direccion("kr23","Envigado","8-10","SanJuan","Mirador","503"))
    usuario5 = Usuario("Susana-Duque","3645274482",Fecha(4,8,2006),"El Carmen de Viboral",3750024,"sduque@unal.edu.co",Direccion("cll5","Medellin","4S-69", "Poblado","UrbColina", "1023"))
    turnoUsuario._registro.enqueue(usuario1)
    turnoUsuario._registro.enqueue(usuario2)
    turnoUsuario._registro.enqueue(usuario3)
    turnoUsuario._registro.enqueue(usuario4)
    turnoUsuario._registro.enqueue(usuario5)
    turnoUsuario.atenderSiguiente()
    turnoUsuario.atenderSiguiente()
    turnoUsuario.toFile()


    
