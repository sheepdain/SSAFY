from collections import deque

arr = []
q = deque()
for i in range(4):
    arr.append(list(map(int, input().split())))
    for j in range(5):
        if arr[i][j] == 1:
            q.append((i, j, 0))
directy = [-1, -1, -1, 0, 0, 1, 1, 1]
directx = [-1, 0, 1, -1, 1, -1, 0, 1]
ret = 0
while q:
    y, x, sec = q.popleft()
    for i in range(8):
        dy = directy[i] + y
        dx = directx[i] + x
        if 0 <= dy < 4 and 0 <= dx < 5:
            if arr[dy][dx] != 0: continue
            arr[dy][dx] = sec + 1
            q.append((dy, dx, sec + 1))
            if ret < sec + 1:
                ret = sec + 1
print(ret)
