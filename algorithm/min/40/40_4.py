arr = [list(map(int, input().split())) for _ in range(7)]
direct = [(-1, -1), (-1, 0), (-1, 1)]
for i in range(1, 7):
    for j in range(3):
        if arr[i][j] == 0: continue
        sub = []
        for dr in direct:
            dy = i + dr[0]
            dx = j + dr[1]
            if dy < 0 or dx < 0 or dy >= 7 or dx >= 3 or arr[dy][dx] == 0: continue
            sub.append(arr[dy][dx])
        if sub:
            arr[i][j] += max(sub)
        else:
            arr[i][j] = -21e8
ret = []
for k in range(3):
    if arr[6][k] != 0:
        ret.append(arr[6][k])
print(max(ret))
