from collections import deque


def bfs(sty, stx, edy, edx):
    q = deque()
    q.append((sty, stx, 0))
    used = [[0] * m for _ in range(n)]
    used[sty][stx] = 1
    while q:
        y, x, cnt = q.popleft()
        if y == edy and x == edx:
            return cnt
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if 0 <= dy < n and 0 <= dx < m:
                if arr[dy][dx] == 'x': continue
                if used[dy][dx] == 1: continue
                used[dy][dx] = 1
                q.append((dy, dx, cnt + 1))


n, m = map(int, input().split())
Sy, Sx, Cy, Cx, Dy, Dx = 0, 0, 0, 0, 0, 0
arr = []
for i in range(n):
    arr.append(list(input().split()))
    for j in range(m):
        if arr[i][j] == 'S':
            Sy, Sx = i, j
        elif arr[i][j] == 'C':
            Cy, Cx = i, j
        elif arr[i][j] == 'D':
            Dy, Dx = i, j

directy = [0, 0, -1, 1]
directx = [1, -1, 0, 0]
ret = bfs(Sy, Sx, Cy, Cx)
ret += bfs(Cy, Cx, Dy, Dx)
print(ret)
