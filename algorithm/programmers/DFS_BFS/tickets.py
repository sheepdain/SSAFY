# 틀림

def dfs(air, t_lst):
    global answer

    answer.append(air)
    if air not in t_lst.keys(): return
    t_lst[air].sort()
    for go in t_lst[air]:
        t_lst[air].remove(go)
        dfs(go, t_lst)


def solution(tickets):
    global answer
    ticket_lst = {}
    for st, ed in tickets:
        if st in ticket_lst.keys():
            ticket_lst[st] += [ed]
        else:
            ticket_lst[st] = [ed]

    answer = []
    dfs('ICN', ticket_lst)
    return answer
