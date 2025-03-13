import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x: (x[1], x[0]))
    st = 0
    ed = 0
    cnt = 0
    while 1:
        for i in range(len(arr)):
            if arr[i][0] >= ed:
                cnt += 1
                ed = arr[i][1]
                break
        else:
            break
    print(f'#{tc}', cnt)
