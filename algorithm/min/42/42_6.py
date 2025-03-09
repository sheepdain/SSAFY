n, m = map(int, input().split())
arr = list(map(int, input().split()))
ret = []
lst = []
a = min(arr)
arr.remove(a)
lst.append(a)
for i in range(m - 1):
    if a<0:
        b = max(arr)
        arr.remove(b)
        lst.append(b)
    else:
        b = min(arr)
        arr.remove(b)
        lst.append(b)
lst.sort()
ret.extend(lst)
print(*ret)
