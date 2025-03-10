def check():
    for i in arr:
        for j in range(5):
            if i[j] != lst[j]:
                break
            if j == 4:
                return 'yes'
    return 'no'


arr = [list(input()) for _ in range(5)]
for i in range(5):
    arr[i][1], arr[i][3] = arr[i][3], arr[i][1]
lst = ['M', 'A', 'P', 'O', 'M']
ret = check()
print(ret)
