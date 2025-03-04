import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = [0] * (N + 1)
    # 노드에 값 입력
    for i in range(M):
        node, num = map(int, input().split())
        arr[node] = num
    # 짝수일 때 마지막 값 더해질 값이 없으므로 부모 노드 값과 같음
    if N % 2 == 0:
        if arr[N]:
            arr[N // 2] = arr[N]
        # i를 2로 나눈 몫이 부모 노드 이므로 i-1과 i값을 더해서 부모 노드에 입력
        for i in range(N - 1, 1, -2):
            if arr[i]:
                arr[i // 2] = arr[i - 1] + arr[i]
            # 출력할 노드 값이 찾아지면 출력 후 중단
            if arr[L]:
                print(f'#{test_case}', arr[L])
                break
    else:
        for i in range(N, 1, -2):
            # i를 2로 나눈 몫이 부모 노드 이므로 i-1과 i값을 더해서 부모 노드에 입력
            if arr[i]:
                arr[i // 2] = arr[i - 1] + arr[i]
            # 출력할 노드 값이 찾아지면 출력 후 중단
            if arr[L]:
                print(f'#{test_case}', arr[L])
                break


