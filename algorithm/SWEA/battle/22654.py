T=int(input())
for tc in range(1,T+1):
    n=int(input())
    X_x, X_y=-1,-1
    field=[]
    for i in range(n):
        field.append(list(input()))
        if X_x==-1: 
            for j in range(n):
                if field[i][j]=='X':
                    X_x, X_y=j,i

    q=int(input())
    d=[(-1,0),(0,1),(1,0),(0,-1)]
    run_list=[]
    for r in range(q):
        y,x=X_y,X_x
        X_d=0
        commend=list(input().split())
        for c in range(int(commend[0])):
            if commend[1][c]=='A':
                dy=y+d[X_d][0]
                dx=x+d[X_d][1]
                if dy<0 or dx<0 or dy>=n or dx>=n: continue
                if field[dy][dx]=="T": continue
                y, x=dy,dx
            elif commend[1][c]=='R':
                X_d=(X_d+1)%4
            elif commend[1][c]=='L':
                X_d=(X_d-1)%4
        if field[y][x]=="Y":
            run_list.append(1)
        else:
            run_list.append(0)
    print(f'#{tc}', *run_list)