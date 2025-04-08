def num(level,total):
    global min_total, max_total, lst
    if level==n:
        max_total=max(total, max_total)
        min_total=min(total, min_total)
        return
    
    for i in range(4):
        if lst[i]!=0:
            lst[i] -= 1
            if i == 0:
                num(level + 1, total + number[level])
            elif i == 1:
                num(level + 1, total - number[level])
            elif i == 2:
                num(level + 1, total * number[level])
            elif i == 3:
                if total < 0:
                    result = - (abs(total) // number[level])
                else:
                    result = total // number[level]
                num(level + 1, result)
            lst[i] += 1



n=int(input())
number=list(map(int,input().split()))
lst=list(map(int,input().split()))
max_total=-10e8
min_total=10e8
num(1,number[0])
print(max_total)
print(min_total)