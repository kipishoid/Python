#  Создайте программу для игры в "Крестики-нолики".


def main():
    board = [["_" for _ in range(3)] for _ in range(3)]
    flag = True
    game_over = False
    while not game_over:
        print_board(board)
        try:
            selection = convert_selection(select_square())
            place_turn(selection, flag, board)
        except ValueError:
            print('Извините, пожалуйста, выберите клетку 1-9')
            continue
        game_over = is_win(board) or is_draw(board)
        flag = not flag


def is_draw(board):
    for row in board:
        for val in row:
            if val == '_':
                return False
    print('Ничья, ходов нет!')
    return True


def is_win(board):
    winner = None
    for i in range(3):
        # Горизонталь
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":
            winner = board[i][0]
            break
        # Вертикаль
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_":
            winner = board[0][i]
            break
    # Диагональ
    if board[1][1] != "_":
        if (board[0][0] == board[1][1] == board[2][2]
                or board[0][2] == board[1][1] == board[2][0]):
            winner = board[1][1]
    if winner is not None:
        print_board(board)
        print(f"{winner} is the winner!")
        return True
    return False


def convert_selection(selection):
    selection -= 1
    return (selection // 3, selection % 3)


def place_turn(selection, flag, board):
    i, j = selection
    if board[i][j] == '_':
        board[i][j] = 'X' if flag else 'O'
    else:
        raise ValueError


def print_board(board):
    for row in board:
        print(row)


def select_square():
    selection = int(input('Выбери квадрат: '))
    if not 1 <= selection <= 9:
        raise ValueError
    return selection


if __name__ == "__main__":
    main()
