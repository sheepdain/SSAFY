import heapq


def dij(st):
    heap = [(0, st)]
    result = [21e8] * (p + 1)
    result[st] = 0
    while heap:
        ky_cost, ky = heapq.heappop(heap)
        for do, do_cost in arr[ky]:
            baro = result[do]
            new = ky_cost + do_cost
            if new < baro:
                result[do] = new
                heapq.heappush(heap, (new, do))
    return result


c, p, k, a, b = map(int, input().split())
arr = [[] for _ in range(p + 1)]
for _ in range(c):
    s, e, d = map(int, input().split())
    arr[s].append((e, d))
    arr[e].append((s, d))
go = dij(k)
A = dij(a)
B = dij(b)
ret = min((go[a] + A[b]), (go[b] + B[a]))
print(ret)
