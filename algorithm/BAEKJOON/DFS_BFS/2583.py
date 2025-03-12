import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def bfs(y, x):
    global arr, ret
    num = 1
    q.append((y, x))
    arr[y][x] = 1
    while q:
        yy, xx = q.popleft()
        for dr in direct:
            dy = yy + dr[0]
            dx = xx + dr[1]
            if dy < 0 or dx < 0 or dy >= m or dx >= n: continue
            if arr[dy][dx] == 1: continue
            arr[dy][dx] = 1
            num += 1
            q.append((dy, dx))
    ret.append(num)


m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
for sq in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque()
cnt = 0
ret = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            cnt += 1
            bfs(i, j)
ret.sort()
print(cnt)
print(*ret)
