import random
import math

class Ordenador:

    def __init__(self, capacidad):
        self._A = []
        self._capacidad = capacidad

    def inicializar(self):
        indice = self._capacidad
        while indice > 0:
            numero = random.randint(-5000,5000)
            self._A.append(numero)
            indice -= 1
    
    def  ordenar_burbuja(self):
        n = self._capacidad
        for i in range(n):
            for j in range(1,n):
                if self._A[j-1] > self._A[j]:
                    self.intercambiar(j-1,j)
    
    def intercambiar(self,primero,segundo):
        valor1 = self._A[primero]
        valor2 = self._A[segundo]
        self._A[primero] = valor2
        self._A[segundo] = valor1
    
    def ordenar_seleccion(self):
        n = self._capacidad
        for i in range(n):
            minimo = i
            for j in range(i+1,n):
                if self._A[j] < self._A[minimo]:
                    minimo = j
            self.intercambiar(i,minimo)
    
    def ordenar_insercion(self):
        n = self._capacidad
        for i in range(1,n):
            temporal = self._A[i]
            j = i
            while (j > 0 and self._A[j-1] > temporal):
                self._A[j] = self._A[j-1]
                j -= 1
            self._A[j] = temporal
      
    def ordenar_mergeSort(self,A):
        if len(A) < 2:
            return A
        else:
            q = len(A) // 2
            L = self.ordenar_mergeSort(A[:q])
            R = self.ordenar_mergeSort(A[q:])
            self._A = self.merge(L,R)
            return self.merge(L,R)

    def merge(self,arr1,arr2):
        resultado = []
        i,j = 0,0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                resultado.append(arr1[i])
                i += 1
            else:
                resultado.append(arr2[j])
                j += 1
        
        if i == len(arr1):
            for k in range(j, len(arr2)):
                resultado.append(arr2[k])
            
        elif j == len(arr2):
            for k in range(i, len(arr1)):
                resultado.append(arr1[k])
            
        return resultado
    
    def mostrar(self):
        print(self._A)
    
    def busqueda_binaria(self,x,izquierda,derecha):
        if izquierda > derecha:
            return -1
        
        else:
            medio = (izquierda + derecha) // 2
            if x < self._A[medio]:
                return self.busqueda_binaria(x,izquierda,medio - 1)
            elif x > self._A[medio]:
                return self.busqueda_binaria(x,medio + 1, derecha)
            else:
                return medio

if __name__ == "__main__":
    ordenador = Ordenador(10)
    ordenador.inicializar()
    ordenador.mostrar()
    #ordenador.ordenar_burbuja()
    #ordenador.ordenar_seleccion()
    #ordenador.ordenar_seleccion()
    #ordenador.ordenar_mergeSort(ordenador._A)
    ordenador.mostrar()
    numero = int(input("Ingrese un numero: "))
    print(ordenador.busqueda_binaria(numero,0,ordenador._capacidad-1))
