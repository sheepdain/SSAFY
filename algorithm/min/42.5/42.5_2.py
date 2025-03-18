from copy import deepcopy


def bomb(num, cnt):
    global pang, ret, visited

    if num == n:
        if pang < cnt:
            pang = cnt
            ret = path[:]
        return

    for y, x in yx:
        if visited[y][x]: continue
        remember = deepcopy(visited)
        path[num] = arr[y][x]
        k = 0
        for dr in direct:
            dy = y + dr[0]
            dx = x + dr[1]
            if dy < 0 or dx < 0 or dy >= 4 or dx >= 4 or arr[dy][dx] == '_' or visited[dy][dx]: continue
            visited[dy][dx] = True
            k += 1
        bomb(num + 1, cnt + k)
        visited = remember


yx = []
arr = []
for i in range(4):
    arr.append(list(input()))
    for j in range(4):
        if arr[i][j] != '_':
            yx.append((i, j))
n = int(input())
visited = [[False for _ in range(4)] for _ in range(4)]
direct = [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]
path = [''] * n
pang = 0
ret = []
bomb(0, 0)
ret.sort()
print(*ret)
