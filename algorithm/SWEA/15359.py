import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n, lst = input().split()
    ret = []
    for i in lst:
        if str.isdigit(i):
            num = int(i)
        else:
            num = 10 + (ord(i) - ord('A'))
        a = []
        while len(a) != 4:
            a.append(num % 2)
            num //= 2
        a.reverse()
        ret.extend(a)
    print(f'#{test_case} ', *ret, sep='')
