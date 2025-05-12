import heapq

n, k = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jewels.sort()
bags.sort()
ret = 0
hq = []
i = 0

for bag in bags:
    while i < n and jewels[i][0] <= bag:
        heapq.heappush(hq, -jewels[i][1])
        i += 1
    if hq:
        ret += -heapq.heappop(hq)
print(ret)
