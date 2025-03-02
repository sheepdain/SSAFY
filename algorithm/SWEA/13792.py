def Tile(n):
    t = n // 10
    tile = [0] * (t + 1)
    tile[1] = 1
    tile[2] = 3
    if t >= 3:
        for i in range(3, t + 1):
            tile[i] = tile[i - 1] + 2 * tile[i - 2]
    return tile[t]

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    ret = Tile(n)
    print(f'#{test_case}',ret)