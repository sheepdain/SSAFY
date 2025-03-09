from collections import deque

n = int(input())
y1, x1, y2, x2 = map(int, input().split())
arr = [[0] * n for _ in range(n)]
directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]
arr[y1][x1], arr[y2][x2] = 1, 1
q = deque()
q.append((y1, x1, 1))
q.append((y2, x2, 1))
while q:
    y, x, num = q.popleft()
    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        if 0 <= dy < n and 0 <= dx < n:
            if arr[dy][dx] != 0: continue
            arr[dy][dx] = num + 1
            q.append((dy, dx, num + 1))
for i in range(n):
    print(*arr[i], sep='')
