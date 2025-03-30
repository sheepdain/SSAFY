n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1],x[0]))
ed=0
cnt=0
double=0
for i in range(n):
    if ed<=arr[i][0]:
        cnt += 1
        ed = arr[i][1]
print(cnt)