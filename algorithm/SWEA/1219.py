import sys

sys.stdin = open('input.txt', 'r')


def dfs(node):
    global ret
    if node == 99:
        ret = 1
        return

    for i in arr[node]:
        if used == 1: continue
        dfs(i)
        if ret == 1:
            return


T = 10
for test_case in range(1, T + 1):
    tc, n = map(int, input().split())
    arr = [[] for _ in range(n)]
    lst = list(map(int, input().split()))
    for i in range(0, 2 * n, 2):
        arr[lst[i]].append(lst[i + 1])
    used = [0] * 100
    used[0] = 1
    ret = 0
    dfs(0)
    print(f'#{tc}', ret)
