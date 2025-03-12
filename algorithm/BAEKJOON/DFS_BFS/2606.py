def dfs(node):
    global ret
    for i in arr[node]:
        if visited[i] == 1: continue
        visited[i] = 1
        dfs(i)
        ret += 1


n = int(input())
arr = [[] for _ in range(n + 1)]
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0] * (n + 1)
visited[1] = 1
ret = 0
dfs(1)
print(ret)
