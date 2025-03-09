from collections import deque


def bfs(y, x):
    q = deque()
    q.append((y, x))
    while q:
        yy, xx = q.popleft()
        for i in range(4):
            dy = yy + directy[i]
            dx = xx + directx[i]
            if dy < 0 or dx < 0 or dy >= n or dx >= m: continue
            if arr[dy][dx] == 0: continue
            arr[dy][dx] = 0
            q.append((dy, dx))


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
directy = [0, 0, -1, 1]
directx = [1, -1, 0, 0]
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            bfs(i, j)
            cnt += 1
print(cnt)
