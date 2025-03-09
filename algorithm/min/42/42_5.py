def dfs(level, SUM):
    global ret

    if level == n:
        if SUM == 10:
            ret += 1
        return

    if SUM > 10:
        return

    for i in range(1, 10):
        dfs(level + 1, SUM + i)


n = int(input())
ret = 0
dfs(0, 0)
print(ret)
