from heap import HEAP
import random
class PriorityQueu(HEAP):

    def __init__(self,capacidad):
        super().__init__(capacidad)

    def MAX_HEAP_INSERT(self, k):
            self._tamaño += 1
            i = self._tamaño - 1
            self._A.append(k)
            while i > 0 and self._A[self.parent(i)] < self._A[i]:
                temp = self._A[self.parent(i)]
                self._A[self.parent(i)] = self._A[i]
                self._A[i] = temp
                i = self.parent(i)

    def HEAP_EXTRACT_MAX(self):
        if self._tamaño == 1:
            self._tamaño -= 1
            return self._A.pop()
        else:
            max = self._A[0]
            ultimo = self._A.pop()
            self._A.pop(0)
            self._A.insert(0,ultimo)
            self._tamaño -= 1
            self.max_heapify(0)
            return max
    
    def HEAP_MAXIMUM(self):
        return self._A[0]

if __name__ == "__main__":
    
    print("MAX-HEAP-INSERT:\n")
    priorityQueu = PriorityQueu(5)
    A1 = random.sample(range(100),5)
    print(A1)
    for i in A1:
        priorityQueu.MAX_HEAP_INSERT(i)
    print(priorityQueu.getA())
    print("__________________________________________________________________________________________________________________________\n")
    print("HEAP_EXTRACT_MAX:\n")

    while priorityQueu._tamaño > 0:
        print(priorityQueu.HEAP_EXTRACT_MAX(),end=" ")
        


    """
    priorityQueu2 = PriorityQueu(5)
    A2 = random.sample(range(100),5)
    #print(A2)
    priorityQueu2.build_max_heap(A2)
    #print(priorityQueu2.getA())
    #print(priorityQueu2.HEAP_EXTRACT_MAX())
    #print(priorityQueu2.getA())
    #print("__________________________________________________________________________________________________________________________\n")
    #print("HEAP-MAXIMUM:\n")
    priorityQueu3 = PriorityQueu(5)
    A3 = random.sample(range(100),5)
    #print(A3)
    priorityQueu3.build_max_heap(A3)
    #print(priorityQueu3.getA())
    #print(priorityQueu3.HEAP_MAXIMUM())
    
"""
    
