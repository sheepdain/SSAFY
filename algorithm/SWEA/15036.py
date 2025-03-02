import sys

sys.stdin = open('input.txt', 'r')


def dfs(node):
    global ret
    if node == G-1:
        ret = 1
        return

    for i in range(v):
        if arr[node][i] == 1:
            if used[i] == 0:
                used[i] = 1
                dfs(i)
                if ret == 1:
                    return

T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    arr = [[0] * v for _ in range(v)]
    for i in range(e):
        s, g = map(int, input().split())
        arr[s-1][g-1] = 1
    S, G = map(int, input().split())
    ret = 0
    used = [0] * v
    used[S-1] = 1
    dfs(S-1)
    print(f'#{test_case}',ret)