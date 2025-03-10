n=int(input())
arr=list(map(int,input().split()))
SUM=sum(arr[:4])
for i in range(n-4):
    sub=SUM-arr[i]+arr[i+4]
    SUM=min(SUM,sub)
print(SUM)