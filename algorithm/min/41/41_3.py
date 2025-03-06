# 입력 받기
T, n = map(int, input().split())
coin = list(map(int, input().split()))

# dp 배열 초기화
dp = [float('inf')] * (T + 1)
dp[0] = 0  # 0원을 만들기 위해서는 동전이 0개

# 동전의 개수 최소화를 위해 DP 배열 갱신
for c in coin:
    for i in range(c, T + 1):
        dp[i] = min(dp[i], dp[i - c] + 1)

# 결과 출력
if dp[T] == float('inf'):
    print("impossible")
else:
    print(dp[T])
