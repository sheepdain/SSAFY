import sys

sys.stdin = open('input.txt', 'r')


def probability(num, pb):
    global ret

    if num == n:
        if ret < pb * 100:
            ret = pb * 100
        return

    if ret >= pb*100: return

    for i in range(n):
        if visited[i]: continue
        visited[i] = True
        probability(num + 1, pb * (job[num][i] / 100))
        visited[i] = False


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    job = [list(map(int, input().split())) for _ in range(n)]
    visited = [False for _ in range(n)]
    ret = 0
    probability(0, 1)
    print(f'#{tc} {ret:.6f}')
