def dfs(level, SUM):
    global ret

    if ret < SUM:
        return

    if level == n:
        if ret > SUM:
            ret = SUM
        return

    for i in range(n):
        if visited[i]: continue
        visited[i] = True
        dfs(level + 1, SUM + arr[level][i])
        visited[i] = False


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False for _ in range(n)]
    ret = 21e8
    dfs(0,0)
    print(f'#{tc}',ret)