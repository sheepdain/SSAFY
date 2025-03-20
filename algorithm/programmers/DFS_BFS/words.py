from collections import deque


def solution(begin, target, words):
    if target not in words: return 0
    q = deque([(begin, 0)])
    n = len(begin)
    while q:
        now, step = q.popleft()
        if now == target: return step
        for word in words:
            cnt = 0
            for i in range(n):
                if now[i] != word[i]:
                    cnt += 1
            if cnt == 1:
                q.append((word, step + 1))

    return 0
