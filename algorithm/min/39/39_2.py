n = int(input())
money = [500, 100, 50, 10]
cnt = 0
for i in range(4):
    if n >= money[i]:
        cnt += n // money[i]
        n %= money[i]
print(cnt)
