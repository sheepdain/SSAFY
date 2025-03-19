import sys

sys.stdin = open('input.txt', 'r')


def abc(node):
    if len(arr[node])==2: return int(arr[node][1])
    if arr[node][1] == '+':
        return abc(int(arr[node][2])) + abc(int(arr[node][3]))
    elif arr[node][1] == '-':
        return abc(int(arr[node][2])) - abc(int(arr[node][3]))
    elif arr[node][1] == '*':
        return abc(int(arr[node][2])) * abc(int(arr[node][3]))
    elif arr[node][1] == '/':
        return abc(int(arr[node][2])) / abc(int(arr[node][3]))


T = 10
for tc in range(1, T + 1):
    n = int(input())
    arr = [[]] + [list(input().split()) for _ in range(n)]
    ret = abc(1)
    print(f'#{tc}', int(ret))
