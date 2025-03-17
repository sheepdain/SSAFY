def divide(lst):
    global cnt
    m = len(lst)
    if m > 1:
        a = divide(lst[:m // 2])
        b = divide(lst[m // 2:])
        if a[-1] > b[-1]:
            cnt += 1
        return sorted(a + b)
    return lst


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = divide(arr)
    print(f'#{tc}', arr[len(arr) // 2], cnt)
