def smallest_missing_integer(arr):
    max_num, min_num = max(arr), min(arr)
    if min_num < 0:
        minus = [0] * (- min_num + 1)
    else:
        minus = [0]
    plus = [0] * (max_num + 1)
    for num in arr:
        if num <= 0:
            minus[-num] = 1
        else:
            plus[num] = 1
    if 0 in minus:
        return minus[::-1].index(0) + min_num
    if 0 in plus[1:]:
        return plus.index(0) + 1
    return max_num + 1


arr = [5, 4, 2, -1, -3, 0]
print(f"Наименьшее пропущенное целое число в массиве {arr}: {smallest_missing_integer(arr)}")
