from collections import deque


def bfs(y, x, goal):
    if int(arr[y][x]) == goal:
        return y, x, 0
    q = deque()
    q.append((y, x, 0))
    visit = [[0] * m for _ in range(n)]
    visit[y][x] = 1
    while q:
        yy, xx, cnt = q.popleft()
        for i in range(4):
            dy = yy + directy[i]
            dx = xx + directx[i]
            if 0 <= dy < n and 0 <= dx < m:
                if arr[dy][dx] == '#': continue
                if visit[dy][dx] == 1: continue
                if int(arr[dy][dx]) == goal:
                    return dy, dx, cnt + 1
                visit[dy][dx] = 1
                q.append((dy, dx, cnt + 1))


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
directy = [0, 0, -1, 1]
directx = [1, -1, 0, 0]
ret = 0
i, j, cnt = bfs(0, 0, 1)
ret += cnt
i, j, cnt = bfs(i, j, 2)
ret += cnt
i, j, cnt = bfs(i, j, 3)
ret += cnt
i, j, cnt = bfs(i, j, 4)
ret += cnt
print(f'{ret}회')
