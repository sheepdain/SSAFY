def max_land_value(grid):
    max_value = 0
    rows = len(grid)
    cols = len(grid[0])

    # 직사각형 영역을 찾아서 그 합을 구하기 위해 다중 for문 사용
    for r1 in range(rows):
        for c1 in range(cols):
            if grid[r1][c1] == 0:  # 0인 곳은 시작점으로 사용할 수 없으므로 건너뛴다
                continue
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    # 직사각형 범위 내에 0이 있는지 확인
                    has_zero = False
                    for i in range(r1, r2 + 1):
                        for j in range(c1, c2 + 1):
                            if grid[i][j] == 0:
                                has_zero = True
                                break
                        if has_zero:
                            break

                    if has_zero:
                        continue  # 0이 있으면 이 직사각형은 건너뛴다

                    # 직사각형 영역의 값을 구하기
                    value = 0
                    for i in range(r1, r2 + 1):
                        for j in range(c1, c2 + 1):
                            value += grid[i][j]

                    # 최대값 갱신
                    max_value = max(max_value, value)

    return max_value


# 입력 받기
grid = []
for _ in range(4):
    grid.append(list(map(int, input().split())))

# 최대 가치 출력
print(max_land_value(grid))
