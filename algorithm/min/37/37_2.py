from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
y, x = map(int, input().split())
directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]
arr[y][x] = 0
q = deque()
q.append((y, x, 0))
ret = 0
while q:
    yy, xx, day = q.popleft()
    for i in range(4):
        dy = yy + directy[i]
        dx = xx + directx[i]
        if 0 <= dy < n and 0 <= dx < m:
            if arr[dy][dx] != 0: continue
            arr[dy][dx] = day + 1
            q.append((dy, dx, day + 1))
            if ret < day + 1:
                ret = day + 1
print(ret)
