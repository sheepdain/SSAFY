from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
acc = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    acc[b] += 1

q = deque()
for i in range(1, n + 1):
    if acc[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    print(now, end=' ')
    for i in arr[now]:
        if acc[i] == 1:
            acc[i] = 0
            q.append(i)
        else:
            acc[i] -= 1