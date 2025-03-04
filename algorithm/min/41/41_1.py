n=int(input())
p=[0]*(n+1)
p[0]=0
p[1]=1
if n>=2:
    for i in range(2,n):
        p[i]=p[i-2]+p[i-1]
print(p[n-1])