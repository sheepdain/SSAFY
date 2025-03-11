from copy import deepcopy
arr = [
    ['A', 'B', 'C', 'E', 'F', 'G'],
    ['H', 'I', 'J', 'K', 'L', 'M'],
    ['N', 'O', 'P', 'Q', 'R', 'S']
]
sub=deepcopy(arr)
lst=input()
directy=[0,-1,1,0,0]
directx=[0,0,0,-1,1]
for k in lst:
    for i in range(3):
        for j in range(6):
            if sub[i][j]==k:
                for t in range(5):
                    dy=i+directy[t]
                    dx=j+directx[t]
                    if 0<=dy<3 and 0<=dx<6:
                        if arr[dy][dx]!='#':
                            arr[dy][dx]='#'
                        else:
                            arr[dy][dx]=sub[dy][dx]
for i in arr:
    print(*i,sep='')