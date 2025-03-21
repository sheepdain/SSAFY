def solution(answers):
    b_arr = [2, 1, 2, 3, 2, 4, 2, 5]
    c_arr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a, b, c = 0, 0, 0
    for i, ans in enumerate(answers):
        if i % 5 + 1 == ans: a += 1
        if b_arr[i % 8] == ans: b += 1
        if c_arr[i % 10] == ans: c += 1
    dic = {1: a, 2: b, 3: c}
    answer = [1]
    for idx, num in dic.items():
        if idx == 1: continue
        ret = dic[answer[0]]
        if ret < num:
            answer = [idx]
        elif ret == num:
            answer.append(idx)

    return answer
