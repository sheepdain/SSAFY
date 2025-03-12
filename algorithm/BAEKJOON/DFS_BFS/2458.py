N, M = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 0:
                if arr[i][k] == 1 and arr[k][j] == 1:
                    arr[i][j] = 1

result = 0
for i in range(1, N+1):
    sum = 0
    for j in range(1, N+1):
        sum += arr[i][j] + arr[j][i]
    if sum == N-1:
        result += 1
print(result)
# 연습하기
# def solution():
#     N, M = map(int, input().split())
#     graph = [[] for _ in range(N+1)]
#     for _ in range(M):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#     visited = [[False]*(N+1) for _ in range(N+1)]
#     for i in range(1, N+1):
#         stack = []
#         for j in graph[i]:
#             stack.append(j)
#             visited[i][j] = True
#         while stack:
#             u = stack.pop()
#             for v in graph[u]:
#                 if visited[i][v]:
#                     continue
#                 stack.append(v)
#                 visited[i][v] = True
#     res = 0
#     for i in range(1, N+1):
#         cnt = 0
#         for j in range(1, N+1):
#             cnt += visited[i][j] or visited[j][i]
#         if cnt >= N-1:
#             res += 1
#     print(res)
#
# solution()