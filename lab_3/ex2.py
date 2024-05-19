def o_3n(mas):
    summary = 0
    for i in mas:
        temp = 1
        for j in range(3):
            temp *= i
        summary += temp
    return summary


def merge_sort(mas):
    if len(mas) <= 1:
        return mas
    middle = len(mas) // 2
    left = merge_sort(mas[:middle])
    right = merge_sort(mas[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def generate_permutations(mas, n, i):
    if i == n:
        print(mas)
    else:
        for j in range(i, n):
            mas[i], mas[j] = mas[j], mas[i]
            generate_permutations(mas, n, i + 1)
            mas[i], mas[j] = mas[j], mas[i]


def multiplying_matrices(matrix1, matrix2):
    n = len(matrix1)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def binary_search(array, target1, traget2, target3):
    targets = [target1, traget2, target3]
    for target in targets:
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


print(int(4))