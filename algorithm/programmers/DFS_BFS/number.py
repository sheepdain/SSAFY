def dfs(level, num, n, numbers, target):
    global answer
    if level == n:
        if num == target:
            answer += 1
        return

    dfs(level + 1, num + numbers[level], n, numbers, target)
    dfs(level + 1, num - numbers[level], n, numbers, target)


def solution(numbers, target):
    global answer
    n = len(numbers)
    answer = 0
    dfs(0, 0, n, numbers, target)
    return answer


'''
이..이게 뭐지?
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
'''
