def dfs(node, cnt):
    global ret
    if node == B:
        ret = cnt
        return

    for i in arr[node]:
        if visited[i]: continue
        visited[i] = True
        dfs(i, cnt + 1)


n = int(input())
arr = [[] for _ in range(n + 1)]
A, B = map(int, input().split())
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [False for _ in range(n + 1)]
ret = -1
dfs(A, 0)
print(ret)
