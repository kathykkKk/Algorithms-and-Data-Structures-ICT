def binary_search(array, target):
    left, right = 0, len(array) - 1
    cnt = 0
    while left < right:
        cnt += 1
        m = (left + right) // 2
        if target > m:
            left = m + 1
        else:
            right = m
    return cnt


array = [i for i in range(10)]
for target in array:
    print(target, ' --> ', binary_search(array, target))

