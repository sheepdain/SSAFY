from collections import deque


def check():
    global first

    while first:
        y, x, num = first.popleft()
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if 0 <= dy < 8 and 0 <= dx < 9:
                if arr[dy][dx] == '#':
                    print(num)
                    return
                if arr[dy][dx] == x: continue
                arr[dy][dx] = x
                first.append((dy, dx, num + 1))


arr = [list(input()) for _ in range(8)]
directy = [0, 0, -1, 1]
directx = [1, -1, 0, 0]
q = deque()
q.append((0, 8))
first = deque()
first.append((0, 8, 0))
arr[0][8] = 'x'
while q:
    y, x = q.popleft()
    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        if 0 <= dy < 8 and 0 <= dx < 9:
            if arr[dy][dx] != '#': continue
            arr[dy][dx] = 'x'
            q.append((dy, dx))
            first.append((dy, dx, 0))

check()
