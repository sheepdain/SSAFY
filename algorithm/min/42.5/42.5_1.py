def rotation(idx):
    global ret

    if idx == n:
        nums = []
        for j in range(n):
            num = 0
            for i in range(n):
                num += cube[i][j]
            nums.append(num)
        ans = 1
        for k in range(n):
            ans *= nums[k]
        ret = max(ret, ans)
        return

    origin = cube[idx]
    for rt in range(n):
        cube[idx] = origin[-rt:] + origin[:-rt]
        rotation(idx + 1)
    cube[idx] = origin


n = int(input())
cube = [list(map(int, input().split())) for _ in range(n)]
ret = -21e8
rotation(0)
print(f'{ret}점')
