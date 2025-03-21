def solution(brown, yellow):
    if yellow == 1: return [3, 3]
    answer = []
    for i in range(1, yellow):
        if yellow % i != 0: continue
        x = yellow // i
        y = i
        if 4 + 2 * x + 2 * y == brown:
            answer = [x + 2, y + 2]
            break

    return answer
