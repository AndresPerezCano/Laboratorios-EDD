from direccion import Direccion
from fecha import Fecha
from usuario import Usuario

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    id1 = input("ingrese su id: ")
    fechaNacimiento = input("Ingrese su fecha de nacimiento(d/m/a):")
    ciudadNacimiento = input("Ingrese su ciudad de nacimiento: ")
    tel = input("Ingrese su telefono: ")
    email = input("Ingrese su email: ")
    dir1 = input("Ingrese su direccion(Ciudad/Calle/Nomenclatura/Barrio/Edificio/Apto): ")
    
    usuario = Usuario(nombre,id1)
    dia, mes, año = fechaNacimiento.split("/")
    usuario.setFecha_nacimiento(Fecha(int(dia),int(mes),int(año)))
    usuario.setCiudad_nacimiento(ciudadNacimiento)
    usuario.setTel(tel)
    usuario.setEmail(email)
    usuario.setDir(Direccion())
    if len(dir1.split("/")) == 6:
        ciudad,calle,nomenclatura,barrio,edificio,apto = dir1.split("/")
        usuario.getDir().setApto(apto)
        usuario.getDir().setEdificio(edificio)
    elif len(dir1.split("/")) == 5:
        ciudad,calle,nomenclatura,barrio,edificio = dir1.split("/")
        usuario.getDir().setEdificio(edificio)
        
    elif len(dir1.split("/")) == 4:
        ciudad,calle,nomenclatura,barrio = dir1.split("/")
    
    usuario.getDir().setCalle(calle)
    usuario.getDir().setNomenclatura(nomenclatura)
    usuario.getDir().setBarrio(barrio)
    usuario.getDir().setCiudad(ciudad)

    print(usuario)