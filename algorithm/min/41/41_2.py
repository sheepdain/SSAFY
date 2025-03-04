# n=150 일 때 타임에러

def dfs(now,score):
    global ret
    if now>n:
        if ret<score:
            ret=score
        return

    for i in m:
        dfs(now+i,score+MAP[now])

n=int(input())
MAP=list(map(int,input().split()))
MAP.insert(0,0)
m=[2,7]
ret=-21e8
dfs(0,0)
print(ret)