def dfs(level, SUM):
    global MAX

    if level == n:
        if SUM % 10 == 0:
            MAX = max(MAX, SUM)
        return

    for i in range(len(buy_list)):
        if used[i] == 1: continue
        used[i] = 1
        dfs(level + 1, SUM - products[buy_list[i]])
        used[i] = 0


products = {'a': 15, 'b': 20, 'c': 44, 'd': 22, 'e': 55, 'f': 16, 'g': 45}
buy_list = list(input())
used = [0] * len(buy_list)
n = int(input())
ret = 0
MAX = 0
for i in buy_list:
    ret += products[i]
dfs(0, ret)
print(MAX)
