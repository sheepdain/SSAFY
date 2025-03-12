import heapq

n=int(input())
arr=list(map(int,input().split()))
heapq.heapify(arr)
a=heapq.heappop(arr)
b=heapq.heappop(arr)
stone=[]
num=b*2
stone.append(num)
heapq.heappush(arr,num)
cnt=2
while len(arr)>1:
    a=heapq.heappop(arr)
    b=heapq.heappop(arr)
    if a==stone[0] and b!=stone[0]:
        break
    elif b==stone[0]:
        cnt+=1
        break
    cnt+=2
    num=b*2
    stone.append(num)
    heapq.heappush(arr,num)
print(cnt)