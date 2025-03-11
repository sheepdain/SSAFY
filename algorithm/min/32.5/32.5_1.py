arr = ['ABCD', 'ABCE', 'AGEH', 'EIEI', 'FEQE', 'ABAD']
lst = list(input())
ret = 0
for i in range(6):
    lst_cnt = 0
    cnt = 0
    for j in range(4):
        if lst[j] != '?':
            lst_cnt += 1
            if arr[i][j] == lst[j]:
                cnt += 1
    if lst_cnt == cnt and cnt != 0:
        ret += 1
print(ret)
