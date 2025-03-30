k=int(input()) # 정점의 개수
n=int(input()) # 간선 정보의 개수
lst=[list(input().split()) for _ in range(n)]
lst.sort(key=lambda x:int(x[2]))
arr=[0]*200

def findboss(m):
    if not arr[ord(m)]:
        return m
    ret=findboss(arr[ord(m)])
    arr[ord(m)]=ret
    return ret

def union(a,b,i):
    global arr,cnt,total_cost
    a_boss,b_boss=findboss(a),findboss(b)
    if a_boss==b_boss:
        return
    total_cost+=int(lst[i][2])
    cnt+=1
    arr[ord(b_boss)]=a_boss

total_cost=0 # 최종 비용
cnt=0 # 연결되는 간선의 개수
for i in range(n):
    if cnt==k-1:
        print(total_cost)
        break
    union(lst[i][0],lst[i][1],i)

# 5
# 8
# A B 9
# A C 3
# A E 7
# B C 14
# B D 11
# C D 1
# C E 5
# A D 20