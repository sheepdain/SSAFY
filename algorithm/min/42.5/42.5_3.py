def custom_operator(a, b, op):
    if op == "!!":
        return (a - b) * (a + b)
    elif op == "#":
        return max(a, b)
    elif op == "$":
        return a * (2 ** b)
    elif op == "&":
        return (a + b) ** 2


def suhak(idx, value):
    global cnt
    if idx == n - 1:
        if value == 100:
            cnt += 1
        return

    for op in operator:
        new = custom_operator(value, numbers[idx + 1], op)
        suhak(idx + 1, new)


n = int(input())
numbers = list(map(int, input().split()))
operator = ['!!', '#', '$', '&']
cnt = 0
suhak(0, numbers[0])
print(cnt)
