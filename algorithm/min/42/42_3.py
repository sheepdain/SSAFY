def dfs(cnt, ans):
    global ret

    if ans == a:
        ret = min(ret, cnt)
        return

    if len(ans) >= len(a):
        return

    for i in lst_str:
        dfs(cnt + 1, ans + i)


lst_str = ['BTS', 'SBS', 'BS', 'CBS', 'SES']
path = ''
ret = 10
a = input()
dfs(0, '')
print(ret)
