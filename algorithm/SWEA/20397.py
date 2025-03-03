import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    for t in range(m):
        i, j = map(int, input().split())
        for k in range(1,j+1):
            a, b = i - 1 - k, i - 1 + k
            if a >= 0 and b < n:
                if arr[a] == arr[b]:
                    arr[a] = 1 - arr[a]
                    arr[b] = arr[a]

    print(f'#{test_case}', *arr)
