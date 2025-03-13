import sys

sys.stdin = open('input.txt', 'r')


def dfs(level, node, cnt):
    global ret
    if level == n - 1:
        cnt += arr[node][0]
        if ret > cnt:
            ret = cnt
        return

    for i in range(1, n):
        if visited[i]: continue
        visited[i] = True
        dfs(level + 1, i, cnt + arr[node][i])
        visited[i] = False


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False for _ in range(n)]
    ret = 21e8
    dfs(0, 0, 0)
    print(f'#{tc}', ret)
