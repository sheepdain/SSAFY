import heapq

n = int(input())
arr = []
cost = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(i + 1, n):
        if arr[i][j] == -1: continue
        heapq.heappush(cost, (arr[i][j], i, j))
for i in range(10):
    cost_num = heapq.heappop(cost)
    heapq.heappush(cost, (cost_num[0] * 2, cost_num[1], cost_num[2]))
    if i == 9:
        print(cost_num[0] * 2, '만원', sep='')
