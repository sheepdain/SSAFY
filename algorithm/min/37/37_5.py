from collections import deque


def bfs(level):
    while q:
        y, x, num = q.popleft()
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if 0 <= dy < 4 and 0 <= dx < 4:
                if arr[dy][dx] == 1: continue
                if dy == y2 and dx == x2:
                    return num + 1
                arr[dy][dx] = 1
                q.append((dy, dx, num + 1))


arr = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 1, 0],
]
y1, x1 = map(int, input().split())
y2, x2 = map(int, input().split())
directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]
q = deque()
q.append((y1, x1, 0))
arr[y1][y2] = 1
ret = bfs(0)
print(f'{ret}회')
