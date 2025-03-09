def dfs(y, x):
    global flag

    if y == n - 1 and x == n - 1:
        flag = 1
        return

    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        if 0 <= dy < n and 0 <= dx < n:
            if arr[dy][dx] == 1: continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            dfs(dy, dx)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
used = [[0] * n for _ in range(n)]
directy = [1, 0, 0, -1]
directx = [0, 1, -1, 0]
flag = 0
dfs(0, 0)
if flag == 0:
    print('불가능')
else:
    print('가능')
