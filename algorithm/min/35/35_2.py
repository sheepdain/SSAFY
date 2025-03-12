import heapq

n = int(input())
arr = []
cost = {}
hp = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] != 0:
            num = arr[i][j]
            heapq.heappush(hp, -num)
            cost[num] = f'{chr(i + 65)}-{chr(j + 65)}'
for i in range(3):
    num = -heapq.heappop(hp)
    print(cost[num], num)
