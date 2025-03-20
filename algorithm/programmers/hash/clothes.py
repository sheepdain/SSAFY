def solution(clothes):
    dic = {}
    for name, kind in clothes:
        if kind in dic.keys():
            dic[kind] += [name]
        else:
            dic[kind] = [name]
    answer = 1
    for _, value in dic.items():
        answer *= (len(value) + 1)
    return answer - 1


'''
# 참고
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1
'''
