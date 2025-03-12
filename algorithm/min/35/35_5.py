import heapq


def ugly_numbers(arr):
    heap = []
    heapq.heappush(heap, 1)
    visited = set()
    visited.add(1)
    ugly = []

    while len(ugly) < max(arr):
        num = heapq.heappop(heap)
        ugly.append(num)

        for i in [2, 3, 5]:
            new_num = num * i
            if new_num not in visited:
                heapq.heappush(heap, new_num)
                visited.add(new_num)

    return ugly


Q = int(input())
k = list(map(int, input().split()))

ugly_list = ugly_numbers(k)

for i in range(Q):
    print(ugly_list[k[i] - 1], end=' ')
