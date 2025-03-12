def binary(target):
    left, right = 1, target
    ans = 1
    while left <= right:
        mid = (left + right) // 2
        if mid ** 2 == target:
            return mid
        elif mid ** 2 < target:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans


n = int(input())
ret = binary(n)
print(ret)
