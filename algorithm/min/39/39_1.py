arr = list(map(int, input().split()))
arr.sort(reverse=True)
n = len(arr)
time = 0
for i in range(1, n):
    time += arr[i] * i
print(time)
