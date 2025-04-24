n=int(input())
arr=list(map(int,input().split()))
ret=[0]*n
for i in range(n):
    cnt=0
    for j in range(n):
        if ret[j]==0:
            if cnt==arr[i]:
                ret[j]=i+1
                break
            else:
                cnt+=1
print(*ret)
