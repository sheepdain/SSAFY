import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    arr = list(input().split())
    stack = []
    ret = 1
    try:
        for i in arr:
            if i.isdigit():
                stack.append(int(i))
            else:
                if i == '.':
                    if len(stack) == 1:
                        print(f'#{test_case}', stack.pop())
                    else:
                        print(f'#{test_case} error')
                else:
                    b = stack.pop()
                    a = stack.pop()
                    if i == '+':
                        stack.append(a + b)
                    elif i == '-':
                        stack.append(a - b)
                    elif i == '*':
                        stack.append(a * b)
                    elif i == '/':
                        stack.append(a // b)
    except:
        print(f'#{test_case} error')
