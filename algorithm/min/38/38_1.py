from collections import deque

S = int(input())
D = int(input())

q = deque()
q.append((S, 0))

visited = [0] * 100001
visited[S] = 1

while q:
    num, cnt = q.popleft()

    if num == D:
        print(cnt)
        break

    next_channels = [num // 2, num * 2, num + 1, num - 1]

    for next_num in next_channels:
        if 0 <= next_num <= 100000:
            if visited[next_num] == 1: continue
            visited[next_num] = 1
            q.append((next_num, cnt + 1))
