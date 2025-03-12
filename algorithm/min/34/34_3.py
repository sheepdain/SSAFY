def check(st,ed,book,s):
    while s>0:
        s-=1
        mid=(st+ed)//2
        if books[mid]==book:
            return 1
        elif books[mid]<book:
            st=mid+1
        elif books[mid]>book:
            ed=mid-1
        if st>ed:
            return 0
    return 0

n=int(input())
books=list(input().split())
books.sort()
m=int(input())
lst=[list(input().split()) for i in range(m)]
for i in range(m):
    book=lst[i][0]
    s=lst[i][1]
    if check(0,n-1,book,int(s))==1:
        print('pass')
    else:
        print('fail')