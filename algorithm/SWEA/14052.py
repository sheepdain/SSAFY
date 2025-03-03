import sys
sys.stdin=open('input.txt','r')

from collections import deque

T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    arr=[]
    st=[]
    for i in range(n):
        arr.append(list(map(int,input())))
        if st:continue
        for j in range(n):
            if arr[i][j]==2:
                st=[i,j]

    # arr=[list(map(int,input())) for _ in range(n)]
    # for i in range(n-1,-1,-1):
    #     if st: continue
    #     for j in range(n):
    #         if arr[i][j] == 2:
    #             st = [i, j]
    #             break
    #     if st:
    #         break

    directy=[-1,1,0,0]
    directx=[0,0,-1,1]
    # used=[[0]*n for _ in range(n)]
    q=deque()
    q.append((st[0],st[1],0))
    ret=0
    while q:
        y,x,cnt=q.popleft()
        for i in range(4):
            dy=y+directy[i]
            dx=x+directx[i]
            if dy<0 or dx<0 or dy>=n or dx>=n:continue
            if arr[dy][dx]==1:continue
            if arr[dy][dx]==3:
                ret=cnt
                break
            q.append((dy,dx,cnt+1))
            arr[dy][dx]=1
        if ret: break

    print(f'#{test_case}',ret)