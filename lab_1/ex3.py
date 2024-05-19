import numpy as np


def input_matrix():
    rows = int(input("Enter number of rows for matrix: "))
    columns = int(input("Enter number of columns for matrix: "))
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


# example
matrix1 = input_matrix()
matrix2 = input_matrix()

print("Matrix 1:")
print_matrix(matrix1)

print("Matrix 2:")
print_matrix(matrix2)

print("Transposed Matrix 1:")
print_matrix(np.transpose(matrix1))

print("Transposed Matrix 2:")
print_matrix(np.transpose(matrix2))

print("Multiplied Matrix:")
print_matrix(np.dot(matrix1, matrix2))

print("Rank of Matrix 1:")
print(np.linalg.matrix_rank(matrix1))

print("Rank of Matrix 2:")
print(np.linalg.matrix_rank(matrix2))

