arr = list(input())
a_l = len(arr)
while 1:
    print(*arr, sep='')
    cnt = 0
    for i in range(a_l):
        if ord('A') <= ord(arr[i]) <= ord('Z'):
            cnt += 1
            if arr[i] == 'A':
                arr[i] = '_'
            else:
                arr[i] = chr(ord(arr[i]) - 1)
    if cnt == 0:
        break
