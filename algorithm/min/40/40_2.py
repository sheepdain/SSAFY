n=int(input())
dp=[0]*(n+5)
dp[1]=1
dp[2]=2
dp[3]=3
dp[4]=5
i=5
while i<=n:
    dp[i]=dp[i-1]+dp[i-2]
    i+=1
print(dp[n])