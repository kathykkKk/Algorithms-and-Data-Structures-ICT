def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
    for i in range(3):
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def check_game_result(board):
    if check_winner(board, 'X'):
        return 'X победил!'
    if check_winner(board, 'O'):
        return 'O победил!'
    if all([cell != ' ' for row in board for cell in row]):
        return 'Ничья!'
    return 'Игра еще не закончена'


# пример
board = [
    ['X', 'O', 'O'],
    ['X', 'X', 'X'],
    ['O', 'X', 'O']
]

result = check_game_result(board)
for i in board:
    print(i)
print(result)
