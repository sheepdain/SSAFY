arr = [[[] for _ in range(3)] for _ in range(3)]
n = int(input())
for i in range(n):
    y, x, lst = map(int, input().split())
    arr[y][x] = [int(num) for num in str(lst)]
wind_n = int(input())
wind = list(map(int, input().split()))
for k in range(wind_n):
    s = wind[k]
    for i in range(3):
        for j in range(3):
            if arr[i][j]:
                arr[i][j][-1] -= s
                if arr[i][j][-1] <= 0:
                    arr[i][j].pop(-1)
ret = sum(len(arr[i][j]) for i in range(3) for j in range(3))
print(ret)
