def dfs(level):
    global ans
    if level == n:
        ans += 1
        return

    for i in range(n):
        if used[i] == 1: continue
        if r_up[i + level] == 1 or r_down[i - level + n] == 1: continue
        used[i], r_up[i + level], r_down[i - level + n] = 1, 1, 1
        dfs(level + 1)
        used[i], r_up[i + level], r_down[i - level + n] = 0, 0, 0


T = int(input())
for tc in range(1, 1 + T):
    ans = 0
    n = int(input())
    used = [0] * n
    r_up = [0] * (n * 2)
    r_down = [0] * (n * 2)

    dfs(0)

    print(f'#{tc}', ans)
