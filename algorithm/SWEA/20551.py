import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    cnt = 0
    for j in range(2):
        for i in range(1, 3):
            while arr[i - 1] >= arr[i]:
                arr[i - 1] -= 1
                cnt += 1
            if arr[i - 1] <= 0:
                cnt = -1
                break
        if cnt == -1:
            break
    print(f'#{tc}', cnt)
