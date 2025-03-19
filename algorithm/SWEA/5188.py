import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    direct = [(-1, 0), (0, -1)]
    for i in range(n):
        for j in range(n):
            ret = []
            for dr in direct:
                dy = i + dr[0]
                dx = j + dr[1]
                if dy < 0 or dx < 0 or dy >= n or dx >= n: continue
                ret.append(arr[dy][dx])
            if ret:
                arr[i][j] += min(ret)
    print(f'#{tc}', arr[-1][-1])
