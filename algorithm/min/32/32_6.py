n, m = map(int, input().split())
member = [[0, []] for _ in range(n)]
for i in range(m):
    num, name = input().split()
    member[int(num)][0] += 1
    member[int(num)][1].append(name)
member.sort(key=lambda x: (-x[0], x))
print(*member[0][1])
