from direccion import Direccion
from fecha import Fecha
from usuario import Usuario

if __name__ == "__main__":
    miFechaNacimiento = Fecha(4 , 1 , 2006)
    miDireccion = Direccion()
    miDireccion.setCalle("Transversal 40 A Sur")
    miDireccion.setNomenclatura("# 63 - 105")
    miDireccion.setBarrio("Barrio pradito")
    miDireccion.setApto("Apt 312")
    miDireccion.setCiudad("Medellín")
    miDireccion.setEdificio("Ciudadela Prado Etapa 2 Torre 5")
    misDatos = Usuario("Andrés Pérez Cano",1035973301)
    misDatos.setDir(miDireccion)
    misDatos.setCiudad_nacimiento("Itagüi")
    misDatos.setFecha_nacimiento(miFechaNacimiento)
    misDatos.setEmail("aperezcan@unal.edu.co")
    misDatos.setTel(2863382)
    print(f"{miFechaNacimiento.getDia():02d}-{miFechaNacimiento.getMes():02d}-{miFechaNacimiento.getA()}")
    print("__________________________________________________________________________________________________________________________")
    print(miDireccion)
    print("__________________________________________________________________________________________________________________________")
    print(misDatos)