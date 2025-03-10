n = int(input())
names = [input() for _ in range(n)]
for i in range(n):
    if names[i] == names[i].capitalize():
        pass
    elif names[i].islower():
        names[i] = names[i].capitalize()
    else:
        names[i] = names[i].upper()
names.sort()
for i in range(n):
    print(names[i])
