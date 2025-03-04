import sys

sys.stdin = open('input.txt', 'r')

def dfs(nd):
    global cnt
    for i in node[nd]:
        dfs(i)
        cnt+=1

T = int(input())
for test_case in range(1, T + 1):
    e,n=map(int,input().split())
    arr=list(map(int,input().split()))
    node=[[] for _ in range(e+2)]
    for i in range(0,len(arr),2):
        node[arr[i]].append(arr[i+1])
    cnt=1
    dfs(n)
    print(f'#{test_case}',cnt)