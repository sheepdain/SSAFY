from collections import deque


def check(y, x, num):
    if num == 1:
        k = 2 # 3칸 떨어졌다고 했는데 2칸이 맞음
    else:
        k = 3 # 4칸 떨어졌다고 했는데 3칸이 맞음
    for i in range(4):
        dy = y + directy[i] * k
        dx = x + directx[i] * k
        if 0 <= dy < 7 and 0 <= dx < 7:
            if arr[dy][dx] == num:
                return 0
    return 1


arr = [list(map(int, input())) for _ in range(7)]
directy = [0, 0, -1, 1]
directx = [1, -1, 0, 0]
flag = 1
for i in range(7):
    for j in range(7):
        if arr[i][j] != 0:
            flag = check(i, j, arr[i][j])
        if flag == 0: break
    if flag == 0: break
if flag == 1:
    print('pass')
else:
    print('fail')
