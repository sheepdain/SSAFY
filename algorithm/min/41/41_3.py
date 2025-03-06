# 2000넘어가면 타임에러

def dfs(money, num):
    global cnt

    if num>cnt:
        return

    if money == 0:
        if cnt > num:
            cnt = num
        return

    for i in coin:
        if money >= i:
            dfs(money - i, num + 1)


T, n = map(int, input().split())
coin = list(map(int, input().split()))
cnt = 21e8
dfs(T, 0)
if cnt==21e8:
    print('impossible')
else:
    print(cnt)
