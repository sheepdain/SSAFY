from collections import deque

arr = [list(map(int, input().split())) for _ in range(4)]
directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]
cnt = 0
q = deque()
q.append((0, 0))
while q:
    y, x = q.popleft()
    for i in range(4):
        dy = directy[i] + y
        dx = directx[i] + x
        if 0 <= dy < 4 and 0 <= dx < 6:
            if arr[dy][dx] == 1: continue
            if arr[dy][dx] == 2:
                cnt += 1
            arr[dy][dx] = 1
            q.append((dy, dx))
            if arr[dy][dx] == 2:
                cnt += 1
print(cnt)
