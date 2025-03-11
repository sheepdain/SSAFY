def find(member):
    global arr
    if arr[ord(member) - 65] == 0:
        return member
    ret = find(arr[ord(member) - 65])
    arr[ord(member) - 65] = ret
    return ret


def alliance(a, b):
    global arr
    bossa, bossb = find(a), find(b)
    if bossa != bossb:
        arr[ord(bossb) - 65] = bossa
        human_num[ord(bossa) - 65] += human_num[ord(bossb) - 65]


def war(a, b):
    global arr, human_num, live
    bossa, bossb = find(a), find(b)
    if bossa != bossb:
        pop_a = human_num[ord(bossa) - 65]
        pop_b = human_num[ord(bossb) - 65]

        if pop_a > pop_b:
            for i in range(7):
                if find(chr(i + 65)) == bossb:
                    live[i] = 0
        elif pop_b > pop_a:
            for i in range(7):
                if find(chr(i + 65)) == bossa:
                    live[i] = 0


n = int(input())
arr = [0] * 7
human_num = list(map(int, input().split()))
live = [1] * 7
s = int(input())
for i in range(s):
    command, A, B = input().split()
    if command == 'alliance':
        alliance(A, B)
    elif command == 'war':
        war(A, B)
ans = sum(live)
print(ans)
