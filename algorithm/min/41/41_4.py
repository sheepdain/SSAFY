def dfs(level, SUM):
    global cnt

    if SUM > 7:
        return

    if level == n:
        if SUM == 7:
            cnt += 1
        return

    for i in range(10):
        dfs(level + 1, SUM + i)


n = int(input())
cnt = 0
dfs(0, 0)
print(cnt)
