import heapq


class h:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        return ord(self.a) > ord(other.a)


MaxHeap = list(input())
MaxHeap = list(map(lambda x: h(x), MaxHeap))
heapq.heapify(MaxHeap)
for i in range(len(MaxHeap)):
    print(heapq.heappop(MaxHeap).a, end='')
