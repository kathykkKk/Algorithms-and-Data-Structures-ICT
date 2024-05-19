import numpy as np
import timeit


def input_matrix():
    rows = 3
    columns = 3
    matrix, cnt = [], 1
    while cnt <= rows:
        row = list(map(int, input(f"Enter {columns} elements for row {cnt}: ").split()))
        if len(row) != columns:
            print(f"The string must contain {columns} elements!")
        else:
            matrix.append(row)
            cnt += 1
    return matrix


def print_matrix(matrix):
    n = 0
    for row in matrix:
        for item in row:
            n = max(n, len(str(item)))
    for row in matrix:
        for i in row:
            print(str(i).ljust(n), end=' ')
        print()
    print()


def matrix_det(matrix, parity):
    n = len(matrix[0])
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif n == 1:
        return matrix[0][0]
    det = 0
    for i in range(n):
        modified_matrix = [row[:i] + row[i + 1:] for row in matrix[:0] + matrix[1:]]
        modified_parity = 0 if parity == 1 else 0
        if ((i % 2) + modified_parity) % 2 == 0:
            det += matrix[0][i] * matrix_det(modified_matrix, modified_parity)
        else:
            det -= matrix[0][i] * matrix_det(modified_matrix, modified_parity)
    return det


def inverse_matrix(matrix):
    det = matrix_det(matrix, 0)
    if len(matrix[0]) != len(matrix):
        print("It is impossible to calculate the determinant of a given matrix")
        return None
    if det == 0:
        print("Inverse matrix not defined")
        return None
    inversed = []
    for i in range(len(matrix[0])):
        inversed.append([])
        for j in range(len(matrix)):
            modified_matrix = [row[:i] + row[i + 1:] for row in matrix[:j] + matrix[j + 1:]]
            inversed[i].append(matrix_det(modified_matrix, 0) / det * (-1) ** (i + j))
    return inversed


def inverse_matrix_numpy(matrix):
    return np.linalg.inv(matrix)


#matrix = input_matrix()

# Создаем тестовую матрицу
matrix = [[1, 2, 3], [1, 2, 34], [1, 3, 7]]


# Замеряем время выполнения функции inverse_matrix
time_inv = timeit.timeit('inverse_matrix(matrix)', globals=globals(), number=1000)

# Замеряем время выполнения функции inverse_matrix_numpy
time_inv_numpy = timeit.timeit('inverse_matrix_numpy(matrix)', globals=globals(), number=1000)

print(f"Time for inverse_matrix: {time_inv}")
print(f"Time for inverse_matrix_numpy: {time_inv_numpy}")

