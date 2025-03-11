from collections import deque


def dfs(node):
    print(node, end=' ')

    for i in lst[node]:
        if visited[i] == 1: continue
        visited[i] = 1
        dfs(i)


def bfs(node):
    q = deque()
    q.append(node)
    visited = [0] * (n + 1)
    visited[node] = 1
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in lst[now]:
            if visited[i] == 1: continue
            visited[i] = 1
            q.append(i)


n, m, v = map(int, input().split())
lst = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for i in range(n + 1):
    lst[i].sort()
visited = [0] * (n + 1)
visited[v] = 1
dfs(v)
print()
bfs(v)
