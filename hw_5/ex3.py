def queens(n, k):
    board = [[0] * n for _ in range(n)]
    solutions = []
    alph = [chr(i) for i in range(ord('A'), ord('A') + n)]

    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 1:
                return False
        return True

    def arrangement(row):
        if row == k:
            solution = []
            for r in range(n):
                for c in range(n):
                    if board[r][c] == 1:
                        solution.append(f'({alph[r]}, {c + 1})')
            solutions.append(solution)
        else:
            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = 1
                    arrangement(row + 1)
                    board[row][col] = 0
    arrangement(0)
    return solutions


x = queens(8, 8)
print(f"Всего существует {len(x)} позиции")
for i in x:
    print(i)
