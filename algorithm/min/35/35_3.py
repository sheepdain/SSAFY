n = int(input())
arr = []
time = {}
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        time[arr[i][j]] = (i, j)
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 1
ret = 0
while cnt <= n * n:
    y, x = time[cnt]
    if arr[y][x] == 0:
        cnt += 1
        continue
    arr[y][x] = 0
    for dr in direct:
        dy = y + dr[0]
        dx = x + dr[1]
        if dy < 0 or dx < 0 or dy >= n or dx >= n or arr[dy][dx] == 0: continue
        arr[dy][dx] = 0
    ret = cnt
    cnt += 1
print(f'{ret}초')
