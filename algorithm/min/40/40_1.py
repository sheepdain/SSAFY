import heapq

arr = [list(map(int, input().split())) for _ in range(4)]
direct = [(1, 0), (0, 1)]
lst = [[[float('inf'), []] for _ in range(4)] for _ in range(4)]
lst[0][0] = [0, [(0, 0)]]

pq = []
heapq.heappush(pq, (0, 0, 0, [(0, 0)]))

while pq:
    cur_damage, y, x, path = heapq.heappop(pq)

    if (y, x) == (3, 3):
        lst[y][x] = [cur_damage, path]
        break

    for dy, dx in direct:
        ny, nx = y + dy, x + dx
        if 0 <= ny < 4 and 0 <= nx < 4:
            new_damage = cur_damage + arr[ny][nx]
            if new_damage < lst[ny][nx][0]:
                lst[ny][nx] = [new_damage, path + [(ny, nx)]]
                heapq.heappush(pq, (new_damage, ny, nx, path + [(ny, nx)]))

for y, x in lst[3][3][1]:
    print(f"{y},{x}")
