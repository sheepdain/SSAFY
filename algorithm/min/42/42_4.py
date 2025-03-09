def dfs(cnt, money):
    global ret

    if money == n:
        ret = min(ret, cnt)
        return

    if money > n:
        return

    for i in arr:
        dfs(cnt + 1, money + i)


arr = [10, 40, 60]
n = int(input())
ret = 21e8
dfs(0, 0)
print(ret)
