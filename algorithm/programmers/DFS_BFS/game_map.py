from collections import deque

def solution(maps):
    n=len(maps)
    m=len(maps[0])
    goal=(n-1,m-1)
    q=deque()
    q.append((0,0,1))
    direct=((1,0),(-1,0),(0,1),(0,-1))
    answer=1
    flag=False
    while q:
        y,x,cnt=q.popleft()
        for dr in direct:
            dy=y+dr[0]
            dx=x+dr[1]
            if dy==goal[0] and dx==goal[1]:
                answer=cnt+1
                flag=True
                break
            if dy<0 or dx<0 or dy>=n or dx>=m: continue
            if maps[dy][dx]==0: continue
            maps[dy][dx]=0
            q.append((dy,dx,cnt+1))
        if flag: break
    if answer==1:
        answer=-1
    return answer