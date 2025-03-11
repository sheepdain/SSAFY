def dfs(node, y):
    global flag

    for i in range(n):
        if i == y: continue
        if arr[node][i] == 1:
            if visited[i] == 1:
                flag = 1
                return
            else:
                visited[i] = 1
                dfs(i, node)
                visited[i] = 0
    if flag == 1: return


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
flag = 0
dfs(0, 0)
if flag:
    print('cycle 발견')
else:
    print('미발견')
