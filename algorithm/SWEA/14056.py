import sys

sys.stdin = open('input.txt', 'r')


def inorder(now):
    global cnt
    if now > len(arr) - 1: return
    inorder(now * 2)
    arr[now] = cnt
    cnt += 1
    inorder(now * 2 + 1)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [0] * (n + 1)
    cnt = 1
    inorder(1)

    print(f'#{tc}', arr[1], arr[n // 2])
