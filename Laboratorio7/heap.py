import random
class HEAP:
     
    def __init__(self, capacidad):
        self._A = []
        self._size = capacidad
        self._tamaño = 0

    def size(self):
        return self._tamaño

    def parent(self,i):
        return int(-(-(i/2)//1) - 1)
    
    def left(self,𝑖):
       return 2*i+1
    
    def right(self,𝑖):
        return 2*𝑖+2

    def max_heapify(self,i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l < self.size() and self._A[l] > self._A[i]:
            largest = l
        #else:
            #largest = i
        if r < self.size() and self._A[r] > self._A[largest]:
            largest = r
        if largest != i:
            temp = self._A[i]
            self._A[i] = self._A[largest]
            self._A[largest] = temp
            self.max_heapify(largest)
    
    def build_max_heap(self,A):
        self.setA(A)
        indice = int((len(self._A)/2) -1 )
        while indice > -1:
            self.max_heapify(indice)
            indice -= 1
    
    def heap_sort(self):
        self.build_max_heap(self._A)
        heap_size = len(self._A)
        indice = len(self._A)
        tempL = []
        while indice - 1 > 0:
            indice -= 1
            temp = self._A[indice]
            self._A[indice] = self._A[0]
            self._A[0] = temp
            tempL.insert(0,self._A.pop())
            self._tamaño -= 1
            self.max_heapify(0)
        self._A += tempL

        


    def getA(self):
        return self._A
    
    def setA(self,A):
        self._tamaño = len(A)
        self._A = A

if __name__ == "__main__":
    #print("max-heapify:\n")
    heap1 = HEAP(5)
    A1 = random.sample(range(100),5)
    heap1.setA(A1)
    #print(A1)
    heap1.max_heapify(0)
   # print(heap1.getA())
    #print("__________________________________________________________________________________________________________________________\n")
    print("build-max-heap:\n")
    heap2 = HEAP(5)
    A2 = random.sample(range(100),5)
    print(A2)
    heap2.build_max_heap(A2)
    print(heap2.getA())
    print("__________________________________________________________________________________________________________________________\n")
    print("heap-sort:\n")
    heap3 = HEAP(5)
    A3 = random.sample(range(100),5)
    heap3.setA(A3)
    #print(A3)
    heap3.heap_sort()
    print(heap3.getA())
