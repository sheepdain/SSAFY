def counsel(day, coin):
    global ret


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
ret = 0
counsel(0, 0)
print(ret)
