# 풀리긴 하나 remove를 쓰면 heap 구조가 깨짐 이 점 유의할 것

import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    for command in operations:
        cm = command[0]
        if cm == 'I':
            heapq.heappush(min_heap, int(command[2:]))
            heapq.heappush(max_heap, -int(command[2:]))
        else:
            if min_heap:
                if command[2] == '1':
                    sub = heapq.heappop(max_heap)
                    min_heap.remove(-sub)
                else:
                    sub = heapq.heappop(min_heap)
                    max_heap.remove(-sub)
    if min_heap:
        a = heapq.heappop(min_heap)
        b = heapq.heappop(max_heap)
        answer = [-b, a]
    else:
        answer = [0, 0]
    return answer


arr = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
solution(arr)
