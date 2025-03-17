import heapq

n = int(input())
arr = []
ret = 0
for i in range(n):
    heapq.heappush(arr, int(input()))
while len(arr) > 1:
    num = heapq.heappop(arr) + heapq.heappop(arr)
    ret += num
    heapq.heappush(arr, num)
print(ret)
