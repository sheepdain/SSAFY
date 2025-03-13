import heapq

n = int(input())
low = [-500]
high = []
for i in range(n):
    a, b = map(int, input().split())
    for i in [a, b]:
        if i > -low[0]:
            heapq.heappush(high, i)
        else:
            heapq.heappush(low, -i)
    if len(low) - 1 > len(high):
        num = -heapq.heappop(low)
        heapq.heappush(high, num)
    elif len(low) - 1 < len(high):
        num = heapq.heappop(high)
        heapq.heappush(low, -num)
    print(-low[0])
