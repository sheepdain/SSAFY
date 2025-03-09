def dfs(level, SUM):
    global MAX, MIN

    if level == 4:
        if MAX - 10 > SUM > MIN + 10:
            return

    if level == 5:
        if MAX < SUM:
            MAX = SUM
        elif MIN > SUM:
            MIN = SUM
        return

    for i in range(5):
        if level == 0 or level == 2:
            if used[i] == 1: continue
            used[i] = 1
            path[level] = num_lst[i]
            dfs(level + 1, SUM)
            used[i] = 0
        elif level == 1:
            if used[i] == 1: continue
            used[i] = 1
            path[level] = num_lst[i]
            dfs(level + 1, SUM + (path[0] * path[1]))
            used[i] = 0
        elif level == 3:
            if used[i] == 1: continue
            used[i] = 1
            path[level] = num_lst[i]
            dfs(level + 1, SUM - (path[2] * path[3]))
            used[i] = 0
        elif level == 4:
            if used[i] == 1: continue
            used[i] = 1
            path[level] = num_lst[i]
            dfs(level + 1, SUM + num_lst[i])
            used[i] = 0


num_lst = list(map(int, input().split()))
used = [0] * 5
path = [0] * 5
MAX = -21e8
MIN = 21e8
dfs(0, 0)
print(MAX)
print(MIN)
