import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort(reverse=True)
    ret = 0
    for i in range(n):
        if t:
            if t[0] >= w[i]:
                ret += w[i]
                t.pop(0)
        else:
            break
    print(f'#{tc}', ret)
