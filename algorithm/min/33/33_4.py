def find(member):
    global arr
    if arr[member] == 0:
        return member
    ret = find(arr[member])
    arr[member] = ret
    return ret


def union(a, b):
    global arr
    if ord('A') <= ord(a) <= ord('F'):
        lank[int(b)] = a
        return
    elif ord('A') <= ord(b) <= ord('F'):
        lank[int(a)] = b
        return
    bossa, bossb = find(int(a)), find(int(b))
    if bossa != bossb:
        arr[bossb] = bossa


n, k = map(int, input().split())
arr = [0] * (k + 1)
lank = [''] * (k + 1)
for i in range(n):
    A, B = input().split()
    union(A, B)
for i in range(1, k + 1):
    print(lank[find(i)], end='')
