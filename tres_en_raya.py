
from random import randrange

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flag = True


def display_board(board):
    for row in range(len(board)):
        print('+-------+-------+-------+')
        print('|       |       |       |', end='\n|')
        for col in range(len(board[row])):
            print('  ', str(board[row][col]), end='   |')
        print('\n|       |       |       |')
    print('+-------+-------+-------+')


def enter_move(board):
    free_fields = make_list_of_free_fields(board)
    try:
        move_to = int(input('Ingresa tu movimiento:'))
        if move_to > 0 and move_to < 10:
            for posicion in range(len(free_fields)):
                row, column = free_fields[posicion]
                if move_to == board[row][column]:
                    board[row][column] = 'O'
            display_board(board)
            return victory_for(board, 'O')
        else:
            print('Ingrese un valor valido!')
            enter_move(board)
            return True
    except:
        print('Ingrese un valor valido!')
        enter_move(board)
        return True


def make_list_of_free_fields(board):
    list_of_free_fields = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != 'X' and board[row][col] != 'O':
                list_of_free_fields.append((row, col))
    return list_of_free_fields


def victory_for(board, sign):
    free_fields = make_list_of_free_fields(board)

#   Comprobando diagonales
    contador_1 = contador_2 = 0
    for pos in range(len(board)):
        if sign == board[pos][pos]:
            contador_1 += 1
        if sign == board[pos][2-pos]:
            contador_2 += 1
    if contador_1 == 3 or contador_2 == 3:
        print('Las ' + sign + ' han ganado!')
        return False

#   Comprobando filas y columnas
    for row in range(len(board)):
        contador_1 = contador_2 = 0
        for column in range(len(board[row])):
            if sign == board[column][row]:
                contador_1 += 1
            if sign == board[row][column]:
                contador_2 += 1
        if contador_1 == 3 or contador_2 == 3:
            print('Las ' + sign + ' han ganado!')
            return False

#   Comprobar empate
    if len(free_fields) == 0:
        print('Ha sido un empate!')
        return False

    return True


def draw_move(board):
    if board[1][1] == 5:
        board[1][1] = 'X'
        display_board(board)
        return True

    free_fields = make_list_of_free_fields(board)
    number = randrange(len(free_fields))
    row, col = free_fields[number]
    board[row][col] = 'X'
    display_board(board)
    return victory_for(board, 'X')


while flag:
    flag = (draw_move(board) and enter_move(board))
