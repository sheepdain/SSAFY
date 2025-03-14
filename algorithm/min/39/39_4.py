n = int(input())
arr = list(map(int, input().split()))
arr.sort()
block = 100
cnt = 0
for i in arr:
    block -= i
    if block < 0: break
    cnt += 1
print(cnt)
