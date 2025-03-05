import sys

sys.stdin = open('input.txt', 'r')


def inorder(now):
    global ret
    if now > n: return
    inorder(now * 2)
    ret+=arr[now]
    inorder(now * 2 + 1)


T = 10
for tc in range(1, T + 1):
    n = int(input())
    arr = [0] * (n + 1)
    for i in range(n):
        lst = list(input().split())
        arr[int(lst[0])] = lst[1]
    ret = ''
    inorder(1)
    print(f'#{tc}', ret)

