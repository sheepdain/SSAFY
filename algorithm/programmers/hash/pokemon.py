nums=[3, 3, 3, 2, 2, 2]
ret = len(nums)
num_s = set()
for i in range(ret):
    num_s.add(i)
answer = ret / 2

if answer > len(num_s):
    answer = len(num_s)
print(answer)