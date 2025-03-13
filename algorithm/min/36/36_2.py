import heapq


def cost():
    heap = [(0, A)]
    result = [21e8] * (n + 1)
    result[A] = 0
    while heap:
        ky_cost, ky = heapq.heappop(heap)
        for do, do_cost in arr[ky]:
            baro = result[do]
            new = ky_cost + do_cost
            if baro > new:
                result[do] = new
                heapq.heappush(heap, (new, do))
    print(result[B])


n, m, k = map(int, input().split())
arr = [[] for _ in range(n + 1)]
A, B = map(int, input().split())
for _ in range(m):
    f, t, c = map(int, input().split())
    arr[f].append([t, c])
    arr[t].append([f, c])
cost()
for _ in range(k):
    up = int(input())
    for i in arr:
        for j in i:
            j[1] += up
    cost()
