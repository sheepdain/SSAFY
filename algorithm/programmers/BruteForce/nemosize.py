def solution(sizes):
    w, h = [], []
    for x, y in sizes:
        if x > y:
            w.append(x)
            h.append(y)
        else:
            w.append(y)
            h.append(x)

    answer = max(w) * max(h)
    return answer