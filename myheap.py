class Heap:

    def __init__(self):
        self.heapList = ['empty']
        self.length = 0

    def insert(self, k):
        self.heapList.append(k)
        self.length += 1
        self.bubbleUp(self.length)

    def bubbleUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i = i // 2

    def extractMin(self):
        self.heapList[1], self.heapList[self.length] = self.heapList[self.length], self.heapList[1]
        self.length -= 1
        self.bubbleDown(1)
        return self.heapList.pop()

    def bubbleDown(self,i):
        while (i * 2) <= self.length:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.length:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1



if __name__ == '__main__':
    heap = Heap()

    heap.insert(1)
    heap.insert(-2)
    heap.insert(11)
    heap.insert(-12)
    heap.insert(0)
    heap.insert(0)
    heap.insert(5)
    heap.insert(8)

    print(heap.heapList)
    for i in range (heap.length):
        print(heap.extractMin())
    print(heap.heapList)
