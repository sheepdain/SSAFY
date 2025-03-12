import sys

sys.stdin = open('input.txt', 'r')


def bfs(y, x):
    q = [(y, x)]
    arr[y][x] = 0
    while q:
        yy, xx = q.pop(0)
        for dr in direct:
            dy = yy + dr[0]
            dx = xx + dr[1]
            if dy < 0 or dx < 0 or dy >= n or dx >= m: continue
            if arr[dy][dx] == 1:
                q.append((dy, dx))
                arr[dy][dx] = 0


T = int(input())
for tc in range(1, T + 1):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for i in range(k):
        X, Y = map(int, input().split())
        arr[Y][X] = 1
    cnt = 0
    direct = ((0, -1), (0, 1), (-1, 0), (1, 0))
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
                bfs(i, j)
    print(cnt)
