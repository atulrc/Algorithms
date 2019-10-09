from heapq import heappush, heappop

def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
        out = [heappop(h) for i in range(len(h))]
        print(out)

if __name__ == '__main__':
    inp = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    heapsort(inp)
