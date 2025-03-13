import sys

sys.setrecursionlimit(10 ** 7)


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
# 위 아래 차이가 뭐지?
def dfs(t):
    global cnt
    visited[t] = cnt
    line[t].sort()
    for i in line[t]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

import sys
sys.setrecursionlimit(150000)
N, M, R = map(int, sys.stdin.readline().split())
line = [[] for _ in range(N+1)]
visited = [0]*(N+1)  # 저장값
cnt = 1
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    line[a].append(b)  # 양 방향 간선
    line[b].append(a)  # 양 방향 간선
dfs(R)
for i in range(1, N+1):
    print(visited[i])
