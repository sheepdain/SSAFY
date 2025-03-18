from collections import deque

def one(a, b):
    return (a - b) * (a + b)


def two(a, b):
    return max(a, b)


def three(a, b):
    return a ** 2 - b ** 2


def fore(a, b):
    return (a + b) ** 2


n=int(input())
arr=list(map(int,input().split()))
q=deque()
q.append((arr[0],arr[1]))
while q:
