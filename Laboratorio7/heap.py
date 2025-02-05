import random
class HEAP:
     
    def __init__(self, capacidad):
        self._A = []
        self._size = capacidad

    def size(self):
        return len(self._A)

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
        if r < self._size and self._A[r] > self._A[largest]:
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
            self._size -= 1
            self.max_heapify(0)
        self._size = heap_size
        self._A += tempL

        


    def getA(self):
        return self._A
    
    def setA(self,A):
        self._A = A

if __name__ == "__main__":
    heap1 = HEAP(14)
    A = [-3,4,5,23,53,65,95,96,97,98,99,34,11,70]
    #[16,4,10,14,7,9,3,2,8,1]
    #print(A)
    heap1.setA(A)
    heap1.max_heapify(1)
    #print(heap1.getA())
    heap100 = HEAP(9)
    A100 = random.sample(range(16),9)
    #print(A100)
    heap100.setA(A100)
    heap100.max_heapify(1)
    
    #print(heap100.getA())
    #heap100 = HEAP(20)
    #A100 = [random.randint(-100,100) for _ in range(20)]}
    #A100 = random.sample(range(100),20)
    #print(A100)
    #heap100.setA(A100)
    #heap100.max_heapify(2)
    #print(heap100.getA())
    
    print("build-max-heap:\n")
    heap2 = HEAP(20)
    A = random.sample(range(-100,100),20)
    print(A)
    heap2.build_max_heap(A)
    print(heap2.getA())
    print("__________________________________________________________________________________________________________________________\n")
    print("heap-sort:\n")
    print(A)
    heap2.heap_sort()
    print(heap2.getA())

