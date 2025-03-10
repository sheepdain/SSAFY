import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1]:
                cnt += 1
            elif arr[i][0] < arr[j][0] and arr[i][1] > arr[j][1]:
                cnt += 1
    print(f'#{tc}', cnt)
