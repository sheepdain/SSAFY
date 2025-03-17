n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = 0
for i in range(n):
    cnt += 1
    arr[i] -= b
    if arr[i]>0:
        cnt+=arr[i]//c
        if arr[i]%c:
            cnt+=1
print(cnt)