from collections import deque


def bfs(y, x, num):
    global MAX, MAX_cnt
    q = deque()
    q.append((y, x))
    arr[y][x] = 0
    cnt = 1
    while q:
        yy, xx = q.popleft()
        for i in range(4):
            dy = yy + directy[i]
            dx = xx + directx[i]
            if 0 <= dy < 4 and 0 <= dx < 9:
                if arr[dy][dx] != num: continue
                arr[dy][dx] = 0
                cnt += 1
                q.append((dy, dx))
    if MAX_cnt < cnt:
        MAX_cnt = cnt
        MAX = num


arr = [list(map(int, input().split())) for _ in range(4)]
directy = [0, 0, -1, 1]
directx = [1, -1, 0, 0]
MAX = 0
MAX_cnt = 0
for i in range(4):
    for j in range(9):
        if arr[i][j] != 0:
            bfs(i, j, arr[i][j])
print(MAX * MAX_cnt)
