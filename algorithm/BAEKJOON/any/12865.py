n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

# 1차원 DP 배열
dp = [0] * (k + 1)

# 물건을 하나씩 고려
for weight, value in items:
    for j in range(k, weight - 1, -1):  # 무게 k부터 weight까지 거꾸로 탐색
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[k])