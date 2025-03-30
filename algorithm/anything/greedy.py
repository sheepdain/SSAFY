n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
arr.sort()
ret=0
st=0
ed=0
for i in range(n):
    if arr[i][0]>=ed:
        ed=arr[i][1]
        ret+=1
print(ret)