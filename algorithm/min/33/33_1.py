def findboss(member):
    if arr[ord(member)] == 0:
        return member
    ret = findboss(arr[ord(member)])
    arr[ord(member)] = ret
    return ret


def union(a, b):
    global arr
    bossa, bossb = findboss(a), findboss(b)
    if bossa == bossb:
        return 1
    arr[ord(bossb)] = bossa
    return


arr = [0] * 200

n = int(input())
for i in range(n):
    A, B = input().split()
    if union(A, B):
        print('발견')
        break
else:
    print('미발견')

n = int(input())
flag = 0
for i in range(n):
    A, B = input().split()
    flag = union(A, B)
    if flag == 1:
        break
if flag == 1:
    print('발견')
else:
    print('미발견')
