from collections import Counter

n = int(input())
num_lst = [list(map(int, input().split())) for _ in range(n)]
bit_lst = [list(map(int, input().split())) for _ in range(n)]
ret = []
for i in range(n):
    for j in range(n):
        if bit_lst[i][j] == 1:
            ret.append(num_lst[i][j])
Count = Counter(ret)
ret.sort(key=lambda x: (-Count[x], x))
print(*ret)
