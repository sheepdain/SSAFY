# 어려워ㅓ어

def allow(idx, path, score):
    global max_score, lst, used
    if idx == n:
        if max_score < score:
            max_score = score
            lst = path
        return

    allow(idx + 1, path, score)

    if not used[idx]:
        sub = used[:]
        for i in range(-1, 2):
            if 0 <= idx + i < n:
                used[idx + i] = True
        allow(idx + 1, path + [arr[idx]], score + arr[idx])
        used = sub[:]


n = int(input())
arr = list(map(int, input().split()))
max_score = 0
lst = []
used = [False for _ in range(n)]
allow(0, [], 0)
result = "+".join(map(str, lst)) + f"={max_score}"
print(result)
