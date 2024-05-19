def binary_search_in_matrix(matrix, target):
    M, N = len(matrix), len(matrix[0])
    left, right = 0, M * N
    mas = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    while left < right:
        m = (left + right) // 2
        if target > mas[m // M][m % M]:
            left = m + 1
        elif mas[m // M][m % M] == target:
            return m % M, m // M
        else:
            right = m
    return -1, -1


# Пример использования
target = 8
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 13]
]

print("Матрица: ")
for i in matrix:
    print(i)
print("Ищем число: ", target)

result = binary_search_in_matrix(matrix, target)

if result:
    print(f"Элемент найден на позиции {result}")
else:
    print("Элемент не найден")