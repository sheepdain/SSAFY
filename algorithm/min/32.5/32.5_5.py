def find(idx):
    if idx == 5:
        print(f'{5}번')
        return

    if arr[1][idx] == '>>':
        find(idx + arr[0][idx])
    elif arr[1][idx] == '<<':
        find(idx - arr[0][idx])
    print(f'{idx}번')


arr = [
    [3, 2, 1, 3, 2, '테러범', 1],
    ['>>', '>>', '<<', '>>', '<<', '테러범', '<<']
]
i = int(input())
find(i)
