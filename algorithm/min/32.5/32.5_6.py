from copy import deepcopy

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sub = deepcopy(arr)
for t in range(k):
    sub = deepcopy(arr)
    for i in range(n):
        for j in range(n):
            arr[j][n - i - 1] = sub[i][j]
for i in arr:
    print(*i)
