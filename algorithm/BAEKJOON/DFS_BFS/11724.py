import sys

sys.stdin = open('input.txt', 'r')


def dfs(now):
    for t in arr[now]:
        if visited[t]:
            visited[t] = False
            dfs(t)


n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
visited = [True] * (n + 1)
cnt = 0
for node in range(1, n + 1):
    if visited[node]:
        visited[node] = False
        cnt += 1
        dfs(node)
print(cnt)
