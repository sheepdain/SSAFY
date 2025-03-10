n=int(input())
player=[]
for i in range(n):
    player.append(list(input().split()))
    player.sort(key=lambda x:(int(x[1]),x),reverse=True)
    cnt=0
    for j in player:
        if cnt==3:
            break
        print(j[0],end=' ')
        cnt+=1
    print()
