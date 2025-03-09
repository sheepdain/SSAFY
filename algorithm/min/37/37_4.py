from collections import deque


def bfs(y, x):
    global ret
    q = deque()
    q.append((y, x))
    arr[y][x] = 0
    cnt = 1
    while q:
        yy, xx = q.popleft()
        for i in range(4):
            dy = directy[i] + yy
            dx = directx[i] + xx
            if 0 <= dy < 4 and 0 <= dx < 4:
                if arr[dy][dx] == 1:
                    arr[dy][dx] = 0
                    cnt += 1
                    q.append((dy, dx))
    ret = max(ret, cnt)


arr = [list(map(int, input().split())) for _ in range(4)]
directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]
ret = 0
for i in range(4):
    for j in range(4):
        if arr[i][j] == 1:
            bfs(i, j)
print(ret)
