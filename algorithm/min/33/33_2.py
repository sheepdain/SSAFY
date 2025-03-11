def find(member):
    global arr
    if arr[ord(member) - 65] == 0:
        return member
    ret = find(arr[ord(member) - 65])
    arr[ord(member) - 65] = ret
    return ret


def union(a, b):
    global arr, cnt
    bossa, bossb = find(a), find(b)
    if bossa != bossb:
        arr[ord(bossb) - 65] = bossa
        cnt -= 1


arr = [0, 'A', 'A', 0, 'D', 'D', 0, 'G', 0, 'I']
cnt = 4
n = int(input())
for i in range(n):
    A, B = input().split()
    union(A, B)
print(f'{cnt}개')
