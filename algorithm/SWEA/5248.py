import sys

sys.stdin = open('input.txt', 'r')


def find(member):
    global jo
    if jo[member] == 0:
        return member
    boss = find(jo[member])
    jo[member] = boss
    return boss


def union(a, b):
    global jo
    A, B = find(a), find(b)
    if A == B: return
    jo[B] = A


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [[] for _ in range(n + 1)]
    lst = list(map(int, input().split()))
    for i in range(0, m * 2, 2):
        arr[lst[i]].append(lst[i + 1])
    jo = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in arr[i]:
            union(i, j)
    jo_lst = []
    cnt = jo.count(0) - 1

    print(f'#{tc}', cnt)
