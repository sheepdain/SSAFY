n = int(input())
arr = list(input().split())
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        ret = arr[i] + arr[j]
        if ret == 'HITSMUSIC':
            cnt += 1
print(cnt)
