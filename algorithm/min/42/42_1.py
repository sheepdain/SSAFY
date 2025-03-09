def dfs(level, start):
    if level == 3:
        print(*path, sep='')
        return

    for i in range(start, len(n)):
        path[level] = n[i]
        dfs(level + 1, i)
        path[level] = ''


n = input()
path = [''] * 3
dfs(0, 0)
