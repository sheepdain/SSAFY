n = int(input())
left, right = 0, 51
flag = 0
for i in range(n):
    num, d = input().split()
    if d == 'DOWN':
        right = int(num)
    else:
        left = int(num)
    if left >= right:
        flag = 1
        break
if flag:
    print('ERROR')
else:
    if left + 1 == right - 1:
        print(left + 1)
    else:
        print(f'{left + 1} ~ {right - 1}')
