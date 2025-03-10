n = int(input())
arr = list(map(int, input().split()))
cnt = 1
while 1:
    ans = 0
    for i in range(1, len(arr)):
        ans += 1
        if arr[i - 1] != arr[i]:
            cnt = 1
        elif arr[i - 1] == arr[i]:
            cnt += 1
            if cnt == 3:
                for j in range(3):
                    arr.pop(i - 2)
                    cnt = 1
                break
    if ans == len(arr) - 1:
        break
arr.sort()
print(*arr)
