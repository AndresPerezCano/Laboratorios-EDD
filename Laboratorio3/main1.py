from direccion import Direccion
from fecha import Fecha
from usuario import Usuario
from agenda import Agenda

if __name__ == "__main__":
    print("_____________________________________________________________________________________________________________________________________")
    agenda = Agenda(5)
    agenda.imporT()
    for i in agenda.getRegistro():
        print(i)

    print("_____________________________________________________________________________________________________________________________________")
    #print(agenda.eliminar(3645274482))

    id = input("Ingrese una ID: ")
    print(agenda.eliminar(id))
    agenda.toFile("Laboratorio3/Agenda2.txt")