def binaryY(st, ed):
    MAX = -1
    while 1:
        mid = (st + ed) // 2
        if '#' in arr[mid]:
            MAX = mid
            st = mid + 1
        else:
            ed = mid - 1
        if st > ed:
            break
    return MAX


def binaryX(st, ed):
    MAX = -1
    while 1:
        mid = (st + ed) // 2
        if '#' == arr[idxY][mid]:
            MAX = mid
            st = mid + 1
        else:
            ed = mid - 1
        if st > ed:
            break
    return MAX


n = int(input())
arr = [list(input()) for i in range(n)]
idxY = binaryY(0, n)
idxX = binaryX(0, n)
print(idxY, idxX)