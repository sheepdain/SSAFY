N = int(input())
cube = [list(map(int, input().split())) for _ in range(N)]

max_score = -21e8

# 백트래킹 탐색 (DFS 방식)
def backtrack(depth):
    global max_score

    # 모든 줄을 회전했으면 점수 계산
    if depth == N:
        col_sums = [0] * N
        for i in range(N):  # 세로줄 합 계산
            for j in range(N):
                col_sums[j] += cube[i][j]

        score = 1
        for val in col_sums:  # 곱셈으로 점수 계산
            score *= val

        max_score = max(max_score, score)
        return

    # 현재 줄을 0 ~ N-1번 회전하며 탐색
    original = cube[depth][:]
    for shift in range(N):
        cube[depth] = original[-shift:] + original[:-shift]  # 줄 회전
        backtrack(depth + 1)

    cube[depth] = original  # 원래 상태로 복원

# DFS 시작
backtrack(0)

print(f"{max_score}점")
