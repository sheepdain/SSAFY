import sys

sys.setrecursionlimit(150000) # 크기가 크면 메모리 초과 일어날 수 있음


def dfs(node):
    global cnt
    visited[node] = cnt
    arr[node].sort()
    for i in arr[node]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


n, m, r = map(int, input().split())
arr = [[] for _ in range(n + 1)]
for k in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0] * (n + 1)
cnt = 1
dfs(r)
for i in range(1, n + 1):
    print(visited[i])
