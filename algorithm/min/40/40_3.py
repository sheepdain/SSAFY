arr = list(map(int, input().split()))
lst = [-21e8] * 13
lst[0] = 0
lst[2] = arr[2]
lst[3] = arr[3]
for i in range(4, 12):
    a = lst[i - 2]
    b = lst[i - 3]
    lst[i] = max(a, b) + arr[i]
    if i % 2 == 0:
        c = lst[i // 2]
        lst[i] = max(lst[i], (c + arr[i]))
print(max(lst[11],lst[10], lst[9], lst[6]))
