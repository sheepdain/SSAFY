n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])
ed = 0
cnt = 0
for i in arr:
    if i[0] >= ed:
        ed = i[1]
        cnt += 1
print(cnt)
