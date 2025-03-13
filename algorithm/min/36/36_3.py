import heapq


def go(num):
    heap = [(0, num)]
    result = [21e8] * (n + 1)
    result[num] = 0
    while heap:
        ky_cost, ky = heapq.heappop(heap)
        for do, do_cost in arr[ky]:
            baro = result[do]
            new = ky_cost + do_cost
            if baro > new:
                result[do] = new
                heapq.heappush(heap, (new, do))
    return result[p]


def back():
    heap = [(0, p)]
    result = [21e8] * (n + 1)
    result[p] = 0
    while heap:
        ky_cost, ky = heapq.heappop(heap)
        for do, do_cost in arr[ky]:
            baro = result[do]
            new = ky_cost + do_cost
            if baro > new:
                result[do] = new
                heapq.heappush(heap, (new, do))
    return result


n, m, p = map(int, input().split())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
ret=back()
for i in range(1, n + 1):
    if i == p: continue
    ret[i] += go(i)
ret[0]=0
print(max(ret))
