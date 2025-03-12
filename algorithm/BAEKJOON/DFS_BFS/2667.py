from collections import deque


def bfs(y, x):
    global arr, ret

    q = deque()
    q.append((y, x))
    arr[y][x] = 0
    cnt = 0

    while q:
        yy, xx = q.popleft()
        cnt += 1
        for i in range(4):
            dy = yy + directy[i]
            dx = xx + directx[i]
            if 0 <= dy < n and 0 <= dx < n:
                if arr[dy][dx] == 0: continue
                q.append((dy, dx))
                arr[dy][dx] = 0
    return cnt


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
ret = []
ans = 0
directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            ans += 1
            ret.append(bfs(i, j))
ret.sort()
print(ans)
for i in ret:
    print(i)
