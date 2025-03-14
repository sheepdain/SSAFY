import heapq

Y, X = map(int, input().split())
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = [[21e8] * n for _ in range(n)]
result[Y][X] = arr[Y][X]
heap = [(arr[Y][X], Y, X)]
while heap:
    KY_piro, KY_y, KY_x = heapq.heappop(heap)
    for dr in direct:
        dy = KY_y + dr[0]
        dx = KY_x + dr[1]
        if dy < 0 or dx < 0 or dy >= n or dx >= n or arr[dy][dx] == -1: continue
        baro = result[dy][dx]
        new = KY_piro + arr[dy][dx]
        if new < baro:
            result[dy][dx] = new
            heapq.heappush(heap, (new, dy, dx))
ret = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == -1: continue
        if result[i][j] > ret:
            ret = result[i][j]
print(ret)
