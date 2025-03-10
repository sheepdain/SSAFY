p=int(input())
n=int(input())
for i in range(n):
    p*=2
    p=int(str(p)[::-1])
print(p)