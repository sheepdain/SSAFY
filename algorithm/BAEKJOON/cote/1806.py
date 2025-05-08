n, s=map(int,input().split())
numbers=list(map(int,input().split()))
left, right = 0,0
sum_num=0
ret=100000001
while True:
    if sum_num>=s:
        ret=min(ret, right-left)
        sum_num-=numbers[left]
        left+=1
    elif right==n:
        break
    else:
        sum_num+=numbers[right]
        right+=1
if ret==100000001:
    print(0)
else:
    print(ret)