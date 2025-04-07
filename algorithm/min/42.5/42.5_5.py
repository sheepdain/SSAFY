def eat(level, feed, total):
    global max_total
    if level==n:
        max_total=max(total, max_total)
        return
    
    for i in range(3):
        temp1=feed[:]
        e1=temp1[i]
        temp1[i]=0
        for j in range(3,6):
            temp2=temp1[:]
            e2 = temp2[j]
            temp2[j] = 0

            for k in range(1, 5):
                temp3 = temp2[:]
                e3 = temp3[k]
                temp3[k] = 0

                for idx in range(6):
                    temp3[idx] *= 2

                eat(level + 1, temp3, total + e1 + e2 + e3)


arr=list(map(int,input().split()))
n=int(input())
max_total=0
eat(0, arr, 0)
print(max_total)