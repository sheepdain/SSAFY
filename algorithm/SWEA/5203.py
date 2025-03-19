def check(lst):
    lst.sort()
    i, j = 1, 1
    for k in range(1, len(lst)):
        if lst[k] == lst[k - 1]:
            i += 1
            if i == 3:
                return 1
        else:
            i = 1
            if lst[k] == lst[k - 1] + 1:
                j += 1
                if j == 3:
                    return 1
            else:
                j = 1
    return 0


def result():
    p1, p2 = [], []
    for n in range(0, 12, 2):
        p1.append(arr[n])
        p2.append(arr[n + 1])
        if n >= 4:
            if check(p1):
                print(f'#{tc}', 1)
                return
            if check(p2):
                print(f'#{tc}', 2)
                return
    print(f'#{tc}', 0)
    return


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    result()
