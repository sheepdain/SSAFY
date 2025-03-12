def binary(st,ed):
    MAX=-1
    while 1:
        mid=(st+ed)//2
        if arr[mid]=='#':
            MAX=mid
            st=mid+1
        else:
            ed=mid-1
        if st>ed:
            return MAX


arr=input()
ret=10*(binary(0,9)+1)
print(f'{ret}%')