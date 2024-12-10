from usuario import Usuario
from fecha import Fecha
from direccion import Direccion

class Agenda:

    def __init__(self, capacidad):
        self._registro = []
        self._no_reg = 0
        self._capacidad = capacidad
    
    def agregar(self, usuario):
        if self.buscar(usuario) != -1:
            return "Falso. No fue posible agregar nuevamente al usuario"

        else:
            if self._no_reg < self._capacidad:
                self._registro.insert(self._no_reg,usuario)
                self._no_reg += 1
                return "TRUE. Usuario agregado correctamente"
            
            else:
                return "Falso. Espacio insuficiente en el registro"

    def buscar(self, id):
        indice = 0
        for i in self._registro:
            usuario = i
            if usuario.getId() == id:
                return indice
            indice += 1
        return -1

    def eliminar(self, id):
        if self.buscar(id) == -1:
            return "FALSE"
        
        else:
            indice = self.buscar(id)
            usuario = self._registro[indice]
            for j in range(indice,self._no_reg - 1):
                self._registro[j] = self._registro[j+1]
            self._registro[-1] = None
            self._no_reg -= 1
            return "TRUE"
    
    def toFile(self,h):
        archivo = open(h,"w")
        for i in self._registro:
            usuario = i
            if usuario != None:
                archivo.write(str(usuario ) + "\n")
        archivo.close()
    
    def imporT(self):
        archivo = open("Laboratorio3/Agenda.txt","r")
        while True:
            usuario = archivo.readline()
            usuario = usuario.strip()
            if not usuario:
                break
            else:
                nombre,id,fecha_nacimiento,ciudad_nacimiento,tel,email,dir = usuario.split("/")
                dia, mes, año = fecha_nacimiento.split("-")
                ciudad,calle,nomenclatura,barrio,edificio,apto = dir.split(" ")  
                usuario1 = Usuario(nombre,id,Fecha(int(dia),int(mes),int(año)),ciudad_nacimiento,tel,email,Direccion(calle,ciudad,nomenclatura,barrio,edificio,apto))
                self.agregar(usuario1)

        archivo.close()

    def getRegistro(self):
        return self._registro
    def getNo_reg(self):
        return self._no_reg
    def getCapacidad(self):
        return self._capacidad
    def setRegistro(self,registro):
        self._registro = registro
    def setNo_reg(self,no_reg):
        self._no_reg = no_reg
    def setCapacidad(self,capacidad):
        self._capacidad = capacidad
    
    

