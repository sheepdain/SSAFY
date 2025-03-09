def dfs(level):
    if level == 3:
        print(*path, sep='')
        return

    for i in range(3):
        if used[i] == 1: continue
        used[i] = 1
        path[level] = lst[i]
        dfs(level + 1)
        used[i] = 0


lst = input().split()
used = [0] * 3
path = [''] * 3
dfs(0)
