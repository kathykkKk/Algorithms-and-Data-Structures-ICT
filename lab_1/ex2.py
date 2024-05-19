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


def transpose_matrix(matrix):
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed_matrix


def multiplying_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Specified matrices cannot be multiplied")
        return None

    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def rank_of_matrix(matrix):
    mas = matrix.copy()
    rows, columns = len(mas), len(mas[0])
    lead, flag = 0, True
    for r in range(rows):
        if lead < columns:
            i = r
            while mas[i][lead] == 0:
                i += 1
                if i == rows:
                    i = r
                    lead += 1
                    if columns == lead:
                        flag = False
                        break
            if flag:
                mas[i], mas[r] = mas[r], mas[i]
                k = mas[r][lead]
                mas[r] = [item / k for item in mas[r]]
                for i in range(rows):
                    if i != r:
                        k = mas[i][lead]
                        mas[i] = [item - k * item_r for item_r, item in zip(mas[r], mas[i])]
                lead += 1
            else:
                break
        else:
            break
    rank = rows
    for i in mas:
        if i == [0] * columns:
            rank -= 1
    return rank


# example
matrix1 = input_matrix()
matrix2 = input_matrix()

print("Matrix 1:")
print_matrix(matrix1)

print("Matrix 2:")
print_matrix(matrix2)

print("Transposed Matrix 1:")
print_matrix(transpose_matrix(matrix1))

print("Transposed Matrix 2:")
print_matrix(transpose_matrix(matrix2))

print("Multiplied Matrix:")
result = multiplying_matrices(matrix1, matrix2)
if result:
    print_matrix(result)

print("Rank of Matrix 1:")
print(rank_of_matrix(matrix1))

print("Rank of Matrix 2:")
print(rank_of_matrix(matrix2))
