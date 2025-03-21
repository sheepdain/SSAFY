import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) > 1:
        if scoville[0] >= K: break
        tempa = heapq.heappop(scoville)
        tempb = heapq.heappop(scoville)
        ret = tempa + (tempb * 2)
        heapq.heappush(scoville, ret)
        answer += 1
    if len(scoville) == 1:
        if scoville[0] < K:
            answer = -1

    return answer