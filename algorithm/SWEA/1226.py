import sys

sys.stdin = open('input.txt', 'r')

from collections import deque

T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    arr = []
    st = []
    for i in range(16):
        arr.append(list(map(int, input())))
        if len(st) == 0:
            for j in range(16):
                if arr[i][j] == 2:
                    st = [i, j]
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    q = deque()
    q.append((st[0], st[1]))
    ret = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy < 1 or dx < 1 or dy >= 14 or dx >= 14: continue
            if arr[dy][dx] == 1: continue
            if arr[dy][dx] == 3:
                ret = 1
                break
            arr[dy][dx] = 1
            q.append((dy, dx))
        if ret:
            break

    print(f'#{tc}', ret)
