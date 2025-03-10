arr = [1, 2, 3, 3, 5, 1, 0, 1, 3]
n = int(input())
sub = sum(arr[:n])
cost = 21e8
for i in range(9 - n):
    sub = sub - arr[i] + arr[i + n]
    cost = min(cost, sub)
print(cost)
