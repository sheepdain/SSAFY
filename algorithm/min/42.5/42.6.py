def swap(level):
    global ret, arr
    if level == 3:
        score = 0
        for i in range(1, m):
            a, b = arr[i - 1], arr[i]
            if a == b:
                score -= 50
            elif abs(ord(a) - ord(b)) <= 5:
                score += 3
            elif abs(ord(a) - ord(b)) >= 20:
                score += 10
        if score > ret:
            ret = score
        return

    for i in range(m):
        for j in range(i + 1, m):
            new_i, new_j = arr[i], arr[j]
            arr[i], arr[j] = new_j, new_i
            swap(level + 1)
            arr[i], arr[j] = new_i, new_j


arr = list(input())
n = int(input())
m = len(arr)
ret = -21e8
swap(0)
print(ret)
