import heapq

n, t = map(int, input().split())
arr = [[] for _ in range(n)]
for _ in range(t):
    a, b, w = map(int, input().split())
    arr[a].append((b, w))
st, ed = 0, n - 1
result = [21e8] * n
result[0] = 0
heap = [(0, 0)]

while heap:
    ky_cost, ky = heapq.heappop(heap)
    if result[ky] < ky_cost: continue
    for do, do_cost in arr[ky]:
        baro = result[do]
        new = ky_cost + do_cost
        if new < baro:
            result[do] = new
            heapq.heappush(heap, (new, do))
if result[ed] == 21e8:
    print('impossible')
else:
    print(result[ed])
